# Facing the Probabilistic World That Coding Agents Present

2026-07-07. Non-normative.
Related: [Target End State](./2026-07-05-rationale-target-end-state.md), [The Adjudicator and Phases](./2026-07-05-rationale-adjudicator-centered-collaboration.md), [Repository-Native Planning](./2026-07-05-rationale-repository-native-planning-and-change-control.md), [Design First and Context](./2026-07-05-rationale-design-first-minimal-context.md), [Normative vs Reading](./2026-07-06-rationale-normative-vs-reading-documents.md).

> Japanese original (authoritative): [../2026-07-07-rationale-saas-agent-as-sandbox.md](../2026-07-07-rationale-saas-agent-as-sandbox.md) at commit `ee96d31` (`ee96d310e76897c49fd62348a1fc9e7434019a96`). Terminology and critical-review fixes (adopter, analogies, less repetition): [../README.md](../README.md) and [README.md](./README.md). If English lags, prefer Japanese.

---

Suppose you give the same request to the same coding agent a second time. The second run will likely produce a similar change. It will not necessarily follow the same investigation path, make the same judgments, or land on the same diff. Not only the model output, but which files it reads first, which tools it calls, and which test failures it observes can change the path that follows.

That property is not a defect. It is the source of the power to explore design candidates humans cannot fully enumerate and turn them into concrete proposals quickly. Evaluation research on code generation also shows that exploring multiple samples reaches functionally correct solutions more readily than a single generation. On HumanEval, Chen et al. (2021) reported that problems unsolved with one sample become solvable at much higher rates when many samples are drawn and checked. AlphaCode generates large numbers of candidate programs per problem, then filters and clusters them with example tests; in a simulated Codeforces evaluation it scored about the 54th percentile among participants on average (Li et al., 2022). Those studies measure sampling for function synthesis and contest problems, not path divergence in coding agents that operate tools. The latter is an observation of this essay. Either way, the proposal in front of you must not be mistaken for the only answer or an inevitable finished form. What this essay calls "facing the probabilistic world" is not a refusal of that power; it is accepting, as a human problem, **on what grounds a single generation should be admitted into the project**.

## The Metaphor of Choosing a Finished Artifact

A language model assigns probabilities to the next token given context and produces one continuation under a decoding method. Sampling is one way to draw a continuation from that distribution (Holtzman et al., 2020). A coding agent does not stop after one generation. The model emits reasoning and actions, receives observations from tools or the environment, adds them to the next context, and generates again. That iterative thought–action–observation shape also appears in the basic agent loop shown by ReAct (Yao et al., 2023).

So the phrase "a coding agent is a machine that picks one finished artifact from among possible ones" does not describe internal mechanics literally. Finished artifacts are not lined up in a warehouse waiting to be taken. Generation and observation at each step change the next options, and one path arrives at one result. **Choosing from finished artifacts is a metaphor that looks at this path-dependent generative process from the side of the design space.**

The metaphor matters because it changes the epistemic place of a diff or PR. Chen et al. (2021) note that the space of functionally equivalent programs is large enough that string match to a reference solution cannot measure it. They also showed that BLEU distributions for generated code overlap heavily between correct and incorrect answers, so surface similarity is a poor proxy for functional correctness. Human evaluation of summarization likewise found many hallucinations that are unfaithful to the input, and that automatic metrics such as ROUGE alone cannot measure faithfulness (Maynez et al., 2020). So even when the output is fluent, tests pass, and the explanation is coherent, it is still "a candidate obtained from this input and this path." It is not a unique solution proven correct. Conversely, being generated probabilistically does not by itself make an output wrong. Deterministic processing can err; probabilistic generation can be right. What to ask is not an impression of the generation method, but **whether the grounds for accepting the candidate are in place**.

## Narrow the Possibilities Before Generating

Waiting until post-generation review to consider acceptance is already late. What you pass to the agent changes the design space it can see. Shi et al. (2023) also report experimentally that irrelevant context can hurt language-model performance. More context is not safer; it must be chosen for the purpose.

That is why this template enumerates documents per Operating Path and has Design Intake state include/omit, items not to guess, and target boundaries up front. Splitting what agents read as norms from what stays outside as reading material is left to [Normative vs Reading](./2026-07-06-rationale-normative-vs-reading-documents.md); payload design itself is left to [Design First and Context](./2026-07-05-rationale-design-first-minimal-context.md). Acceptance specifications set the goal, dependency boundaries set allowed structure, and the chosen context sets the initial conditions of search. These do not hand the agent the answer. They do drop irrelevant regions from the distribution of possibilities and narrow candidates to a range humans can verify. AlphaCode likewise separates search from settling submission candidates by placing example-test filtering and clustering after mass generation (Li et al., 2022). This template similarly separates exploration from acceptance, and places part of that separation in pre-generation input design and post-generation human approval.

Here `[DESIGN CHECK]` is not a mechanism that discloses the model's internal thought. It is an external contract, shared with humans before generation, about what counts as input, what is demanded as output, and under which assumptions and open questions the work proceeds. It is also an observable starting point for later asking why a change took the form it did.

## Receive Candidates Under Three Responsibilities

`docs/collaboration/ai-human-scheme.md` splits collaboration into three roles.

1. **Agent** generates candidates inside the approved scope and phase, and makes changes and verification results visible.
2. **Deterministic Tool** checks mechanically decidable properties with formatters, linters, tests, and the like.
3. **Adjudicator** owns decision points in light of specifications, design intent, risk, and trade-offs.

