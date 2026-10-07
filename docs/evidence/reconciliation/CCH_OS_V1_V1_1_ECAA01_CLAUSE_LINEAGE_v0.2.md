# CCH-OS v1.0 ↔ v1.1 ↔ ECAA-01 — Bounded Clause/Requirement Lineage v0.2

**Date:** 2026-10-05  
**Parent gate:** S00-05 / CR-02  
**Status:** PARTIAL — BOUNDED RECONCILIATION COMPLETE; APPROVAL AND IMPLEMENTATION LINKAGE OPEN  
**Canonical status:** NOT ACCEPTED FOR TENTOR HOS  
**Method:** Direct comparison of the three captured baseline text artifacts. No approval metadata or live CCH-OS repository history is inferred.

## 1. Source identities verified from the supplied baseline

| Artifact | Captured path | Bytes | SHA-256 | Direct status text |
|---|---|---:|---|---|
| CCH-OS v1.0 | `01_EVIDENCE/CCH-OS/CCH-OS_Architecture_Specification_v1.0.txt` | 17,326 | `b21928c13c02cbf90fcac3852309b3fe177277881be1217840d8ccd352565faa` | Architecture Specification; Implementation-Independent; Contract-Driven, Modular, Extensible, Testable; Technology-Agnostic |
| CCH-OS v1.1 | `01_EVIDENCE/CCH-OS/architecture/CCH-OS_Architecture_Specification_v1.1_Structurally_Corrected.txt` | 24,931 | `6e444491af880db0c94e0d5958437483205cdac989564cfae3ed09da4654cef0` | Header says “v1.1 / Structurally Corrected / Pending Structural Re-Validation”; embedded document title at line 5 says “CCH-OS ARCHITECTURE SPECIFICATION v1.0” |
| ECAA-01 | `01_EVIDENCE/CCH-OS/evolution/CCH-OS_Architectural_Evolution_Artifact_ECAA-01_v1.0.txt` | 13,721 | `f73ce26b50238f9422f2d62495d4c4f0022886cc0fa733d451a9da5767a3b5d1` | Artifact status: Proposed / Ready for Library; architectural evolution candidate; not automatically baseline |

## 2. Important source-boundary finding

The captured v1.0 artifact ends at **5.15 Transformation Contract**. The captured v1.1 artifact continues through:

- 5.24 Lineage Contract;
- 6 Runtime Architecture;
- 7 State Architecture;
- 8 Event Architecture;
- 9 Agent Runtime;
- and additional sections beyond the displayed capture boundary.

Therefore this document **does not claim a complete semantic diff of the entire v1.0 specification**. Any v1.0→v1.1 mapping below is limited to clauses visible in the captured v1.0 artifact plus the explicit additions visible in v1.1.

This truncation is itself evidence and must not be silently repaired from memory, later versions, or assumptions.

## 3. Clause-family lineage

