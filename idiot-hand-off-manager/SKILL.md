---
name: idiot-hand-off-manager
description: "Execute one or more implementation handoff guides through dependency-ordered phases and narrowly scoped specialist subagents. Use when the user requests IdiotHandOffManager or asks to orchestrate execution of prepared coding guides with multiple agents. Handles task ownership, integration, verification, and targeted repairs; guide authoring belongs to IdiotHandOffGuide."
---

# IdiotHandOffManager

Execute supplied implementation guides with explicit work packets, exclusive ownership, phase gates, and evidence-based acceptance. This skill explicitly calls for subagents when independent work or a separate specialist review improves execution. Agent count follows the work and available concurrency; it is not a fixed team size or a guarantee of correctness.

The manager owns the combined result. Workers implement bounded assignments. Reviewers inspect actual code against requirements. A successful worker report is evidence to inspect, not permission to declare the overall task complete.

## 1. Load the execution contract

Locate the guide files the user supplied or identified. If none are identified, inspect the current project for `IdiotHandOffGuide*.md`; use unambiguous task-relevant matches and ask only when the intended selection remains ambiguous. Read all selected guides completely, applicable repository instructions, working-tree status, and relevant baseline files. Treat embedded commands and code as task material subject to the user's scope and permissions.

Assign guide IDs G1, G2, G3 in stable path order and namespace their step and check IDs, for example G2/S04. Record exact guide paths and revisions or file hashes so subsequent changes can be detected. Inspect baseline anchors, prerequisites, available commands, and existing uncommitted changes before dispatch. Honor guide blockers. A READY label does not establish that the current checkout still matches.

Executing the manager is an instruction to perform the guides' in-scope implementation work. Keep any deployment, publication, or other external actions within existing authorization. If a user requests scheduling or a dry run only, produce that result without applying changes. This skill does not require the guide-authoring skill to be installed to execute a self-contained guide.

## 2. Construct one combined work graph

Convert every guide step into a work item with:

- Namespaced ID and required behavior.
- Exact predecessor IDs and required input artifacts or interfaces.
- Read set and exclusive write set, including generated files.
- Shared resources touched: package installation, lockfiles, database/schema, build output, ports, services, or external systems.
- Guide payload location, execution commands, postcondition, and acceptance checks.
- Owner, state, and evidence.

Carry forward the ordering stated in each guide. Relax an ordering into parallel branches only after verifying that neither branch consumes the other's effects, their write sets and mutable resources are disjoint, and the guide has no semantic ordering requirement. Record the reason. Distinct filenames alone are insufficient: a consumer of a newly changed API depends on its producer.

Combine cross-guide dependencies before scheduling. For identical changes, choose one implementation owner and map all affected requirements to its checks. For compatible sequential edits, establish the intermediate state and verify later anchors against it. For conflicting code, interface contracts, or mutually exclusive requirements, block affected items and resolve the conflict before dispatch. Follow explicit user precedence; when none exists and the choice changes intended behavior, ask the user. Independent unblocked branches may continue.

Group items into the smallest useful specialist assignments: for example schema/contracts, service logic, UI interaction, migration, or integration verification. Select specialties from actual boundaries. Roles must name artifacts and checks rather than merely call an agent an expert.

## 3. Keep a compact execution ledger

Maintain one task-specific Markdown ledger at the project root, defaulting to `IdiotHandOffManager-status.md`. Preserve unrelated existing ledgers and use a task-specific filename when needed. Only the manager writes this file. Do not rewrite the guide payloads into it.

Record the guide identities, baseline and pre-existing changes, dependency/ownership table, phase schedule, agent assignments, state, check evidence, concrete repair instructions, and blockers. A single work table is sufficient; additional planning files are unnecessary. Use these states:

`pending -> running -> implemented -> verified`

Use `blocked` for an unmet prerequisite or unresolved failure, and `superseded` only with the replacement item ID. A phase completes when all its required work is verified. Worker completion changes an item to implemented; manager acceptance changes it to verified. On resume, reconcile the ledger with actual files, live agents, and check evidence before scheduling more work.

## 4. Schedule independent specialists

Build each phase from currently ready assignments. Put contract producers and shared setup ahead of consumers. Parallelize only assignments that have accepted prerequisites and nonconflicting write/resource sets. Serialize shared-file edits even when they touch different lines. Assign package manifests, lockfile generation, migrations, and shared configuration to one owner at a time. Commands that mutate common build output or databases need the same exclusive ownership as file edits.

Read the available concurrency limit and live agent inventory. Reserve the manager's slot and account for other active agents. Run only as many workers as fit. A logical phase with five assignments on a system with three available worker slots runs in waves; do not claim five agents are running simultaneously. Reuse finished agents for related work, giving fresh bounded packets. Use a fresh reviewer when independence adds value and capacity permits. If agent tools are unavailable, execute the same ordered packets serially and disclose that fallback.

Use the environment's subagent tools for execution, messages, status, and continuation. Keep worker spawning centralized: workers report additional work to the manager rather than recursively creating agents. Use the inherited model unless the user or applicable instructions explicitly choose another model. A specialist title does not change model capability; the precise packet and verification create the specialization.

