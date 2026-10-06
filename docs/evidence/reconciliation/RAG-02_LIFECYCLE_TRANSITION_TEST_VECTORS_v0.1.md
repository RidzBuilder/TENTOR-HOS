# RAG-02 — Lifecycle Transition Test Vectors v0.1

**Status:** WORKING CANDIDATE / NON-CANONICAL / NOT ACCEPTED

A lifecycle transition requires both a qualifying evidence/result condition and the governance condition. A result label alone never grants a lifecycle state.

| ID | Scenario | Expected |
|---|---|---|
| LT-001 | criteria defined + explicit approval | PROPOSAL -> APPROVED-DESIGN |
| LT-002 | implementation identity + approved design | APPROVED-DESIGN -> IMPLEMENTED |
| LT-003 | executable criterion + actual execution | IMPLEMENTED -> TESTED |
| LT-004 | PASS but no execution evidence | BLOCK transition |
| LT-005 | tested result but no independence basis | BLOCK transition |
| LT-006 | independent verification but no acceptance authority | BLOCK transition |
| LT-007 | source-declared PASS only | BLOCK transition |
| LT-008 | revoked evidence used for promotion | BLOCK |
| LT-009 | stale/mismatched evidence | BLOCK or re-evaluate |
| LT-010 | unresolved conflict | BLOCK |

These are candidate policy tests, not evidence that TENTOR HOS has passed them.
