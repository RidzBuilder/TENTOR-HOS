# Candidate Scoped Evidence Aggregation Semantics v0.1

Status: WORKING DRAFT / NON-NORMATIVE / NOT ACCEPTED

## 1. Objective

Specify candidate rules for computing a requirement or gate status from evidence without flattening scope, maturity, provenance, or uncertainty. This is a proposal for testability, not an approved TENTOR HOS standard.

## 2. Non-negotiable distinctions

1. Evidence class is not result. A TEST_PLAN may contain an expected PASS but is not a TEST_EXECUTION.
2. Record validity is not requirement satisfaction. A well-formed BLOCKED record can be valid evidence of a blocker.
3. Requirement status is scoped. It must name requirement version, system revision, environment, platform/provider, workload, and time window where applicable.
4. Evidence records are not interchangeable. Source declarations, tests, CI, runtime observations, provider artifacts, and independent reviews support different claims.
5. Historical status is immutable as history, but current satisfaction must be recomputed when applicable evidence is revoked, superseded, or invalidated.
6. Mandatory criteria cannot be averaged, voted, or compensated by unrelated successes.

## 3. Candidate aggregation inputs

For each requirement R and declared scope S, provide:
- versioned acceptance criteria and mandatory/optional classification;
- evidence-to-criterion links and evidence class;
- evidence result and validator disposition;
- provenance/integrity status;
- applicability (scope and revision match);
- freshness/validity/revocation status;
- approved waiver/exception records, if policy permits;
- aggregation policy version and evaluator revision.

If the criterion set, scope, or aggregation policy is absent, the aggregator must not return PASS.

## 4. Candidate per-criterion state resolution

Resolve in this order:

A. INVALID: evidence fails schema/integrity/provenance or is revoked for the claim. Exclude it from current satisfaction and emit an integrity finding.

B. NOT_APPLICABLE: evidence or criterion is outside the explicitly declared scope. It cannot satisfy an in-scope criterion. Do not automatically waive the criterion.

C. INSUFFICIENT: evidence class or maturity is insufficient for the criterion (for example, a plan presented as execution, or provider artifact presented as E2E). Record missing evidence class and remediation.

D. STALE_OR_MISMATCHED: revision, environment, configuration, requirement version, or freshness does not match. Quarantine pending impact analysis or rerun.

E. CONFLICTED: qualifying evidence conflicts on a material assertion and no approved precedence/reconciliation rule resolves it. Preserve each claim; do not select silently.

F. FAIL: at least one applicable, qualifying, current test for a mandatory criterion demonstrates failure under the accepted criterion. Contradictory evidence does not erase the failure without governed adjudication and retest.

G. PASS: all evidence conditions required by the criterion are met, with no unresolved contradiction or invalidation, and required review is complete.

H. BLOCKED: execution or evaluation cannot proceed due to a documented external prerequisite, authorization, capability, or dependency. The blocker must be concrete and evidence-linked.

I. NOT_RUN: required evaluation has not been attempted and no evidenced blocker explains why.

J. INCONCLUSIVE: evidence is insufficient or ambiguous in a way not captured by the more specific states above, including unresolved conflicts or unreliable measurement.

This precedence is a candidate decision order. FAIL and BLOCKED must not be hidden by later lower-precedence states; INVALID evidence is excluded, but a separate qualifying failure remains a failure.

## 5. Candidate gate aggregation

For a gate with mandatory criteria M and optional criteria O:

- FAIL if any mandatory criterion is FAIL.
- BLOCKED if no mandatory criterion is FAIL and at least one is BLOCKED.
- INCONCLUSIVE if no mandatory criterion is FAIL/BLOCKED and at least one mandatory criterion is INCONCLUSIVE.
- NOT_RUN if no mandatory criterion is FAIL/BLOCKED/INCONCLUSIVE and at least one mandatory criterion is NOT_RUN.
- PASS only if every mandatory criterion is PASS and required governance/review conditions are satisfied.
- If no mandatory criteria are defined, return UNSCOPED, not PASS.
- Report optional criteria separately. Optional failures do not silently fail the mandatory gate, but must remain visible and cannot be represented as fully complete.
- Any waiver must be explicit, authorized, scoped, time-bounded, reasoned, and linked to residual risk; absent such a policy, waiver does not convert failure to pass.

The precise ordering among BLOCKED, INCONCLUSIVE, and NOT_RUN is proposed and requires adversarial review. Implementations should report all criterion-level states even when a single aggregate headline is emitted.

## 6. Invalidation and recomputation

When evidence is revoked, found corrupt, or becomes inapplicable:
1. Preserve the original evidence record and prior aggregate snapshot as historical records.
2. Mark the evidence as invalid for current use with reason, authority/source, timestamp, and scope.
3. Identify all criteria, gates, and downstream decisions that depended on it.
4. Recompute current statuses using the same versioned aggregation policy or explicitly record a policy migration.
5. Emit remediation actions and affected downstream artifacts.
6. Never rewrite history to make the old aggregate appear never to have existed.

## 7. Conflict handling

Conflicts must be recorded as first-class objects containing claim IDs, source/evidence IDs, conflicting values, scope, timestamps, provenance, and resolution state. A precedence rule must be defined in advance and be relevant to the claim type. Source recency alone is not a universal precedence rule. If unresolved, status remains CONFLICTED/INCONCLUSIVE and promotion is blocked.

## 8. Required output

At minimum: subject ID/version; declared scope; criteria and mandatory flags; per-criterion state; evidence IDs and class; exclusions and reasons; conflict/invalidation references; aggregate state; aggregation policy version; evaluator version/revision; evaluation time; remediation list; and immutable snapshot identifier.

## 9. Synthetic acceptance examples

- Four mandatory criteria PASS and one mandatory FAIL => gate FAIL.
- All mandatory criteria PASS; optional one NOT_RUN => mandatory gate may PASS with optional gap explicitly reported.
- All mandatory criteria PASS except one BLOCKED => gate BLOCKED, not PASS.
- A prior PASS evidence item is revoked, leaving a mandatory criterion without qualifying evidence => recompute; likely NOT_RUN, INCONCLUSIVE, or BLOCKED based on actual state, never retain PASS automatically.
- One criterion has conflicting qualifying evidence and no adjudication policy => INCONCLUSIVE; no gate promotion.
- A provider artifact passes its provider-level criterion but playback criterion has no evidence => provider criterion may pass; product E2E gate cannot pass.

These are synthetic expected outcomes, not executed tests.

## 10. Open issues and required decisions

- AGG-OI-01: Confirm aggregate precedence among BLOCKED, INCONCLUSIVE, and NOT_RUN.
- AGG-OI-02: Define waiver authority, maximum duration, renewal, and risk ownership.
- AGG-OI-03: Define evidence freshness by class and requirement criticality.
- AGG-OI-04: Define policy migration and historical snapshot semantics.
- AGG-OI-05: Define conflicts and adjudication authority per evidence domain.
- AGG-OI-06: Define whether and how probabilistic/threshold criteria are aggregated.
- AGG-OI-07: Define mandatory review and independent review applicability.

## 11. Current disposition

Drafted for review and adversarial testing only. Not canonical, not implemented, not executed, not independently reviewed, and not accepted. No project or gate status is changed by this document.