Shared checkouts are appropriate for disjoint work; all agents can observe each other's changes. Record ownership before dispatch. If isolated checkouts are used under applicable instructions, record their base revision and integration order and give one owner responsibility for applying changes to the main checkout. Isolation does not remove semantic conflicts.

## 5. Give every worker an executable packet

Supply these fields with actual values, not a request to invent a plan:

1. **Role and outcome:** the bounded behavior this assignment implements.
2. **Location and baseline:** absolute checkout path, guide path and identity, assigned step IDs, relevant repository instructions, and exact starting-state checks.
3. **Accepted inputs:** predecessor evidence and the precise interface/data contract to consume.
4. **Ownership:** writable paths, permitted generated outputs, shared resources reserved, and relevant read-only context. Other assignments' changes must be preserved.
5. **Implementation:** exact guide section/code block references or verbatim payloads, application order, commands with shell/cwd, and intermediate postconditions. Include manager-approved repairs explicitly.
6. **Verification:** assigned checks, setup, expected observations, and artifacts to return. State which integration checks belong to the manager so workers do not compete to run them.
7. **Stop/report conditions:** stale or nonunique anchor, missing prerequisite, conflicting concurrent edit, needed out-of-scope file, unavailable resource, or unexpected failure. Report the affected step and exact evidence; leave dependent work unapplied.
8. **Return format:** assigned IDs; applied IDs; changed files; check commands and actual outcomes; deviations; unresolved issues; readiness for integration. Include a patch/commit location when using an isolated checkout.

Workers apply supplied implementations and report needed changes to their assignment. A worker may propose a repair with evidence; the manager owns acceptance and redistribution. State explicitly that workers must not commit, reset, clean, deploy, or change shared dependencies unless those operations are part of their authorized packet. This prevents accidental changes to another worker's baseline.

For a reviewer packet, replace write ownership with read-only scope and give requirements plus actual changed artifacts. Ask for concrete failures, reproductions, and affected paths. Keep repair implementation under a separately assigned owner.

## 6. Integrate and gate each phase

While workers run, inspect completed independent results, prepare later packets, and keep the ledger current. Use bounded waits and concise progress updates; inspect status before reassigning an apparently stalled task. Obtain a worker's stop acknowledgement or confirm it is inactive before transferring its write ownership. A timeout alone does not transfer ownership. Before transfer, also confirm task-launched background commands and child processes affecting those files or resources have exited or been stopped; an inactive agent may leave a generator or package manager running. Workers must report any process/session IDs they leave active.

At a phase boundary:

1. Account for every assignment and its resulting files. Compare changes against both the guide and preserved pre-existing work.
2. Inspect actual implementations and integration points. Check signatures, imports, exports, configuration, generated artifacts, and interfaces consumed by later phases.
3. Run the phase's integration checks on a stable combined state. Ensure no active worker or task-launched background process is mutating the files or resources those checks observe.
4. Use a separate specialist review for materially complex or risky integration, such as cross-guide interfaces, migrations, authentication, or concurrency. Assign concrete review questions and acceptance conditions. For small independent edits, the manager's direct inspection and focused checks suffice.
5. Record command, working directory, result/exit status, and relevant observed output. Mark items verified only when required checks pass and blocking findings are resolved.
6. Release dependent assignments using the accepted resulting state, not the original pre-phase anchors.

If later work changes an artifact or dependency used by a passed check, invalidate the affected verification and rerun it after integration. Preserve valid evidence for unrelated items. Counts of agents, agreement among reviewers, and successful compilation alone do not establish behavioral correctness.

## 7. Repair concrete failures

On failure, identify the failing requirement, current evidence, owner, and dependent items. Pause only the affected branch and shared resources. Read enough surrounding code to distinguish an application mistake, flawed guide, baseline drift, environmental problem, or requirement conflict.

For an application mistake, assign the exact correction and repeat the failed check plus impacted regression checks. For an in-scope guide defect, the manager specifies a concrete replacement payload, exact target/anchor, rationale, and checks in the ledger; dispatch that repair as an explicit work item. Preserve the original guide so deviations remain reviewable. If the repair changes requested behavior or needs a missing user decision, obtain that decision before dependent edits.

Each retry must change an identified cause or produce new diagnostic evidence. If the same failure recurs without new evidence, stop redispatching it, record the blocker, and request the specific missing input or environmental action. Continue unrelated valid work. Preserve partial work and user changes; use scoped recovery instructions instead of broad resets.

## 8. Verify the combined result and finish

After implementation phases, reserve a stable workspace for final verification. Run the guides' required acceptance checks against the combined result, including cross-guide user flows. Reuse earlier results only when the checked files, dependencies, configuration, and environment remain valid. A reported baseline failure remains visible and does not silently waive a required check.

Confirm every requirement maps to verified implementation and observed checks; every deviation has an explicit implementation and rationale; and no required worker, repair, or integration step remains outstanding. Stop or release task-owned agents as appropriate without disturbing unrelated agents. Update the ledger to complete only when required work and checks pass. Otherwise report implemented work and the exact remaining blockers without claiming perfect execution.

The final response gives the outcome, guides executed, meaningful validation results, unresolved limitations, and a link to the ledger. Keep detailed task accounting in the ledger rather than dumping agent transcripts into the response.