| Lineage ID | v1.0 source | v1.1 source | ECAA-01 relationship | Observed change | Disposition |
|---|---|---|---|---|---|
| CR02-001 | 1.1 System Identity | 1.1 System Identity | ECAA-01 remains within CCH-OS creator-production domain | Core identity and purpose are retained; v1.1 expands runtime/state/provenance vocabulary. | RETAINED + EXPANDED |
| CR02-002 | 1.2 Intent → Contracts → Runtime → Orchestration → Capability → Adapter → External | Same sequence | ECAA-01 makes Intent Interpretation → Workflow Definition → Capability Specification → Adapter Resolution → Native Tool → Execution → Output → Evaluation → Feedback explicit. | ECAA-01 is an explicit capability-resolution refinement of the broad v1.x flow, not proof that the entire v1.1 architecture was replaced. | REFINED / PROPOSED |
| CR02-003 | 1.3 System Boundary | 1.3 System Boundary | ECAA-01 keeps platform/tool independence | v1.1 explicitly lists CCH-OS ownership of authority enforcement, execution trace, persistence abstraction, governance, and domain orchestration; humans retain decisions/approvals/overrides. | EXPANDED |
| CR02-004 | 2.1 Semantic Independence | 2.1 Semantic Independence | ECAA-01 states architecture-defined capability vs implementation-defined adapter | Direct wording/requirement is retained. | RETAINED |
| CR02-005 | 2.12 Capability / Tool Separation | 2.12 Capability / Tool Separation | ECAA-01 directly elaborates this boundary | ECAA-01 adds explicit Capability Specification, Capability Registry, Capability-to-Adapter Mapping, Adapter Registry, Capability Guard, and Resolution Mechanism. | EXPLICIT REFINEMENT |
| CR02-006 | 2.13 Authority Separation | 2.13 Authority Separation | ECAA-01 introduces Capability Guard | “Capability ≠ Authority” is retained; ECAA-01 guard is a proposed mechanism for constraining capability use. No enforcement test is supplied here. | RETAINED + PROPOSED ENFORCEMENT REFINEMENT |
| CR02-007 | 2.14 Provenance and Lineage | 2.14; modules/contracts expanded in v1.1 | ECAA-01 references architectural foundation and evolution, but does not replace provenance/lineage contracts | v1.1 expands provenance/lineage into explicit modules/contracts. | EXPANDED |
| CR02-008 | 2.15 Version Separation | 2.15; 5.7 Version Contract | ECAA-01 does not alter identity/version principle | v1.1 makes version contract explicit. | RETAINED + FORMALIZED |
| CR02-009 | 2.16 Failure Transparency | 2.16 Failure Transparency | ECAA-01 does not provide equivalent failure-runtime evidence | Principle retained in v1.1; no ECAA-01 replacement established. | RETAINED |
| CR02-010 | 2.17 Replaceability | 2.17 Replaceability | ECAA-01 adapter-agnostic model supports replaceability conceptually | Conceptual reinforcement only; no runtime swap test in this artifact set. | RETAINED + REINFORCED |
| CR02-011 | 2.18 Evolvability | 2.18 Evolvability | ECAA-01 is itself an evolution artifact | ECAA-01 explicitly describes itself as an architectural evolution candidate and feedback/evolution stage. | RETAINED + EVOLUTION INPUT |
| CR02-012 | 3 Layer Architecture (L0–L7 visible in v1.0) | 3 Layer Architecture L0–L7 | ECAA-01 focuses on capability/adapter resolution rather than redefining all layers | v1.1 gives explicit responsibilities/dependencies/ownership for L0–L7. | STRUCTURAL ELABORATION |
| CR02-013 | 4 Module Architecture (captured through 4.27) | 4 Module Architecture (4.1–4.27) | ECAA-01 adds capability/adapter governance concepts | v1.1 makes modules for state, event, lifecycle, planning, action, agent, workflow, task, capability registry, adapter runtime, governance, provenance, lineage, history, persistence, observability, recovery explicit. | EXPANDED |
| CR02-014 | 5 Core Contracts (captured through 5.15) | 5.1–5.24 | ECAA-01 supplies no full replacement contract set | v1.1 explicitly adds/retains contracts for Agent, Capability, Tool Adapter, Workflow, Task, Artifact, Provenance, Lineage beyond the v1.0 capture boundary. | EXPANDED; v1.0 FULL BASELINE UNKNOWN |
| CR02-015 | Not visible in captured v1.0 after 5.15 | 6 Runtime Architecture | ECAA-01 execution/evaluation/feedback sequence is conceptually related | v1.1 specifies a canonical runtime cycle: input/event → context → observation → interpretation → evaluation → decision → plan → authorization → action → result → observation → state update → event → history/trace → next cycle. | ADDITION IN CAPTURE / V1.0 BASELINE UNKNOWN |
| CR02-016 | Not visible in captured v1.0 after 5.15 | 7 State Architecture | ECAA-01 does not define generic state model | v1.1 explicitly defines generic and domain state families including approval and publishing state. | ADDITION IN CAPTURE / V1.0 BASELINE UNKNOWN |
| CR02-017 | Not visible in captured v1.0 after 5.15 | 8 Event Architecture | ECAA-01 does not define event model | v1.1 distinguishes state from event and defines domain/runtime/integration events plus consumption requirements. | ADDITION IN CAPTURE / V1.0 BASELINE UNKNOWN |
| CR02-018 | Not visible in captured v1.0 after 5.15 | 9 Agent Runtime | ECAA-01 assumes workflow/agent orchestration but does not define this runtime contract | v1.1 exposes explicit agent architecture/execution model. | ADDITION IN CAPTURE / V1.0 BASELINE UNKNOWN |

## 4. ECAA-01 proposal lineage

The ECAA-01 artifact explicitly states:

- Core Data Contract remains the foundation.
- A Capability Specification Layer is added.
- Capability requirements are mapped through Adapter Resolution.
- Capability is architecture-defined; adapter is implementation-defined.
- Proposed additions include Capability Specification, Capability Registry, Capability-to-Adapter Mapping, Adapter Registry, Capability Guard, and Resolution Mechanism.
- The “new architectural principle” is **Explicit Capability, Agnostic Adapter**.
- The architectural formula is User Intent → Workflow → Capability Specification → Capability Guard → Adapter Resolution → Native Tool → Action → Outcome → Evaluation → Feedback.
- The artifact says it is **accepted as an architectural evolution candidate**, not as a full architecture reconstruction.
- It explicitly does not decide to replace the Core Data Contract or bind the architecture to Google AI Studio, Emergent, or a permanent vendor.
- The archival note states that adoption into the CCH-OS baseline requires gate, comparison, validation, and change-control.

