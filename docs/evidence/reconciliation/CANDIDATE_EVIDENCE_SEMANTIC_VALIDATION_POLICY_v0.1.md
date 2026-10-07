# Candidate Evidence Semantic Validation Policy v0.1

**Status:** CANDIDATE / NON-NORMATIVE / NOT ACCEPTED  
**Scope:** Proposed semantic review rules for records conforming to `schemas/candidate/evidence-record-v0.1.schema.json`.  
**Authority:** This document does not amend the canonical TENTOR HOS architecture, accept any evidence, or authorize promotion of source-project claims.

## 1. Purpose and separation of concerns

JSON Schema conformance establishes only that a record matches the candidate structural contract. It does not establish that a claim is true, that its source is authentic, that an artifact exists, that a test was executed, or that the evidence satisfies a requirement.

The semantic review layer must produce a scoped disposition and retain the reasons and unresolved conditions. It must not silently convert missing information into PASS.

## 2. Candidate dispositions

| Disposition | Meaning |
|---|---|
| REJECT | Structurally or semantically unusable for the asserted evidence purpose; retain the rejection reason. |
| QUARANTINE | Provenance, integrity, authority, or conflict concerns prevent use as accepted evidence. |
| BLOCKED_NOT_PASS | A required prerequisite or access condition prevents the claimed validation; never aggregate as PASS. |
| LIMITED_SCOPE_ONLY | Evidence may support only the explicit bounded claim and cannot be generalized beyond scope. |
| ELIGIBLE_FOR_SCOPED_REVIEW_ONLY | Record is sufficiently described to enter human review; not accepted evidence and not a PASS. |
| ACCEPTED_FOR_REQUIREMENT_SCOPE | Only an authorized gate reviewer may assign after requirement mapping, provenance review, scope review, and applicable independent review. |

These are candidate dispositions, not implemented runtime behavior.

## 3. Mandatory review dimensions

A semantic reviewer should evaluate each dimension separately and record its evidence, result, and rationale:

1. **Identity and uniqueness:** record ID is present, stable, and not conflicting with an existing record.
2. **Claim precision:** subject, assertion, requirement identifier/version, and claimed outcome are explicit and falsifiable.
3. **Scope completeness:** revision, environment, platform/provider/tenant/workload/time window, and boundaries are recorded where material. Unknowns remain explicitly unknown.
4. **Provenance and integrity:** source locator/type, capture time, integrity result, hashes where applicable, and parent-record links are checked against the actual artifacts.
5. **Artifact availability:** each referenced artifact is retrievable and corresponds to the claim; a locator string alone is not proof.
6. **Evidence-class fit:** evidence type is appropriate to the claim. For example, provider artifact receipt alone does not prove end-user playback, product E2E, or user delivery.
7. **Requirement coverage:** evidence maps to a versioned requirement and covers its acceptance conditions; partial coverage stays partial.
8. **Temporal and revision relevance:** evidence is not silently applied to a different code revision, provider, environment, tenant, or time window.
9. **Conflict and supersession:** contradictory, revoked, quarantined, or superseded records are surfaced and resolved under an authorized rule; they are not silently discarded.
10. **Review authority:** reviewer identity, role, independence where required, and decision rationale are recorded.

## 4. Candidate non-promotion rules

- A schema-valid record is not automatically semantically valid.
- A semantic review disposition of ELIGIBLE_FOR_SCOPED_REVIEW_ONLY is not acceptance.
- A source declaration or historical status must remain attributed to its source and time period.
- Synthetic fixtures and CI tests of this schema are evidence about the harness only, not about TENTOR HOS runtime or any source project.
- Provider success, artifact existence, artifact playback, product end-to-end execution, and user delivery are distinct claims.
- A missing artifact, missing provenance, failed integrity check, unresolved contradiction, or unverified required prerequisite cannot be converted to PASS by inference.
- Aggregate status must not exceed the strongest requirement-level conclusion actually supported by accepted, in-scope evidence. Any mandatory FAIL or BLOCKED condition must remain visible.

## 5. Required semantic decision record

For each reviewed record, retain at minimum:

- record ID and immutable record revision/hash;
- reviewer and review timestamp;
- requirement ID/version and exact scope evaluated;
- disposition;
- per-dimension findings and artifact references;
- limitations, conflicts, and unresolved questions;
- remediation actions and accountable owner or role;
- gate authorization reference when acceptance is granted.

The current candidate evidence-record schema does not yet encode all of these fields as mandatory. This is a known schema-to-policy gap, not an implementation claim.

## 6. Conformance and acceptance work still required

1. Map every rule above to explicit schema fields or a versioned semantic review contract.
2. Add executable semantic validators and adversarial fixtures, including contradictory status, absent artifacts, scope mismatch, duplicate IDs, invalid lineage, and unsupported evidence-class/claim combinations.
3. Demonstrate negative controls and mutation tests.
4. Obtain independent review and record the review evidence.
5. Obtain explicit authorization before promoting this candidate policy or schema to canonical status.

**Current disposition:** Draft candidate for review. No semantic acceptance or architecture lock is granted.
