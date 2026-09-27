# TENTOR HOS V.2 — Evidence Record and Maturity Taxonomy v0.1

**Date:** 2026-09-27  
**Gate:** S00-05 / CR-06 and CR-03  
**Status:** WORKING MODEL / NOT CANONICAL / NOT ACCEPTED

## 1. Purpose and non-equivalence rule

This document proposes a cross-project evidence vocabulary for analysis and future specification. It does not replace source-project evidence schemas, nor assert that any source project implements this model. Preserve source-native records and map them through explicit, loss-aware adapters. Never infer stronger evidence maturity from a document label, repeated assertion, file location, or presence in a repository.

## 2. Evidence record fields — candidate schema

| Field | Required? | Meaning / validation |
|---|---|---|
| evidence_id | Yes | Stable unique identifier within the evidence registry; immutable once referenced. |
| subject_id | Yes | Exact requirement, claim, artifact, component, execution, or gate being evidenced. |
| claim | Yes | Atomic proposition supported or challenged; avoid bundled claims. |
| evidence_class | Yes | One controlled class from section 3, or a source-native class mapped with a documented adapter. |
| source_artifact | Yes | URI/path plus repository/source identity; include version/ref and blob/hash where available. |
| provenance | Yes | Capture method, source owner/system, transfer chain, and known provenance gaps. Unknown is explicit, not omitted silently. |
| context | Yes | Environment, configuration, domain, tenant/account (non-sensitive reference), dependencies, and relevant versions. |
| method | Yes | Inspection, static analysis, deterministic test, CI, runtime test, external provider operation, review, or other named method. |
| scope | Yes | Exact requirement clauses, components, environments, cases, and exclusions covered. |
| observed_at | Yes | Timestamp with timezone or explicit unknown; separate from document authored/modified date. |
| evaluator | Yes | Actor/system/tool performing evaluation and role; distinguish author from independent reviewer. |
| result | Yes | PASS, FAIL, BLOCKED, PARTIAL, INCONCLUSIVE, or NOT_RUN, with defined semantics and no implied overall project status. |
| artifacts | Conditional | Logs, outputs, screenshots, recordings, test reports, job IDs, hashes, and durable links needed to reproduce/inspect the claim. |
| limitations | Yes | Known missing context, sampling, unverified claims, nondeterminism, and scope exclusions. Use “none identified in stated scope” only after review. |
| independence | Yes | NONE, AUTHOR_SELF_REVIEW, SAME_SYSTEM_REPLAY, SEPARATE_REVIEWER, or INDEPENDENT_EXTERNAL, with basis. |
| supersedes / derived_from | Conditional | Explicit links to earlier or source evidence; identify derivative/companion/copy relationships. |
| decision_ref | Conditional | Explicit approval/promotion decision and authority; evidence itself does not confer approval. |
| integrity | Conditional | Hash algorithm/value and capture method; bundle integrity is distinct from original-source authenticity. |

## 3. Evidence classes (orthogonal to result)

Evidence class answers “what kind of thing is this?”, not “did it pass?”

- **SOURCE_DECLARATION** — statement in a specification, README, report, issue, or owner assertion.
- **ARCHIVED_ARTIFACT** — preserved source file or repository snapshot; integrity and provenance must be separately stated.
- **DESIGN_REVIEW** — reasoned review of a design or specification; not runtime execution.
- **TEST_PLAN** — test definition, checklist, or suite inventory; not a run.
- **TEST_EXECUTION** — recorded execution with inputs, environment, outputs, and result.
- **CI_EXECUTION** — test/build execution tied to identifiable repository ref and CI run.
- **RUNTIME_OBSERVATION** — behavior observed in a named running system/environment.
- **EXTERNAL_PROVIDER_ARTIFACT** — output from a provider/external service; does not alone prove integration through target runtime.
- **INDEPENDENT_REVIEW** — review by a reviewer independent of the author/implementer for the stated scope; independence basis required.
- **PRODUCTION_OPERATION** — bounded production observation with context, monitoring, and incident/rollback context.
- **INFERENCE** — analytical conclusion derived from other evidence; links all premises and states uncertainty.
- **UNKNOWN_OR_MISSING** — source, method, or artifact unavailable; cannot be upgraded by assumption.

