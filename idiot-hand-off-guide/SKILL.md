---
name: idiot-hand-off-guide
description: "Create a single, self-contained implementation handoff containing exact code changes, ordered application steps, and verification criteria for another model to execute. Use when the user requests IdiotHandOffGuide, a fully specified coding handoff, or a one-file implementation plan for a less capable model. Produces the guide rather than applying the proposed project changes."
---

# IdiotHandOffGuide

Turn the requested change into one execution-ready Markdown file. The author performs the investigation, design decisions, and code writing; the executor applies supplied edits and runs supplied checks. Optimize for fewer executor decisions and tool round trips, while retaining all information required for correctness. Completeness means executable detail, not a promise of flawless results.

## Deliverable and scope

Write `IdiotHandOffGuide.md` at the project root unless the user specifies another destination. If that file already exists, inspect it and update it only when it belongs to this task; otherwise use a task-specific filename. Produce one handoff artifact containing the requirements, implementation, commands, and checks. Include supporting code and scripts inside that file, not as separate deliverables.

During handoff authoring, read the project and write the handoff. Apply project changes only if the user separately requests execution. Distinguish checks actually performed on existing source from checks the executor must perform after applying the proposed code. The handoff must be usable without this conversation, the author's memory, or access to this skill.

## 1. Establish the actual starting point

Read applicable repository instructions, working-tree status, relevant source, callers, configuration, dependency manifests, and existing tests. Follow connected code far enough to resolve interfaces affected by the change. Batch independent reads and keep output focused on relevant symbols. For a new project, choose and state the smallest concrete structure that satisfies the request.

Record the repository root, branch and revision when available, relevant existing uncommitted changes, runtime, package manager, shell, and verified commands. Record paths relative to the repository root. If there is no repository, state that explicitly. Existing uncommitted work is part of the observed baseline and must be preserved.

Resolve library APIs against installed versions or authoritative documentation when necessary. Cite the particular fact used and its source in the handoff; include the actual implementation so the executor need not research the source again.

Separate observed facts, chosen design decisions, and unresolved inputs. Choose ordinary implementation details yourself. Ask for missing information only when it materially changes correctness or scope and cannot be established from available context. If required source, credentials, or decisions remain unavailable, mark the handoff BLOCKED, identify the exact missing input, and specify which steps depend on it. Write the independent portions fully. Never invent existing file contents, APIs, or successful checks to make a guide appear ready.

## 2. Solve the implementation before writing instructions

Map every requested behavior to a concrete code change and an observable check. Resolve the affected interfaces before drafting patches: names, types, signatures, imports, exports, call sites, persistence, configuration, and error handling. Include these details only where the task needs them.

Choose one implementation. Translate phrases such as "wire it up", "handle errors", "add validation", or "update related files" into named files, complete code, and specific behavior. Specify inputs, outputs, defaults, and boundary cases that affect this change. For UI work, specify relevant layout, text, states, interactions, and responsive behavior; for data changes, specify schema, compatibility, and migration order.

Keep the scope tied to the user's request. Reuse the project's conventions and dependencies where they fit. Supply full implementations of all new helpers and all required integration changes. For generated files or binaries, supply exact generation or acquisition instructions, versions and output paths, plus an observable validity check. A required asset with no available source is a blocker, not a request for the executor to improvise.

## 3. Write the single handoff file

Use the following sections, populated with task-specific content. A small task may have short sections; completeness is measured by covered decisions, not length.

### A. Execution contract

State the requested outcome, scope, root directory, shell, baseline, and readiness: READY or BLOCKED. READY means sufficiently specified for execution, not tested or guaranteed correct. List any required values by their exact variable names and how the executor obtains them; reference secret storage without including secret values.

Give the executor this operational sequence in task-specific terms:

1. Check the stated baseline and required inputs before editing.
2. Apply the numbered steps in order, using the supplied code exactly.
3. Run the specified verification commands and compare results to their expected outcomes.
4. Report changed files, actual check results, and unresolved blockers.

For an absent or mismatched edit target, instruct the executor to stop the dependent steps and report the path and mismatch. For a partially applied handoff, identify already-applied steps by their postconditions, verify them, and resume at the first unapplied step. An unfamiliar failure requires the exact error and failing step to be reported; include a repair branch only when its trigger and repair are known. Carry forward any authorization requirements for deployment or other external actions rather than treating the guide itself as permission.

