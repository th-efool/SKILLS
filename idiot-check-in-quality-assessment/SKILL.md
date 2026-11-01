---
name: idiot-check-in-quality-assessment
description: "Audit a completed or in-progress task, feature, workflow, site, or codebase and write one evidence-backed quality assessment file. Use when the user requests IdiotCheckInQualityAssessment or a comprehensive check for incomplete implementation, symptom-only fixes, bugs and regressions, quality gaps, dead code, duplication, and overengineering. Reviews and reports; does not apply fixes unless separately requested."
---

# IdiotCheckInQualityAssessment

Investigate the requested scope systematically and write every substantiated finding into one Markdown report. Follow implementation through its real callers, state transitions, dependencies, and user-visible results. The purpose is to establish what works, what remains incomplete, and what needs correction, including defects hidden behind superficially successful changes.

Exhaustive means accounting for every inventoried requirement and component in scope. It does not mean claiming to have proved that no undiscovered defects exist. Track uninspected areas and unavailable checks explicitly, and keep working until the coverage inventory has no unexplained gaps.

## Output and mutation boundary

Default report: `IdiotCheckInQualityAssessment.md` in the project root. Use the user's requested location when provided. Inspect an existing report before updating it; preserve unrelated reports by choosing a task-specific filename. Put the full assessment, coverage, evidence, and prioritized findings in this one file. Reference existing source and test artifacts rather than creating a collection of planning documents.

Audit and write the report. Apply fixes only when separately requested. Use existing checks and non-destructive observations. Run temporary reproductions, generated output, or test data in an isolated temporary location when possible; do not commit new test files or modify project configuration just to perform the audit. Before a command, determine whether it writes files, migrates a database, calls external services, or changes live data. Use a local or isolated test target for state-changing checks; obtain missing authorization for external mutations. Credentials and secret values belong outside the report.

## 1. Establish scope and expected behavior

Read applicable project instructions and the user's requested scope. Accept a task, feature, workflow, set of changes, or entire site/repository. For a feature audit, follow its dependencies and affected consumers beyond the diff, but distinguish unrelated pre-existing findings. For an entire-site audit, inventory all discoverable routes and user flows rather than treating the landing page as the whole product.

Read available requirements, acceptance criteria, designs, implementation guides, manager ledgers, issue context, and relevant documentation. These describe intended behavior; completion labels are claims to verify. Use connected artifacts when available. Ask only when an ambiguity prevents determining the required outcome. Otherwise state a concrete scope interpretation and proceed.

Record revision/branch when available, working-tree state, existing uncommitted edits, runtime/dependency versions relevant to the audit, and comparison baseline. Establish what changed using the actual diff and history when available. If no reliable before-state exists, label regression attribution unknown instead of inventing one. If auditing only a deployed site without source, state the limits on root-cause, dead-code, and duplication assessment.

Create a requirement inventory with stable IDs and observable success conditions. Separate explicit requirements from reasonable inferred expectations. Document the basis of any quality standard: project rules, supplied design, established behavior, accessibility criteria, performance target, or correctness requirement. A personal style preference is not a failed standard.

## 2. Build and complete a coverage map

Enumerate the actual scope before choosing review depth. Depending on the task, include routes/screens, components, public functions, handlers, services, storage/schema, jobs, integrations, configuration, assets, tests, build/deployment entry points, and their relationships. Exclude vendor/generated content from line-by-line review when appropriate, but inspect its generation, configuration, and use when relevant.

For every in-scope entry record:

- Requirement IDs and source locations or runtime entry point.
- Inputs, outputs, callers, dependencies, and state transitions.
- Review performed: source, runtime, tests, design comparison, or other evidence.
- Result: verified, finding, unverified, or not applicable with reason.
- Finding IDs or the exact remaining coverage gap.

Follow entry point -> validation -> authorization where relevant -> business logic -> persistence/integration -> response/UI state. Follow failure and recovery paths as well as success. For changed code, inspect the surrounding implementation and affected consumers. For claimed fixes, inspect the original trigger and the mechanism that should eliminate it.

