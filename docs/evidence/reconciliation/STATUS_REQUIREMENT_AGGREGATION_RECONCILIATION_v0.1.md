# TENTOR HOS V.2 — Status / Requirement / Aggregation Reconciliation v0.1

**Date:** 2026-10-06  
**Gate:** S00-05 / CR-03 / CR-06  
**Status:** WORKING RECONCILIATION / NON-CANONICAL / NOT ACCEPTED

## 1. Objective

Reconcile the three candidate control layers already present in the repository:

1. **Candidate requirements** — what a future TENTOR HOS requirement would have to prove.
2. **Evidence aggregation semantics** — how evidence can produce a bounded criterion/gate result.
3. **Status & evidence promotion taxonomy** — how a subject may move through lifecycle/governance states.

The reconciliation explicitly prevents these layers from being collapsed into one status vocabulary.

## 2. Core separation

| Layer | Answers | Candidate outputs | Cannot prove by itself |
|---|---|---|---|
| Requirement | What must be true? | CRQ-01…CRQ-12 | That it is implemented or satisfied |
| Evidence | What evidence exists and what did it observe? | evidence class/result/maturity | Governance approval |
| Aggregation | What is the bounded criterion/gate result? | PASS/FAIL/BLOCKED/NOT_RUN/INCONCLUSIVE/UNSCOPED | Lifecycle promotion |
| Lifecycle | What state is the subject authorized to occupy? | PROPOSAL…PRODUCTION-ACCEPTED | Truth beyond its declared scope |
| Governance | Who authorized the transition? | decision/approval/revocation/deprecation | Technical evidence itself |

**Invariant:** a PASS result is not an ACCEPTED-FOR-SCOPE lifecycle state.

## 3. Requirement-to-control reconciliation

| Requirement | Primary evidence/aggregation dependency | Lifecycle dependency | Current test coverage | Current disposition |
|---|---|---|---|---|
| CRQ-01 Intent traceability | criterion links + lineage evidence; PASS requires traceable request/semantic mapping | IMPLEMENTED → TESTED; later verification required for acceptance | No runtime lineage test | OPEN |
| CRQ-02 Capability/provider separation | capability/provider distinction + provider-swap criterion | IMPLEMENTED → TESTED; independent verification required before acceptance | No provider-swap harness | OPEN |
| CRQ-03 Authority before invocation | authorization criterion + positive/negative execution evidence | IMPLEMENTED → TESTED; acceptance requires bounded authority decision | No live enforcement test | OPEN |
| CRQ-04 Status/evidence boundary | adversarial evidence-state screening + execution evidence | source declaration cannot skip to TESTED/ACCEPTED | Synthetic adversarial coverage exists | OPEN; candidate control exercised only |
| CRQ-05 Restore/history safety | state transition criterion + provider-call observation | IMPLEMENTED → TESTED | No runtime restore test | OPEN |
| CRQ-06 Exact/partial/fallback/failure semantics | typed result criterion + failure injection | IMPLEMENTED → TESTED | Aggregation states cover gate outcomes, not product result taxonomy | OPEN |
| CRQ-07 Observable acceptance | criterion/evaluator/evidence/scope fields | APPROVED-DESIGN requires explicit criteria; later TESTED/VERIFIED | Schema/semantic candidate tests exist | OPEN |
| CRQ-08 Evidence class/provenance separation | candidate schema + semantic/adversarial screening | lifecycle promotion requires evidence refs and provenance | Schema 7/7; semantic 7/7; adversarial 8/8 in recorded CI | OPEN |
| CRQ-09 State/event/history separation | lifecycle model + replay/recovery criteria | IMPLEMENTED → TESTED | No lifecycle replay harness | OPEN |
| CRQ-10 Evolution governance | lineage/impact/authority/regression criteria | PROPOSAL → APPROVED-DESIGN and later promotion gates | No governance execution harness | OPEN |
| CRQ-11 Domain boundary | domain fixtures + negative/non-mappable case | APPROVED-DESIGN only after explicit scope | No 3-domain conformance harness | OPEN |
| CRQ-12 Provider output → target E2E | runtime provenance + E2E criterion | TESTED → INDEPENDENTLY-VERIFIED → ACCEPTED-FOR-SCOPE | No target runtime E2E evidence | OPEN |

## 4. Evidence-result-to-lifecycle transition rules

A candidate gate result may support a lifecycle transition only when the transition contract is also satisfied.

### Example A — PASS

`PASS` means the declared mandatory criteria passed within the candidate aggregation scope.

It does **not** mean:

`PASS = TESTED = INDEPENDENTLY-VERIFIED = ACCEPTED`

At minimum:

- TESTED requires actual execution evidence;
- INDEPENDENTLY-VERIFIED requires qualifying independence;
- ACCEPTED-FOR-SCOPE requires explicit authority and decision record.

### Example B — BLOCKED

`BLOCKED` is a result indicating a concrete prerequisite prevented evaluation.

It must not be promoted to ACCEPTED.

The blocker becomes a remediation input.

### Example C — NOT_RUN