### B. Requirements and acceptance map

Assign short requirement IDs. For each, state the externally observable behavior, implementing step IDs, and verification IDs. Include user constraints and relevant regression expectations. Explicitly separate deferred or blocked requirements from completed coverage.

### C. File-change manifest

List every created, modified, deleted, renamed, or generated file, its exact path, its operation, and its implementing step. Include relevant tests, configuration, dependency manifests, lockfiles, and migrations. Explain a deletion or rename and list affected references. Generated outputs may be a precise output directory/pattern when individual filenames are inherently tool-generated.

### D. Ordered implementation steps

Each step has a stable ID, prerequisites, exact target path, action, implementation payload, and a postcondition. Put dependencies before consumers and migrations in their required order. For each edit choose one unambiguous format:

- **Create:** complete file contents, including imports and exports. State that the target must not already exist, except when its contents match a previously applied step.
- **Replace entire file:** complete final contents, used for small files when their observed contents are fully accounted for. Record a reliable baseline check such as the exact original content or a verified checksum with its calculation command.
- **Replace block:** provide the exact original block and the complete replacement block. Require exactly one match. Include enough surrounding context to make it unique. If edits touch the same file repeatedly, anchors must match the intermediate state at that step.
- **Insert:** give an exact unique anchor, whether insertion is before or after it, and the complete inserted text.
- **Delete or rename:** give exact source/destination paths, baseline checks, and all resulting reference changes.

Use fenced code blocks with the appropriate language. Each implementation payload appears once; refer to step IDs elsewhere. Include all code needed for the change. Omission markers, pseudocode, and instructions to invent code are not implementation payloads. Literal ellipses or TODOs that are required source-language syntax or preserved existing content may remain; they must not stand for omitted implementation. Unchanged parts of a large file need not be reproduced when an exact block edit preserves them mechanically.

For commands, specify the working directory, shell, exact command, preconditions, expected output or invariant, and what to do on failure. Prefer existing package scripts and the established package manager. Supply exact dependency changes and use the package manager to generate lockfiles; identify those outputs in the manifest. Define external side effects and any required authorization before the corresponding command.

### E. Verification and failure handling

Provide exact commands for applicable focused tests, type checks, linting, builds, or manual checks. Use the project's real scripts and test conventions. Include complete source for tests that must be added. Select checks that demonstrate the requested behavior and plausible regressions; for a small low-impact edit, a precise inspection or manual check can suffice.

For each check, specify setup, action/input, expected result, and the requirement it proves. Cover the relevant success and failure behavior, not only compilation. State stable pass conditions rather than guessing timestamps, durations, or complete console output. Separate pre-existing failures from change-related failures when evidence permits. If a check cannot run, state the missing prerequisite and retain it as outstanding.

For risky multi-step operations, give concrete recovery steps scoped to the changes in this handoff. Preserve unrelated work; describe any irreversible step and its prerequisite before execution.

### F. Completion report contract

Tell the executor to report applied step IDs, changed files, checks actually run and their results, and any skipped checks or blockers. Define completion as all required steps and acceptance checks passing, or explicitly report incomplete work. Include the author's own validation status separately so proposed code is not mistaken for code already executed.

## 4. Audit the guide before delivery

Read the finished handoff as the executor, following the intermediate state after each step:

- Trace each requirement through the manifest, code payloads, and verification. Fill uncovered requirements or mark their specific blocker.
- Trace every new symbol to its definition, import/export, and caller. Check paths, types, configuration keys, dependency versions, and test fixtures agree.
- Check replacement anchors against observed source, and later anchors against earlier planned edits. Ensure full-file replacements preserve relevant existing behavior and uncommitted work.
- Check each command for the stated shell and working directory. Identify generated artifacts and external side effects.
- Find every place the executor would need to make a design choice, locate an unspecified file, supply missing code, or guess a pass condition. Resolve it with concrete instructions or mark it blocked.
- Check the file contains all required payloads and closes every code fence. If a tool or response limit interrupts writing, continue into the same artifact and verify its end before delivery. Never replace unfinished content with a summary and call it complete.

Keep explanations brief and remove repeated code, duplicated requirements, and unrelated background. Reduce tokens through precise edits and shared references inside the file, not by omitting decisions or code. Report the file location, readiness, and actual validation performed. Do not claim runtime correctness from a written-plan review alone.