## 4. Result semantics (separate axis)

| Result | Candidate meaning |
|---|---|
| PASS | All declared acceptance criteria passed within explicitly stated scope and method. Not a global project PASS. |
| FAIL | One or more acceptance criteria failed with attributable evidence. |
| BLOCKED | Evaluation could not proceed because a declared prerequisite, permission, capability, or dependency was absent. |
| PARTIAL | Some criteria or cases passed and others remain untested/failed; enumerate both. |
| INCONCLUSIVE | Evidence is conflicting, insufficient, or method cannot decide the criterion. |
| NOT_RUN | No execution was performed. A test plan may exist. |

A result must never be inferred from evidence class. Example: TEST_PLAN + no run = NOT_RUN, not PASS. SOURCE_DECLARATION saying PASS remains a source claim until execution evidence is independently established.

## 5. Maturity / assurance states (candidate ordered gates, not a score)

Maturity is a gate state attached to a specific claim and scope; it is not a universal ranking of project quality.

1. **Captured** — artifact preserved and capture details recorded.
2. **Provenance-checked** — source identity and transfer/integrity claims checked to the stated level; original-source authenticity may still be unknown.
3. **Content-reviewed** — relevant content inspected with scope and reviewer recorded.
4. **Criteria-defined** — explicit acceptance criteria and test/evaluation method exist.
5. **Executed** — applicable tests/observations were run and evidence retained.
6. **Conformance-reviewed** — result and evidence checked against criteria by a named reviewer.
7. **Independently-verified** — separate reviewer/method meets declared independence conditions.
8. **Accepted-for-scope** — authorized decision-maker explicitly accepts claim for bounded scope and version.
9. **Production-observed** — bounded production behavior observed; does not guarantee future operation.

States are not automatically monotonic: changed code, context, provider, policy, or requirement can invalidate prior maturity and require re-evaluation. “Accepted-for-scope” is a governance decision, not an evidence class or substitute for execution.

## 6. Required integrity and anti-inflation checks

- No PASS without linked acceptance criteria and evidence supporting each criterion.
- No independent label without reviewer identity/role and independence rationale.
- No CI claim without repository/ref and run identity.
- No runtime claim without environment/context and reproducible observation details.
- No system integration claim from an external provider artifact alone.
- No cross-domain generalization from repeated derivative documents alone.
- No promotion from source-declared LOCKED/PASS to accepted-for-scope without an explicit decision record.
- No missing provenance silently treated as verified.
- Conflicting evidence is retained and resolved by explicit decision; never overwritten by a newer summary.
- Evidence records must identify supersession and derivation rather than double-counting copies.

## 7. Mapping existing baseline

The current TH-EV registry is an intake/evidence index, not yet a fully populated instance of this candidate schema. Batch review references establish content-review records, not independent verification. Existing source-reported statuses remain attributed to their original source documents. TH-EV-017 remains a specific example: bundle-level checksum match does not establish original Library provenance.

## 8. Open design questions

- EV-01: stable IDs and namespace policy across repos/workspaces.
- EV-02: machine-readable schema format and schema evolution compatibility.
- EV-03: evaluator identity/privacy and retention constraints.
- EV-04: cryptographic signing and trusted timestamp requirements, if any.
- EV-05: independence criteria by claim risk/class.
- EV-06: revocation, invalidation, supersession, and re-evaluation lifecycle.
- EV-07: mapping source-native evidence and audit systems without losing semantics.
- EV-08: accepted result aggregation semantics; no aggregation rule is approved here.

## 9. Disposition

Working evidence model only. CR-06 and CR-03 remain OPEN until source-specific mapping, counterexamples, schema validation, aggregation semantics, governance authority, and explicit human acceptance are complete. No TENTOR HOS specification or implementation conformance is accepted.