`NOT_RUN` is not failure and not acceptance.

A lifecycle subject cannot claim TESTED solely because criteria exist.

### Example D — source-declared PASS

A source artifact saying PASS remains SOURCE-DECLARED unless current evidence and governance independently satisfy the applicable promotion contract.

## 5. Existing synthetic controls and their exact meaning

Recorded candidate CI provides bounded control evidence:

- schema/fixture expectations: **7/7**
- semantic screening expectations: **7/7**
- adversarial semantic screening: **8/8**
- negative controls: **3/3**
- aggregation semantics: **10/10**

These results establish only that the synthetic candidate harness behaves according to its encoded expectations at the recorded CI revision.

They do **not** establish:

- authenticity of the 61 source artifacts;
- runtime conformance of ACS/ACOS/ACPA/CCH-OS/EVO/LCH-OS;
- TENTOR HOS implementation conformance;
- canonical evidence ontology;
- production acceptance;
- independent verification of the candidate rules.

## 6. Status promotion gates mapped to evidence states

| Lifecycle transition | Minimum evidence/result condition | Additional governance condition |
|---|---|---|
| PROPOSAL → APPROVED-DESIGN | criteria/scope defined; material conflicts visible | explicit approval authority + decision |
| APPROVED-DESIGN → IMPLEMENTED | implementation identity/revision + traceability | approved design remains applicable |
| IMPLEMENTED → TESTED | executable criteria + actual execution evidence | revision/environment match |
| TESTED → INDEPENDENTLY-VERIFIED | qualifying test result + review evidence | independence basis |
| INDEPENDENTLY-VERIFIED → ACCEPTED-FOR-SCOPE | verification supports accepted criteria | explicit authorized acceptance |
| ACCEPTED-FOR-SCOPE → PRODUCTION-ACCEPTED | bounded production observation | explicit production decision |

No transition is granted merely because the previous row contains PASS.

## 7. Invalid promotion patterns detected by reconciliation

The following are formally treated as invalid shortcuts:

1. `SOURCE-DECLARED PASS → ACCEPTED-FOR-SCOPE`
2. `DESIGN → IMPLEMENTED`
3. `IMPLEMENTED → TESTED` without execution
4. `TESTED → INDEPENDENTLY-VERIFIED` without independence
5. `INDEPENDENTLY-VERIFIED → PRODUCTION-ACCEPTED` without production decision
6. provider artifact → target E2E
7. CI success → production acceptance
8. repeated copies → independent corroboration
9. unresolved conflict → promotion
10. revoked evidence → continued satisfaction
11. accepted revision A → accepted revision B without re-evaluation

## 8. Reconciliation findings

### RF-01 — Structural compatibility

The candidate requirement matrix, aggregation semantics, and lifecycle taxonomy are **structurally compatible** because they operate on different semantic axes.

### RF-02 — Aggregation is not promotion

The current aggregation harness can produce PASS/FAIL/BLOCKED/etc., but there is no legitimate path in which its headline output alone promotes a lifecycle state.

### RF-03 — Candidate CI is itself bounded evidence

The successful CI runs are evidence for the candidate harness behavior, not evidence that the candidate requirements are satisfied by TENTOR HOS.

### RF-04 — Requirement coverage remains mostly future-facing

Of the 12 candidate requirements, only evidence/status boundary and evidence-model controls have meaningful synthetic harness coverage. The majority still require runtime, provider-swap, authorization, lifecycle, domain, or E2E tests.

### RF-05 — Canonicalization remains blocked

No candidate requirement should be promoted to canonical solely because it appears in this reconciliation.

## 9. Open gaps generated by reconciliation

- **RAG-01:** machine-readable linkage between CRQ, criterion, evidence record, aggregate result, and lifecycle transition.
- **RAG-02:** explicit lifecycle-transition test vectors.
- **RAG-03:** provider-swap conformance harness.
- **RAG-04:** authorization/consent enforcement harness.
- **RAG-05:** state/history/recovery harness.
- **RAG-06:** typed fulfillment/fallback taxonomy and execution harness.
- **RAG-07:** cross-domain negative/mapping harness.
- **RAG-08:** target-system E2E provenance harness.
- **RAG-09:** governance decision/approval record schema.
- **RAG-10:** freshness/expiry policy.
- **RAG-11:** conflict adjudication and waiver policy.

These are reconciliation gaps, not implementation authorization.

## 10. Gate disposition

- Candidate requirements: **0/12 canonical**
- Candidate aggregation semantics: **working / synthetic-tested / not accepted**
- Status promotion taxonomy: **working / not accepted**
- Cross-project ontology: **working / not accepted**
- CR-03: **OPEN**
- CR-06: **OPEN**
- S00-05: **IN PROGRESS**
- S00-06 Fundamental Specification: **NOT STARTED**
- S00-07 Implementation: **NOT STARTED**
- S00-08 U-AAFA: **GATED**

**Conclusion:** reconciliation is internally coherent enough to proceed to controlled candidate test-vector expansion, but not sufficient for canonicalization or architecture synthesis acceptance.
