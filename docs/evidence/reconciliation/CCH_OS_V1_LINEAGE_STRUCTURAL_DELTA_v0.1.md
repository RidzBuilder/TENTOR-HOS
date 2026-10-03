# CCH-OS v1.0 ↔ v1.1 ↔ ECAA-01 — Structural Delta and Lineage Map v0.1

**Date:** 2026-09-27  
**Gate:** S00-05 / CR-02  
**Status:** STRUCTURAL COMPARISON COMPLETE AT HEADING/CLAUSE-FAMILY LEVEL; NORMATIVE DELTA AND APPROVAL LINEAGE OPEN  
**Scope:** Supplied baseline text files only; no live repository history or author/approver metadata independently audited.

## 1. Sources compared

1. `TH-EV-005`: `CCH-OS_Architecture_Specification_v1.0.txt` (17,326 bytes in bundle).
2. `TH-EV-011`: `CCH-OS_Architecture_Specification_v1.1_Structurally_Corrected.txt` (24,931 bytes in bundle).
3. `TH-EV-012`: `CCH-OS_Architectural_Evolution_Artifact_ECAA-01_v1.0.txt` (13,721 bytes in bundle).

The three artifacts are distinct documents with distinct purposes. The word “structurally corrected” in the v1.1 filename is source metadata, not independent proof that every v1.0 normative clause is superseded or that the correction was approved.

## 2. Structural comparison (not a line-by-line semantic diff)

| Topic / clause family | v1.0 visible structure | v1.1 visible structure | ECAA-01 visible structure | Reconciliation |
|---|---|---|---|---|
| Core architecture flow | Semantic Intent → System Contracts → Core Runtime → Agent/Workflow Orchestration → Capabilities → Adapters → External Systems | Retains same seven named structural elements in its opening architecture flow | Adds a more explicit sequence: User Intent → Intent Interpretation → Workflow Definition → Capability Specification → Adapter Resolution → Native Tool/Service → Execution → Output → Evaluation → Feedback/Evolution | Apparent refinement/expansion; exact normative insertion and approval status require clause mapping. |
| Capability vs implementation | Capability and adapter/tool distinction appears in v1.0 | Retains explicit “what can be done” vs “how it is done” distinctions | Adds explicit capability specification and native capability resolution sections | Conceptual convergence; no TENTOR HOS universal acceptance. |
| Provenance/reference identity | Reference identity/version/lineage/equivalence family appears in v1.0 | Same family appears in v1.1 | ECAA-01 focuses on creator-production case and its architectural evolution | Shared concern does not establish common evidence schema. |
| Runtime lifecycle/state | v1.0 includes architecture and runtime contract content; detailed state families require full clause-level mapping | v1.1 visibly includes observation/evaluation/decision/authorization/action/result/state update/event/history cycle and state labels | ECAA-01 adds execution, output, evaluation, feedback/evolution sequence | v1.1 and ECAA-01 may elaborate different aspects; don't infer equivalence between event/state and feedback loop. |
| Domain-specific creator flow | Not established as universal by the high-level architecture headings | Broader architecture text includes creator/workflow examples and other expanded concepts | ECAA-01 explicitly discusses script, storyboard, storyboard image, social output, performance evaluation, and CCH-OS/AKOS relevance | ECAA-01 is a creator-derived evolution input, not domain-independent validation. |
| Guard/capability boundary | v1.0 detailed content requires normative clause mapping | v1.1 contains explicit guard/authorization/action flow and state labels | ECAA-01 includes “Guard / Capability Boundary” and end-to-end example sections | Compare exact enforcement semantics and test evidence before treating as operational. |

## 3. Observed lineage limitations

- The supplied baseline contains the three text artifacts and registry links, but no signed approval record or complete clause-by-clause change-control record tying each v1.0 clause to v1.1 disposition.
- ECAA-01 is an architectural evolution artifact with explicit creator-production examples. It is not by itself evidence that changes were merged, implemented, tested, or independently accepted.
- A structural heading comparison cannot determine whether unchanged wording was semantically modified, whether clauses were deleted or relocated, or whether a clause is normative, explanatory, or illustrative.
- Source review notes describe v1.1 as structurally corrected, but the precise authority and approval chain for that label is not independently established by the three files alone.
- No current CCH-OS branch, commit ancestry, PR approval, CI run, runtime, or conformance test was inspected in this comparison.

## 4. Required closure work for CR-02

1. Establish canonical source versions and repository commit/blob identity for each artifact, with reproducible hashes.
2. Produce a paragraph/requirement-level mapping: v1.0 clause ID → v1.1 clause ID(s) → change type (retained, clarified, moved, split, merged, deleted, added, conflict) → rationale → evidence.
3. Map every ECAA-01 proposal to the affected v1.1/v1.0 clauses and mark as accepted, rejected, deferred, or unresolved, citing explicit decision records.
4. Retrieve or identify the authorized approval/decision records and responsible approver; do not infer approval from filename or “LOCKED” wording.
5. Link each normative clause to its conformance test and actual execution evidence; distinguish design correction from implemented correction.
6. Preserve unresolved or conflicting clauses as explicit issues; do not silently choose the newest file.

## 5. Disposition

CR-02 is **PARTIALLY PROGRESSED**: structural clause families and domain-specific scope are mapped, but normative clause-level delta, approval chain, and implementation/conformance linkage remain OPEN. No version is promoted as canonical TENTOR HOS, and no CCH-OS implementation PASS is inferred.
