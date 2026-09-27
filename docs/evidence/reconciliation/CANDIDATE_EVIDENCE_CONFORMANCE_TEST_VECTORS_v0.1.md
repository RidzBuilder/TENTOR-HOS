# Candidate Evidence Conformance Test Vectors v0.1

Status: WORKING DRAFT / NON-NORMATIVE / NOT ACCEPTED

## 1. Purpose and limits

This document turns the candidate Evidence Record and Maturity Taxonomy into explicit, falsifiable test vectors. It is a design artifact only. It does not establish a canonical TENTOR HOS evidence schema, authorize architecture promotion, or claim tests have been executed against a runtime implementation.

The implementation under test (IUT) is a future evidence validator and scoped status aggregator. Every vector is proposed; execution status is NOT_RUN unless a separate test-run record is attached.

## 2. Candidate validator contract

Given an evidence record and declared requirement/scope, the IUT should:
1. Validate required fields, types, enumerations, and internal consistency.
2. Preserve evidence class separately from result/status.
3. Validate source identity, artifact integrity, provenance, and scope without inferring missing facts.
4. Reject or quarantine stale, invalidated, revision-mismatched, duplicated-without-independent-value, or out-of-scope evidence.
5. Return disposition, reason codes, missing fields/evidence, and remediation.
6. Never promote a requirement to PASS solely because a source says PASS/LOCKED, a plan exists, an artifact is named, or a prior result passed another scope/revision.

## 3. Conventions

PASS_RECORD means structurally acceptable for the specific evidence claim, not that the requirement passes. REJECT means invalid as submitted. QUARANTINE means retain for review but do not use to satisfy a gate. ACCEPT_WITH_LIMITATION means usable only for the bounded claim. All vectors are synthetic, not actual project evidence.

## 4. Test vectors

| ID | Input condition | Expected disposition | Required behavior |
|---|---|---|---|
| EVCT-001 | Source declaration says runtime PASS, no execution record or artifact. | QUARANTINE | Class remains SOURCE_DECLARATION; cannot satisfy runtime gate. |
| EVCT-002 | Test plan has cases/outcomes but no run output. | ACCEPT_WITH_LIMITATION | TEST_PLAN supports planning only, not execution. |
| EVCT-003 | Test execution includes test ID, exact revision, environment, timestamp, command, raw output, result. | PASS_RECORD | Eligible for declared scope, subject to integrity and review. |
| EVCT-004 | Test references a different commit from target; no equivalence proof. | QUARANTINE | Rerun on target or provide governed equivalence proof. |
| EVCT-005 | Provider artifact exists without trace to job, input, provider, or requirement. | QUARANTINE | Artifact existence alone is not provenance or E2E. |
| EVCT-006 | Provider job and artifact linked, but playback, delivery, acceptance checks absent. | ACCEPT_WITH_LIMITATION | Supports provider-operation claim only; product E2E unproven. |
| EVCT-007 | Two records are byte-identical copies of one execution. | ACCEPT_WITH_LIMITATION | Preserve custody references; count one underlying event. |
| EVCT-008 | Two reviewers independently review same criterion and produce distinct records. | PASS_RECORD | Eligible as two reviews, subject to qualification/conflict policy. |
| EVCT-009 | Reviewer self-reviews own implementation but labels review independent. | REJECT | Remove independence claim; request qualified independent review. |
| EVCT-010 | Valid prior pass targets superseded revision and requirement is revision-sensitive. | QUARANTINE | Preserve historical result; rerun or assess applicability. |
| EVCT-011 | Revocation or integrity failure invalidates evidence used in aggregate. | REJECT_FOR_CURRENT_AGGREGATE | Exclude from current satisfaction, preserve audit history, recompute, remediate. |
| EVCT-012 | Required field absent but validator silently defaults it. | REJECT | No silent material-field inference; report missing field. |
| EVCT-013 | Record says PASS but raw output contains failing assertion. | REJECT | Flag result/output inconsistency; preserve raw evidence. |
| EVCT-014 | Record says BLOCKED with precise missing credential and no execution. | PASS_RECORD | Valid blocked observation only; not successful execution. |
| EVCT-015 | Evidence outside declared platform, tenant, geography, or workload. | ACCEPT_WITH_LIMITATION | Exclude from target scope; allow only bounded evidenced scope. |
| EVCT-016 | CI green on another branch/workflow config than candidate. | QUARANTINE | Bind CI to exact revision, config, workflow, environment. |
| EVCT-017 | Production observation samples one deployment and period. | ACCEPT_WITH_LIMITATION | Scope claim to deployment/time/population; no broad generalization. |
| EVCT-018 | Requirement lacks measurable acceptance criterion but aggregator is asked to pass it. | REJECT_AGGREGATION | Return BLOCKED/UNSCOPED; define criterion and evidence plan. |
| EVCT-019 | All mandatory criteria have current qualifying evidence; optional criteria untested. | ACCEPT_WITH_LIMITATION | Pass only explicit mandatory scope; report optional gaps. |
| EVCT-020 | One mandatory criterion fails, others pass. | FAIL | Do not average or majority-vote away mandatory failure. |
| EVCT-021 | One mandatory criterion BLOCKED, none fail. | BLOCKED | Aggregate blocked; identify blocker and remediation. |
| EVCT-022 | One mandatory criterion NOT_RUN, none fail/block. | INCONCLUSIVE | No pass assertion; execute missing test. |
| EVCT-023 | Sources conflict on material fact without precedence rule. | INCONCLUSIVE | Preserve both claims and reconcile; no silent selection. |
| EVCT-024 | Requirement changed after test; no impact analysis. | QUARANTINE | Applicability unknown; analyze impact and rerun affected tests. |

## 5. Candidate machine-readable validator output

A future result should include test_vector_id, validator_version, input_record_id, expected_disposition, actual_disposition, assertions (ID/outcome/reason), missing_fields, scope_mismatch, integrity_findings, remediation_action, execution_timestamp, IUT_revision, and raw_result_reference. Names/schema are candidates only and require design review, serialization tests, and governance approval.

## 6. Acceptance criteria for this artifact

- Map every vector to a canonical requirement and rule ID.
- Select and validate machine-readable fixture format.
- Implement positive, negative, boundary, and mutation tests.
- Run on pinned revision and capture raw output plus environment/revision provenance.
- Independently review expected outcomes and ambiguity.
- Cover conflicting/invalidating evidence and aggregate recomputation.
- Obtain explicit authority acceptance for version and scope.

## 7. Open issues

- EVCT-OI-01: Precedence for conflicting source classes.
- EVCT-OI-02: Evidence expiry/revalidation by requirement class.
- EVCT-OI-03: Reviewer qualification and independence criteria.
- EVCT-OI-04: Semantic/event duplicate detection beyond byte identity.
- EVCT-OI-05: Exact AND/OR, threshold, waiver, and exception aggregation policy.
- EVCT-OI-06: Revocation propagation and historical aggregate immutability.
- EVCT-OI-07: Privacy, retention, and secret-redaction controls.

## 8. Current disposition

Candidate fixture design drafted. No validator implementation, test execution, independent review, or acceptance is evidenced. All 24 vectors are NOT_RUN.