Use searches to discover candidates, then inspect context. A TODO search, unused-symbol warning, lint pass, green test suite, or a screenshot is one source of evidence, not a complete audit. Continue until all inventoried entries have an explicit disposition. If scope is large, work in batches and checkpoint into the same report; report remaining gaps instead of silently sampling and declaring completion.

## 3. Inspect all six finding categories

### A. Pending or half-finished implementation

Trace each requirement to actual implementation and a usable end-to-end path. Check for missing integration, unregistered routes, disconnected handlers, placeholder data, partial migrations, absent configuration, flags that permanently hide intended behavior, tests that were never connected to the runner, and UI controls that appear functional but do not complete their action.

Exercise required loading, empty, success, failure, and recovery states where applicable. Distinguish intentionally deferred work from accidentally omitted work. A TODO alone does not prove incompleteness; tie the missing piece to required behavior. Record unfulfilled explicit requirements even if no code exists for them.

### B. Symptom-only fixes and unresolved root causes

Start with a concrete failing scenario or claimed fix. Trace the causal chain to the earliest incorrect assumption, state transition, data transformation, or boundary. Check whether the change eliminates that cause across affected paths or merely hides the visible failure.

Investigate broad exception swallowing, success fallbacks after failed writes, arbitrary delays/retries, forced refreshes, duplicated synchronization, weakened validation, and disabled assertions when they occur in relevant paths. These are investigation signals, not automatic findings. Demonstrate the condition under which the underlying defect survives. Test adjacent inputs, retries, alternate callers, or repeated execution when relevant. Mark a root cause confirmed only when evidence supports it; otherwise report the confirmed symptom and separately label the causal hypothesis.

### C. Existing defects, breakage, and regressions

Check interface compatibility, call sites, imports/exports, data shapes, schema changes, configuration, and deployment assumptions. Inspect applicable boundary inputs, null/empty states, error propagation, cancellation, races, stale state, duplicate submission, idempotency, resource cleanup, and failure recovery.

Trace security-sensitive behavior when the scope reaches it: authorization boundaries, input handling, secret exposure, and data isolation. Verify the relevant behavior without testing real users' data or performing destructive probes.

Reproduce failures using focused existing tests, isolated scripts, or actual UI interaction. Compare with the baseline where feasible. Label each issue introduced, pre-existing, or attribution unknown; all relevant issues belong in the report, even if the current change did not create them. Separate deterministic defects, intermittent evidence, and unverified suspicions.

### D. Quality-standard gaps

Compare implementation with the recorded standards. For interfaces, inspect rendered pages and interactions at relevant viewport sizes; check keyboard operation, focus, names/labels, content hierarchy, readability, overflow, feedback, and required visual states. Use real assets and representative data when available. Record browser, viewport, route, and state for visual evidence.

For workflows and services, inspect observability, useful error responses, consistency, maintainability, and performance only to the degree the scope and requirements warrant. Measure claimed performance failures under stated conditions or identify the unmeasured risk explicitly. A functional pass does not establish visual quality, accessibility, or acceptable performance. If runtime access is unavailable, label those dimensions unverified rather than inferring them from source.

### E. Dead code and unused artifacts

Investigate unreachable branches, unused modules/exports, abandoned feature paths, stale styles/assets/configuration, and obsolete compatibility layers. Check all relevant reference mechanisms before recommending removal: direct imports, dynamic imports, framework routing and file conventions, reflection, configuration, scripts, generated consumers, and external/public APIs.

State the candidate, reference searches performed, execution/configuration context, and evidence that it is unused. A symbol with no local textual references may be a public entry point. Keep uncertain candidates in the investigation queue rather than describing their deletion as safe. Preserve legitimate side-effect imports and intentionally retained compatibility behavior.

### F. Duplication and overengineering

Find repeated behavior with the same responsibility, divergent copies of validation/business rules, needless wrapper layers, abstractions with no useful variation, redundant state, and complexity that materially obscures or destabilizes the feature.

