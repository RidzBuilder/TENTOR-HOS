# TENTOR HOS V.2 — Status & Evidence Promotion Taxonomy v0.1

**Date:** 2026-10-05  
**Gate:** S00-05 / CR-03 / CR-06  
**Status:** WORKING MODEL / NON-CANONICAL / NOT ACCEPTED

## 1. Purpose

This document defines a candidate lifecycle for the **status of a claim, requirement, design artifact, implementation artifact, verification result, or governance decision**.

It complements, and does not replace:

- `EVIDENCE_RECORD_AND_MATURITY_TAXONOMY_v0.1.md`
- `CANDIDATE_SCOPED_EVIDENCE_AGGREGATION_SEMANTICS_v0.1.md`
- source-native status vocabularies
- repository/CI/runtime records
- explicit governance decisions

The central distinction is:

> **Evidence maturity describes how strongly an evidentiary record has been established. Status promotion describes what lifecycle state a subject is authorized to occupy.**

Neither axis may be inferred from the other.

No state in this document is a canonical TENTOR HOS V.2 status until explicitly accepted through governance.

## 2. Non-negotiable status boundaries

1. A source-declared `PASS` or `LOCKED` is historical source evidence, not automatic TENTOR HOS acceptance.
2. A design artifact is not an implementation.
3. An implementation is not tested merely because code exists.
4. A successful test is not independent verification unless the independence conditions are met.
5. Independent verification is not production acceptance unless the acceptance authority explicitly decides so.
6. A provider artifact is not target-system E2E evidence by itself.
7. CI success is bounded to the repository/ref/workflow/run and does not prove production behavior.
8. Acceptance is a governance decision; evidence informs the decision but does not grant authority.
9. A status must always be scoped to subject, version/revision, environment/domain where applicable, and decision authority where applicable.
10. Missing provenance, unresolved conflict, stale evidence, or revoked evidence must not be silently promoted.

## 3. Two-axis model

### 3.1 Evidence / assurance axis

Retain the existing candidate maturity sequence:

`Captured → Provenance-checked → Content-reviewed → Criteria-defined → Executed → Conformance-reviewed → Independently-verified → Accepted-for-scope → Production-observed`

This remains the evidence/assurance model.

### 3.2 Subject lifecycle axis

Candidate lifecycle states:

| State | Meaning | Minimum basis | Does not imply |
|---|---|---|---|
| PROPOSAL | Candidate subject exists for consideration | Identifiable subject + stated intent/scope | approval, implementation, validity |
| SOURCE-DECLARED | State/assertion imported from a source project or owner | Traceable source declaration + provenance status | current TENTOR HOS conformance |
| APPROVED-DESIGN | Design/requirement is explicitly approved for implementation in a bounded scope | criteria/scope + explicit authority decision + decision record | implementation or test success |
| IMPLEMENTED | Approved subject has a corresponding implementation at a named revision | approved design + implementation identity + traceable revision | correctness or acceptance |
| TESTED | Applicable implementation/behavior has been executed against declared criteria | implementation identity + executable criteria + execution evidence | independent verification |
| INDEPENDENTLY-VERIFIED | Qualifying independent review/verification confirms the declared scope | TESTED evidence + independence basis + review result | production acceptance |
| ACCEPTED-FOR-SCOPE | Authorized decision-maker accepts the subject for explicit scope/version | qualifying evidence + decision authority + explicit decision record | universal validity or perpetual validity |
| PRODUCTION-ACCEPTED | Accepted subject has bounded production evidence and explicit production decision | ACCEPTED-FOR-SCOPE + production observation + production authority decision | future/regression guarantee |
| DEPRECATED | Subject remains historical but is no longer approved for new use | explicit deprecation decision + replacement/impact information where applicable | deletion or invalidation of historical evidence |
| REJECTED | Governance decision refuses the subject for the declared scope | explicit rejection decision + rationale | evidence deletion |
| REVOKED | Previously promoted status is withdrawn for a defined reason/scope | revocation authority + trigger/evidence + affected scope | erasure of historical decision |

**Important:** `SOURCE-DECLARED` is intentionally not placed on the promotion ladder. It is an **imported provenance state**, not proof of TENTOR HOS lifecycle progression.

## 4. Promotion graph

Normal forward progression is candidate, not automatic:

`PROPOSAL → APPROVED-DESIGN → IMPLEMENTED → TESTED → INDEPENDENTLY-VERIFIED → ACCEPTED-FOR-SCOPE → PRODUCTION-ACCEPTED`

A subject may remain at an earlier state when later evidence is not applicable.