The split is not there to distrust the Agent. Nor does it claim that deterministic tools can guarantee truth. As Dijkstra (1970) wrote, "Program testing can be used to show the presence of bugs, but never to show their absence!" Passing tests can show the absence of known failures under the stated conditions; it is not a proof that bugs are absent. Correctness outside the specification and the soundness of design intent are judgments beyond that. Linters likewise cover only mechanically checkable properties. Humans err too. The point of splitting roles is to make clear what each judged on what grounds, and not to let failure end with "the AI hallucinated."

Switching to a stronger model or re-examining with multiple agents can change candidate quality and search breadth. It does not replace Adjudicator approval. However often models agree with one another, that agreement is not a project decision. The asymmetry between generative capacity and acceptance responsibility does not vanish with agent count or capability. Who owns decision points and phases is treated in [The Adjudicator and Phases](./2026-07-05-rationale-adjudicator-centered-collaboration.md).

## Phases Make Candidates Concrete Step by Step

AT-TDD phases are also structure that keeps probabilistic generation from looking like a finished product in one shot. Phase 1 moves the acceptance specification into a testable form. Phase 2 narrows candidates to the minimal implementation that satisfies reviewed tests. Phase 3 revisits structure and readability without changing behavior. Confirming each phase's result with a human before moving on treats goal, implementation, and structure as separate judgment points.

Finally, PRs and review place changes, verification results, and judgments into lasting artifacts. Why judgments belong in the repository rather than chat history is stated in [Repository-Native Planning](./2026-07-05-rationale-repository-native-planning-and-change-control.md). CI can check part of that mechanically; it does not automatically approve specification soundness or design intent. As Chen et al. (2021) note, passing unit tests is a practical acceptance criterion in human development too. Per Dijkstra's warning, it is still not proof that "there are no bugs." Deciding to integrate into the project is not an extension of generation; it is an act on the acceptance side.

## Freedom to Generate, Strictness to Accept

Nothing above is meant to shrink the agent's freedom. Inside an approved scope, it is better to try multiple options, restart from failure, and search for better paths. What code-generation research shows is that the breadth of search itself raises the rate of reaching solutions (Chen et al., 2021; Li et al., 2022). Turning free exploration into value requires explicit acceptance conditions on the outside.

The operational contracts, Operating Paths, acceptance specifications, phase gates, and persisted artifacts this template places in the repository are scaffolding for sharing that boundary (the overall picture is [Target End State](./2026-07-05-rationale-target-end-state.md)). They do not turn probabilistic generation into something deterministic. Rather, they ensure that **whatever candidate appears, the same responsibility structure can verify, accept, or reject it.**

In the world coding agents present, other implementations, other paths, and other finished forms are always possible. That is why the human job is not to rubber-stamp the first proposal as correct. It is to narrow possibilities appropriately, put them in a verifiable form, and take responsibility for the one adopted. That is facing the probabilistic world.

## References

1. **Probabilistic generation and agent loops**
   - Holtzman, A. et al. "The Curious Case of Neural Text Degeneration." ICLR 2020 / arXiv:1904.09751. https://arxiv.org/abs/1904.09751 (Retrieved 2026-07-26. Peer-reviewed conference paper. Sampling from language-model distributions / nucleus sampling)
   - Yao, S. et al. "ReAct: Synergizing Reasoning and Acting in Language Models." ICLR 2023 / arXiv:2210.03629. https://arxiv.org/abs/2210.03629 (Retrieved 2026-07-26. Peer-reviewed conference paper. General agent shape that iterates reasoning, action, and environment observation)
2. **Multiple candidates and functional correctness in code generation**
   - Chen, M. et al. "Evaluating Large Language Models Trained on Code." arXiv:2107.03374. https://arxiv.org/abs/2107.03374 (Retrieved 2026-07-26. Pre-peer-review technical report. HumanEval / pass@k. Multiple sampling, size of functionally equivalent solution space, mismatch between BLEU and functional correctness)
   - Li, Y. et al. "Competition-level code generation with AlphaCode." *Science* 378(6624):1092–1097, 2022 / arXiv:2203.07814. https://www.science.org/doi/10.1126/science.abq1158 (Retrieved 2026-07-26. Peer-reviewed paper. Example-test filter/clustering after mass sampling. About 54th percentile average in simulated Codeforces evaluation)
3. **Hallucination and faithfulness (summarization)**
   - Maynez, J. et al. "On Faithfulness and Factuality in Abstractive Summarization." ACL 2020 / arXiv:2005.00661. https://aclanthology.org/2020.acl-main.173/ (Retrieved 2026-07-26. Peer-reviewed conference paper. Summarization. Reports frequent hallucinations in human evaluation and that ROUGE-like metrics alone do not measure faithfulness. Not evidence about code generation itself)
4. **Context selection**
   - Shi, F. et al. "Large Language Models Can Be Easily Distracted by Irrelevant Context." ICML 2023 / arXiv:2302.00093. https://arxiv.org/abs/2302.00093 (Retrieved 2026-07-07. Peer-reviewed conference paper)
5. **Limits of testing**
   - Dijkstra, E. W. "Notes on Structured Programming" (EWD249), 1970. https://www.cs.utexas.edu/~EWD/transcriptions/EWD02xx/EWD249/EWD249.html (Retrieved 2026-07-26. Public transcript of the author's draft. "Program testing can be used to show the presence of bugs, but never to show their absence!")
6. **Project-internal norms**
   - `AGENTS.md`, `CLAUDE.md`
   - `docs/architecture/agent-quickstart.md`
   - `docs/collaboration/ai-human-scheme.md`
   - `docs/at-tdd/process.md`