Therefore ECAA-01 is best classified as a **proposed architectural evolution input**, not as evidence that the proposed changes were implemented or became canonical.

## 5. Metadata and authority findings

### 5.1 v1.1 internal title inconsistency

The v1.1 captured artifact has:

- Header: “CCH-OS • ARCHITECTURE SPECIFICATION v1.1”
- Status line: “v1.1 | Structurally Corrected | Pending Structural Re-Validation”
- Embedded title: “CCH-OS ARCHITECTURE SPECIFICATION v1.0”

This is a source-level metadata inconsistency. It does not prove an authoring error, rename, supersession, or approval event.

### 5.2 Approval lineage remains absent

The three captured files do not provide sufficient independent approval metadata to establish:

- who authorized v1.1;
- which v1.0 clauses were formally superseded;
- whether ECAA-01 was approved for baseline adoption;
- whether any proposed correction was merged into a runtime;
- whether an associated conformance test was executed.

Filename wording such as “Structurally Corrected,” “LOCKED,” or “Ready for Library” must not be treated as independent approval evidence.

### 5.3 Implementation/conformance linkage remains absent

The clause comparison establishes document content relationships only. It does not establish:

- implementation of v1.1;
- implementation of ECAA-01;
- runtime enforcement of capability/authority separation;
- provider/adapter swap conformance;
- end-to-end execution conformance;
- production acceptance.

## 6. CR-02 requirement/evidence matrix

| Candidate requirement | Source basis | Evidence currently available | Required closure evidence | Status |
|---|---|---|---|---|
| Semantic contracts remain implementation-independent | v1.0 2.1; v1.1 2.1 | Direct source text | Conformance test demonstrating representation/provider changes do not alter semantics | OPEN |
| Capability must remain distinct from tool/adapter | v1.0 2.12; v1.1 2.12; ECAA-01 §§5–7 | Direct source text across three artifacts | Agnostic swap test + contract-level validation | OPEN |
| Capability does not imply authority | v1.0 2.13; v1.1 2.13; ECAA-01 Capability Guard | Direct source text | Authorization denial/override/guard execution evidence | OPEN |
| Provenance/lineage must be explicit | v1.0 2.14, 4.5/4.22/4.23; v1.1 corresponding modules/contracts | Direct source text | Runtime provenance and lineage record conformance | OPEN |
| Failure must not silently become success | v1.0/v1.1 2.16 | Direct source text | Failure injection + state integrity test | OPEN |
| Capability resolution should be provider/adapter agnostic | ECAA-01 §§6–7, 13–14 | Proposed architectural artifact | Provider swap test with equivalent capability and preserved semantics | OPEN |
| Capability Guard should constrain required/optional/restricted capability use | ECAA-01 §13, §19 | Proposed architectural artifact | Executed guard matrix and denial evidence | OPEN |
| Runtime cycle must preserve authorization, state, event, history and trace boundaries | v1.1 §6 | Direct source text | Runtime conformance suite and trace evidence | OPEN |

## 7. CR-02 gate disposition

**Current disposition: PARTIALLY PROGRESSED — bounded clause-family reconciliation completed.**

What is now established:

1. Three exact captured artifacts and their checksums are identified.
2. Shared clause families between v1.0 and v1.1 are mapped.
3. ECAA-01's explicit architectural additions and non-decisions are mapped.
4. The v1.1 metadata/title inconsistency is recorded.
5. The captured v1.0 truncation boundary is recorded rather than silently filled.
6. Approval and implementation/conformance evidence are explicitly separated from document content.

What remains OPEN:

- complete v1.0 clause corpus beyond the captured 5.15 boundary;
- formal v1.0→v1.1 change-control/approval lineage;
- ECAA-01 adoption decision;
- implementation linkage;
- actual conformance/runtime evidence;
- independent review.

**CR-02 is not CLOSED.**

## 8. Next action

Proceed to the ontology crosswalk only after preserving this CR-02 boundary. The ontology work must distinguish:

- same term / same meaning;
- same term / different meaning;
- different term / equivalent meaning;
- parent-child relationship;
- implementation-specific concept;
- unresolved/non-equivalent concept.

No ontology candidate becomes a canonical TENTOR HOS primitive until it survives the requirements/evidence gate.
