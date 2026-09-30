from pathlib import Path
import re
root=Path(__file__).resolve().parents[4]
guide=root/'docs/collaboration/native-subagent-loop-compatibility.md'
template=root/'docs/templates/agent-tool-conformance.md'
g=guide.read_text();t=template.read_text()
for tool in ['Codex','Claude Code','Cursor','Grok Build','GitHub Copilot','Google Antigravity']:
 assert '### '+tool in g,tool
rows=[line for line in g.splitlines() if re.match(r'^\| [1-8] ',line)]
assert len(rows)==8
assert all(len(line.split('|'))==9 for line in rows)
for term in ['Verified','Inferred','Unknown','base commit','attempt ID','event ID','Director','fork','cloud/API']:
 assert term.lower() in g.lower(),term
for term in ['Duplicate/stale','Deliberate review','Billing','Reviewer input allowlist','Attempt ID','Output manifest','Eight-stage','Director close absent']:
 assert term.lower() in t.lower(),term
for p in [guide,template,root/'docs/collaboration/adoption-guide.md']:
 for target in re.findall(r'\]\(([^)]+)\)',p.read_text()):
  if target.startswith(('https:','http:','#')):continue
  assert (p.parent/target.split('#')[0]).exists(),(p,target)
print('PASS six tool sections, eight stage cells, evidence/failure fields, touched relative links')
print('LIMIT: structural checks do not certify native behavior, source correctness or account entitlement')
