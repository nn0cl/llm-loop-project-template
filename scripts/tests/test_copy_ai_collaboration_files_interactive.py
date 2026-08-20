#!/usr/bin/env python3
"""Pty-based tests for scripts/copy-ai-collaboration-files.sh's interactive
prompting behavior (LISS-0054).

Each test method below proves exactly one Gherkin scenario in
docs/specs/interactive-copy-script.feature.md -- see the comment above each
test for which scenario it covers.

Harness notes:
- Uses only the Python standard library (pty, select, os, subprocess,
  tempfile, unittest) -- no third-party test dependency. python3 is already
  a required tool in this repository's own toolchain
  (scripts/check-contract-consistency.py, invoked directly by CI), so this
  adds no new environment requirement; the *shipped* script stays bash-only
  (see docs/collaboration/agreements/2026-08-20-interactive-copy-script.md's
  Boundaries section).
- Reads from the pseudo-terminal in a bounded-timeout polling loop
  (select.select with a short per-iteration timeout, checked against an
  overall wall-clock timeout), not a single fixed sleep -- see
  docs/work-plans/WP-0018-interactive-copy-script.md's "Risks" section on
  pty timing sensitivity.

Run directly:
  python3 scripts/tests/test_copy_ai_collaboration_files_interactive.py
"""

from __future__ import annotations

import os
import pty
import select
import shutil
import signal
import subprocess
import tempfile
import time
import unittest
from pathlib import Path

SCRIPT_PATH = str(
    Path(__file__).resolve().parent.parent / "copy-ai-collaboration-files.sh"
)

DEFAULT_TIMEOUT = 10.0

# Exact prompt/message text this issue's design contract pins down. Keeping
# these as named constants means a wording change only needs to happen in
# one place, and a test failure names exactly which string diverged.
TARGET_PROMPT = "Target repository directory (required): "
TARGET_EMPTY_MESSAGE = "A target directory is required."
PROJECT_NAME_PROMPT = "Project name (optional, press Enter to skip): "
DOMAIN_SUMMARY_PROMPT = "One-line domain summary (optional, press Enter to skip): "
STACK_PROMPT = "Stack (optional, press Enter to skip): "
TARGET_REQUIRED_ERROR = "--target is required."


class ScriptTimeout(AssertionError):
    """The script did not finish, or an expected prompt never appeared,
    within the bounded polling timeout.

    This is a test failure, not test-infrastructure noise: per the spec, a
    non-interactive or --non-interactive invocation must never block on
    stdin, so a timeout in those scenarios is exactly the failure the
    scenario forbids.
    """


def run_interactive(args, responses, timeout=DEFAULT_TIMEOUT):
    """Runs the script under a real pseudo-terminal (pty.fork()), so the
    script's own is_interactive_tty() check sees a real TTY on both stdin
    and stdout.

    responses: an ordered list of (trigger_text, response_text) pairs. Each
    trigger is searched for in the cumulative captured output, in order,
    starting from just past the previous match -- this ensures a repeated
    prompt (e.g. the target prompt shown twice on a re-prompt) is matched
    once per occurrence rather than the same earlier occurrence satisfying
    every subsequent entry. response_text is written to the pty verbatim
    (include the trailing "\\n" to submit a line; "" to leave the field
    empty and press Enter).

    Returns (combined_output, exit_code).
    """
    pid, fd = pty.fork()
    if pid == 0:
        # Child: replace this process with the script under test. A real
        # TTY is already attached by pty.fork().
        try:
            os.execvp("bash", ["bash", SCRIPT_PATH, *args])
        except OSError:
            os._exit(127)
        return  # unreachable

    output = b""
    search_pos = 0
    resp_idx = 0
    start = time.monotonic()
    status = None

    while True:
        if time.monotonic() - start > timeout:
            try:
                os.kill(pid, signal.SIGKILL)
            except ProcessLookupError:
                pass
            os.waitpid(pid, 0)
            raise ScriptTimeout(
                "Timed out after %.1fs waiting for script (args=%r, "
                "responses consumed=%d/%d).\nOutput so far:\n%s"
                % (timeout, args, resp_idx, len(responses), output.decode(errors="replace"))
            )

        ready, _, _ = select.select([fd], [], [], 0.2)
        if fd in ready:
            try:
                chunk = os.read(fd, 4096)
            except OSError:
                chunk = b""
                time.sleep(0.01)
            if chunk:
                output += chunk
                while resp_idx < len(responses):
                    trigger, response = responses[resp_idx]
                    idx = output.find(trigger.encode(), search_pos)
                    if idx == -1:
                        break
                    os.write(fd, response.encode())
                    search_pos = idx + len(trigger.encode())
                    resp_idx += 1

        wpid, status = os.waitpid(pid, os.WNOHANG)
        if wpid == pid:
            break

    # Drain any remaining buffered output without blocking further.
    while True:
        ready, _, _ = select.select([fd], [], [], 0)
        if fd not in ready:
            break
        try:
            chunk = os.read(fd, 4096)
        except OSError:
            break
        if not chunk:
            break
        output += chunk

    try:
        os.close(fd)
    except OSError:
        pass

    exit_code = os.WEXITSTATUS(status) if os.WIFEXITED(status) else -1
    return output.decode(errors="replace"), exit_code


