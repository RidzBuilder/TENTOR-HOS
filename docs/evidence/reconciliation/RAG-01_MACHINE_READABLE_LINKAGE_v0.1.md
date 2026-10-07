# RAG-01 — Machine-Readable Requirement/Evidence/Status Linkage v0.1

**Status:** WORKING CANDIDATE / NON-CANONICAL / NOT ACCEPTED

## Purpose
Provide an explicit machine-readable chain:
CRQ -> criterion -> evidence -> aggregation result -> lifecycle transition -> governance decision.

The linkage is referential. It does not assert authenticity, sufficiency, independent verification, or acceptance of referenced evidence.

## Controls
- Every link requires a candidate CRQ, criterion, at least one evidence reference, bounded aggregation result, lifecycle transition, and governance decision reference.
- PASS is a result only; it cannot encode TESTED, INDEPENDENTLY-VERIFIED, or ACCEPTED-FOR-SCOPE.
- Missing evidence is represented by absence/blocked semantics, not invented evidence.
- Governance decision reference is mandatory even for candidate transitions.
- The schema is candidate-only and does not establish canonical ontology.

## Candidate verification
- Schema + fixtures validator: 2/2 valid.
- Negative controls: 3/3 rejected.
- These are synthetic structural checks only.