`SOURCE-DECLARED` may be attached as source provenance to any subject but cannot substitute for the missing transition evidence.

`DEPRECATED`, `REJECTED`, and `REVOKED` are governance outcomes and may terminate or suspend a previously promoted path.

## 5. Promotion contracts

### 5.1 PROPOSAL → APPROVED-DESIGN

Required:

- exact subject identity/version;
- bounded purpose and scope;
- acceptance criteria or design-review criteria;
- explicit approving authority;
- decision record;
- unresolved conflicts identified;
- known provenance limitations recorded.

Failure conditions:

- approval authority absent;
- scope ambiguous;
- material unresolved conflict hidden;
- proposal represented as implementation.

### 5.2 APPROVED-DESIGN → IMPLEMENTED

Required:

- approved design decision reference;
- implementation identity (repository/path/component/version or equivalent);
- implementation revision/commit;
- traceability from implementation to approved requirement/design;
- implementation boundary and exclusions.

Failure conditions:

- only a blueprint/spec exists;
- implementation revision cannot be identified;
- implementation diverges materially without an approved change;
- source artifact is merely copied/derived without implementation evidence.

### 5.3 IMPLEMENTED → TESTED

Required:

- executable test/evaluation criteria;
- implementation revision;
- test environment/configuration;
- execution identity/time;
- observed outputs/results;
- retained test evidence;
- failures and limitations recorded.

CI may satisfy this only within the exact scope represented by its run/ref/configuration.

### 5.4 TESTED → INDEPENDENTLY-VERIFIED

Required:

- qualifying test evidence;
- independent reviewer or independent verification mechanism;
- explicit independence basis;
- review scope;
- verification result;
- conflicts or exceptions recorded.

Self-review, same-author inspection, or replay by the same system does not automatically satisfy independence.

### 5.5 INDEPENDENTLY-VERIFIED → ACCEPTED-FOR-SCOPE

Required:

- verification evidence;
- explicit authorized decision;
- exact accepted scope/version;
- acceptance criteria satisfied or explicitly governed exception;
- residual risk/limitations;
- decision timestamp and authority.

Independent verification cannot silently become acceptance.

### 5.6 ACCEPTED-FOR-SCOPE → PRODUCTION-ACCEPTED

Required:

- explicit production scope;
- production observation evidence;
- production environment/revision;
- monitoring/operational context appropriate to the claim;
- explicit production acceptance authority;
- rollback/incident conditions where relevant.

Production observation alone does not confer production acceptance.

## 6. Demotion, invalidation, revocation, and rollback

Status is not permanently monotonic.

A previously promoted subject must be re-evaluated when any material basis changes, including:

- implementation revision;
- requirement or acceptance criteria;
- provider/tool/model;
- environment or configuration;
- authority/policy;
- evidence integrity/provenance;
- dependency;
- security/safety/compliance condition;
- discovery of a material defect;
- evidence revocation;
- unresolved contradiction.

Candidate transition rules:

- **INVALIDATED EVIDENCE:** preserve historical status; recompute current status.
- **FAILED RETEST:** current status may fall to TESTED-with-failure, or an earlier applicable lifecycle state, depending on policy; never preserve acceptance automatically.
- **REVOKED ACCEPTANCE:** preserve historical acceptance decision, mark it revoked for current use, identify affected downstream decisions, and trigger remediation/re-evaluation.
- **DEPRECATED:** no new promotion/use under the deprecated state unless an explicit reactivation/change decision exists.
- **REJECTED:** remains historical; may only re-enter consideration through a new proposal or explicit reconsideration process.
- **SUPERSEDED:** old subject remains historical and traceable; successor must independently satisfy its own promotion contract.

No demotion may erase the evidence or decision that caused the earlier state.

## 7. Required status record

Every promoted lifecycle state should have at least:

- `status_record_id`
- `subject_id`
- `subject_version/revision`
- `lifecycle_state`
- `scope`
- `evidence_refs[]`
- `criteria_refs[]`
- `provenance/integrity_state`
- `decision_ref` when governance is required
- `authority`
- `evaluator/reviewer`
- `independence_basis` when applicable
- `effective_at`
- `expires_at` or freshness policy when applicable
- `supersedes/derived_from`
- `limitations`
- `revocation/invalidation_ref` when applicable

A status record is not itself proof; its referenced evidence and decision records remain authoritative for their respective claims.

## 8. Anti-inflation rules

The following transformations are explicitly prohibited without additional evidence:

| Invalid shortcut | Required boundary |
|---|---|
| SOURCE-DECLARED PASS → ACCEPTED-FOR-SCOPE | Explicit acceptance decision + qualifying evidence |
| DESIGN → IMPLEMENTED | Implementation identity/revision |
| IMPLEMENTED → TESTED | Actual execution evidence |
| TESTED → INDEPENDENTLY-VERIFIED | Independent review/verification |
| INDEPENDENTLY-VERIFIED → PRODUCTION-ACCEPTED | Production evidence + production decision |
| Provider artifact → target E2E PASS | Target runtime/E2E evidence |
| CI PASS → production PASS | Production-specific evidence |
| Repeated copies → stronger evidence | Independent provenance/content basis |
| Newer summary → overwrite conflict | Explicit conflict resolution |
| Historical LOCKED → current canonical | Current governance decision |
| Accepted old revision → accepted new revision | Re-test/re-verification as required |

## 9. Relationship to aggregation semantics

The lifecycle taxonomy does not replace criterion-level aggregation.

A gate may aggregate evidence to a candidate result such as `PASS`, but a lifecycle promotion still requires the appropriate governance transition.

Therefore:

- `PASS` is a **result state**, not a lifecycle state.
- `ACCEPTED-FOR-SCOPE` is a **governance lifecycle state**, not an evidence class.
- `INDEPENDENTLY-VERIFIED` requires evidence maturity and independence conditions.
- `PRODUCTION-ACCEPTED` requires bounded production evidence and authority.

This prevents a single result token from being interpreted as a universal lifecycle promotion.

## 10. Conflict and uncertainty

If qualifying evidence materially conflicts and no approved adjudication rule resolves it:

- do not promote;
- preserve all conflicting evidence;
- mark the subject as conflict/inconclusive at the evidence/result layer;
- identify the remediation/adjudication action;
- require re-evaluation after resolution.

A missing record is not a PASS and is not silently converted into NOT_APPLICABLE.

## 11. Freshness and expiry

Freshness is requirement-specific and evidence-class-specific.

No universal time-to-live is declared here.

Until freshness policy is approved:

- record observed/effective time;
- identify the version/environment/provider;
- treat changed context as a trigger for impact analysis;
- do not assume that age alone invalidates evidence;
- do not assume that age alone preserves validity.

## 12. Source-project mapping rule

Historical source states from ACS, ACOS, ACPA, CCH-OS, EVO, LCH-OS, PBOS, or other inputs remain **source-native claims** unless and until TENTOR HOS governance explicitly promotes them.

For each imported claim, preserve:

1. original source wording/status;
2. source artifact and provenance;
3. scope/version;
4. mapped candidate lifecycle state, if any;
5. evidence supporting the mapping;
6. unresolved differences;
7. explicit decision if promoted.

No cross-project status inheritance is allowed by terminology similarity.

## 13. Falsification / adversarial checks

A future conformance harness should reject at least:

- source-declared PASS without execution evidence promoted to TESTED;
- design-only artifact promoted to IMPLEMENTED;
- CI PASS on revision A promoted to revision B;
- provider artifact promoted to target E2E acceptance;
- self-review labeled independent;
- accepted revision promoted automatically after implementation change;
- revoked evidence continuing to satisfy a mandatory criterion;
- unresolved conflict promoted to accepted;
- deprecated artifact promoted without reactivation decision;
- production observation represented as production acceptance without authority.

## 14. Open decisions

This candidate taxonomy does not resolve:

- authority model and role separation;
- exact independence thresholds by risk;
- evidence freshness policies;
- expiry/renewal mechanics;
- waiver/exception authority;
- status aggregation precedence;
- machine-readable schema and versioning;
- policy migration semantics;
- production acceptance requirements by domain;
- exact relationship to future TENTOR HOS architecture layers.

These require later governance and should not be invented during implementation.

## 15. Current disposition

**WORKING MODEL / NON-CANONICAL / NOT ACCEPTED.**

This artifact strengthens S00-05 reconciliation by making status promotion boundaries explicit. It does **not** change:

- CR-01: OPEN / partially resolved provenance;
- CR-02: PARTIALLY PROGRESSED;
- CR-03: OPEN;
- CR-04: OPEN;
- CR-05: OPEN;
- CR-06: OPEN;
- canonical requirements: 0 accepted;
- S00-06 Fundamental Specification: NOT STARTED;
- S00-07 Implementation: NOT STARTED;
- S00-08 U-AAFA: NOT STARTED / GATED.

Next action after governance review: reconcile this taxonomy against candidate requirement matrix, aggregation test vectors, and CR-03/CR-06 evidence before any canonicalization decision.