def run_non_interactive(args, timeout=DEFAULT_TIMEOUT):
    """Runs the script with stdin redirected from /dev/null -- not a TTY --
    so is_interactive_tty() is false regardless of --non-interactive. This
    mirrors how the existing CI "Check template copy smoke test" step
    already invokes the script (no controlling terminal).
    """
    proc = subprocess.run(
        ["bash", SCRIPT_PATH, *args],
        stdin=subprocess.DEVNULL,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        timeout=timeout,
    )
    return proc.stdout.decode(errors="replace"), proc.returncode


class InteractiveCopyScriptTests(unittest.TestCase):
    def setUp(self):
        self.base_dir = tempfile.mkdtemp(prefix="civ-copy-script-test-")

    def tearDown(self):
        shutil.rmtree(self.base_dir, ignore_errors=True)

    def _new_target_dir(self):
        return tempfile.mkdtemp(dir=self.base_dir)

    # Scenario: Prompt for the required target directory when omitted, interactively
    def test_prompts_for_missing_target_when_omitted_interactively(self):
        target = self._new_target_dir()
        output, exit_code = run_interactive(
            [
                "--project-name", "Proj",
                "--domain-summary", "Summary",
                "--stack", "Stack",
                "--dry-run",
            ],
            responses=[(TARGET_PROMPT, target + "\n")],
        )
        self.assertIn(TARGET_PROMPT, output)
        self.assertNotIn(TARGET_REQUIRED_ERROR, output)
        self.assertEqual(0, exit_code, output)

    # Scenario: Re-prompt when the target prompt receives an empty response
    def test_reprompts_target_on_empty_response(self):
        target = self._new_target_dir()
        output, exit_code = run_interactive(
            [
                "--project-name", "Proj",
                "--domain-summary", "Summary",
                "--stack", "Stack",
                "--dry-run",
            ],
            responses=[
                (TARGET_PROMPT, "\n"),
                (TARGET_PROMPT, target + "\n"),
            ],
        )
        self.assertIn(TARGET_EMPTY_MESSAGE, output)
        self.assertEqual(
            2,
            output.count(TARGET_PROMPT),
            "expected the target prompt to be printed twice: %r" % output,
        )
        self.assertEqual(0, exit_code, output)

    # Scenario: Prompt for each missing optional value once, stating it is optional
    def test_prompts_for_each_missing_optional_value_once(self):
        target = self._new_target_dir()
        output, exit_code = run_interactive(
            ["--target", target, "--dry-run"],
            responses=[
                (PROJECT_NAME_PROMPT, "MyProj\n"),
                (DOMAIN_SUMMARY_PROMPT, "Does things\n"),
                (STACK_PROMPT, "Python\n"),
            ],
        )
        self.assertEqual(1, output.count(PROJECT_NAME_PROMPT), output)
        self.assertEqual(1, output.count(DOMAIN_SUMMARY_PROMPT), output)
        self.assertEqual(1, output.count(STACK_PROMPT), output)
        self.assertEqual(0, exit_code, output)

    # Scenario: Empty response to an optional prompt skips placeholder replacement
    def test_empty_optional_response_skips_placeholder_replacement(self):
        target = self._new_target_dir()
        # Not --dry-run: replace_placeholders() is a no-op under --dry-run,
        # so this scenario needs a real copy to prove the skip end-to-end.
        output, exit_code = run_interactive(
            ["--target", target],
            responses=[
                (PROJECT_NAME_PROMPT, "\n"),
                (DOMAIN_SUMMARY_PROMPT, "\n"),
                (STACK_PROMPT, "\n"),
            ],
            timeout=30.0,
        )
        self.assertEqual(0, exit_code, output)
        copied_claude_md = Path(target) / "CLAUDE.md"
        self.assertTrue(copied_claude_md.exists(), output)
        content = copied_claude_md.read_text(encoding="utf-8")
        self.assertIn(
            "<PROJECT_NAME:",
            content,
            "expected the PROJECT_NAME placeholder to remain unreplaced "
            "when every optional prompt got an empty response",
        )

    # Scenario: A supplied flag is never prompted for
    def test_supplied_flags_are_never_prompted_for(self):
        target = self._new_target_dir()
        output, exit_code = run_interactive(
            [
                "--target", target,
                "--project-name", "Proj",
                "--domain-summary", "Summary",
                "--stack", "Stack",
                "--dry-run",
            ],
            responses=[],
        )
        for prompt in (
            TARGET_PROMPT,
            PROJECT_NAME_PROMPT,
            DOMAIN_SUMMARY_PROMPT,
            STACK_PROMPT,
        ):
            self.assertNotIn(prompt, output)
        self.assertEqual(0, exit_code, output)

    # Scenario: Non-interactive shell skips all prompting
    def test_non_interactive_shell_skips_all_prompting(self):
        output, exit_code = run_non_interactive([])
        for prompt in (
            TARGET_PROMPT,
            PROJECT_NAME_PROMPT,
            DOMAIN_SUMMARY_PROMPT,
            STACK_PROMPT,
        ):
            self.assertNotIn(prompt, output)
        self.assertIn(TARGET_REQUIRED_ERROR, output)
        self.assertEqual(2, exit_code, output)

    # Scenario: --non-interactive forces flag-only behavior even in a real terminal
    def test_non_interactive_flag_forces_flag_only_behavior(self):
        output, exit_code = run_interactive(
            ["--non-interactive"],
            responses=[],
            timeout=5.0,
        )
        for prompt in (
            TARGET_PROMPT,
            PROJECT_NAME_PROMPT,
            DOMAIN_SUMMARY_PROMPT,
            STACK_PROMPT,
        ):
            self.assertNotIn(prompt, output)
        self.assertIn(TARGET_REQUIRED_ERROR, output)
        self.assertEqual(2, exit_code, output)

    # Scenario: Prompts still fire under --dry-run
    def test_prompts_still_fire_under_dry_run(self):
        target = self._new_target_dir()
        output, exit_code = run_interactive(
            ["--dry-run"],
            responses=[
                (TARGET_PROMPT, target + "\n"),
                (PROJECT_NAME_PROMPT, "Proj\n"),
                (DOMAIN_SUMMARY_PROMPT, "Summary\n"),
                (STACK_PROMPT, "Stack\n"),
            ],
        )
        self.assertIn(TARGET_PROMPT, output)
        self.assertIn(PROJECT_NAME_PROMPT, output)
        self.assertIn(DOMAIN_SUMMARY_PROMPT, output)
        self.assertIn(STACK_PROMPT, output)
        self.assertEqual(0, exit_code, output)
        # dry-run must have no visible effect: nothing actually written.
        self.assertEqual([], os.listdir(target), output)

    # Scenario: --force and --dry-run stay flag-only, never prompted
    def test_force_and_dry_run_stay_flag_only_never_prompted(self):
        target = self._new_target_dir()
        # Neither --force nor --dry-run passed: a real copy runs.
        output, exit_code = run_interactive(
            [
                "--target", target,
                "--project-name", "Proj",
                "--domain-summary", "Summary",
                "--stack", "Stack",
            ],
            responses=[],
            timeout=30.0,
        )
        self.assertEqual(0, exit_code, output)
        self.assertNotIn("force", output.lower())
        self.assertIn("Existing files were left unchanged", output)


if __name__ == "__main__":
    unittest.main()