Explain the concrete cost: inconsistent behavior, extra state transitions, unnecessary runtime work, difficult testing, or avoidable maintenance. Give a smaller design that preserves required semantics and public contracts. Similar-looking code with different responsibilities may appropriately remain separate; a one-use abstraction may enforce a valuable boundary. Ground findings in actual costs rather than line count, number of files, or stylistic dislike. Do not prescribe a broad rewrite when a narrow simplification resolves the problem.

## 4. Validate findings and close coverage gaps

For every candidate, inspect the complete relevant function/module and its connected callers, then seek evidence that could disprove the finding: an upstream guard, an intentional contract, a framework convention, an existing fallback, or a test covering the disputed condition. Retain only findings whose explanation survives that check.

Use focused checks first, then required integration/build checks appropriate to the scope. Record exact command, working directory, setup, input/action, exit/result, and relevant observed output. Identify what each result proves and what it leaves untested. Do not mark a test passed if it was skipped, unavailable, or only proposed.

For static findings, give a precise reachable input and control/data-flow explanation sufficient to establish the defect. For runtime findings, give reproducible steps and expected versus actual behavior. Keep hypotheses and blocked checks in a separate investigation queue. Merge duplicate manifestations under their shared cause while listing all affected locations and requirements; keep distinct causes separate even if their symptoms look similar.

If files change during the audit, identify affected coverage and recheck it against the final state. Record the assessed revision and working-tree state so evidence is not silently attributed to a newer implementation.

## 5. Write the complete assessment file

Use these sections, with all applicable content filled in:

1. **Verdict and assessed scope:** what was audited, baseline, standards used, and whether acceptance is met, unmet, or undetermined. Keep implementation acceptance separate from lower-severity cleanup recommendations. State coverage limits prominently.
2. **Requirement and component coverage:** the completed inventories, disposition, evidence/check IDs, and outstanding gaps. Account for all six categories, including explicit reasons where a category is not applicable.
3. **Prioritized findings:** every substantiated finding, not only the top few. Sort by severity and group related causes. Include the fields below.
4. **Checks and evidence:** actual source inspections, searches, runtime exercises, tests, commands, results, and relevant limitations. Distinguish passed, failed, skipped, and unavailable checks.
5. **Unverified risks and blocked investigation:** exact missing information/access, why it matters, the next concrete check, and affected requirements. These are not confirmed defects.
6. **Correction order and completion criteria:** dependencies among fixes, the smallest suitable correction for each cause, and the regression check that would establish resolution. This is a remediation roadmap; full implementation payloads can be produced later by IdiotHandOffGuide when requested.

Each finding includes:

- Stable ID, category tags, concise title, and severity.
- Requirement/standard affected and user-visible or maintenance impact.
- Exact file path and verified line numbers, or route/endpoint/state when source is unavailable.
- Trigger/preconditions and expected versus actual behavior.
- Evidence, reproduction or static proof, and relevant check IDs.
- Confirmed root cause or explicitly qualified causal uncertainty.
- Attribution: introduced, pre-existing, or unknown.
- Minimal correction direction, affected integration points, and verification needed to close it.

Use severity consistently: **critical** for demonstrated catastrophic exposure/loss or total failure; **high** for core required behavior failing or a serious reachable risk; **medium** for limited functional/quality failures or meaningful maintenance cost; **low** for minor demonstrated issues. State the conditions that justify severity. Do not elevate speculative risk to a confirmed critical issue.

## 6. Finish only with an honest coverage accounting

Before delivery, reconcile every requirement, inventory entry, candidate finding, and required check. Ensure every finding has evidence and every gap has a reason and a concrete next step. Include all confirmed issues even when the list is long; continue writing the same report across tool limits instead of replacing the remainder with a summary.

A clean result means no substantiated findings within the coverage actually performed. It does not erase unavailable checks or establish perfection. When blockers prevent assessment, use an undetermined verdict for the affected requirements and identify what remains necessary.

Return the report link, overall verdict, severity counts, and material coverage limitations. Keep the full findings in the report; do not fix or silently delete code during the assessment.
