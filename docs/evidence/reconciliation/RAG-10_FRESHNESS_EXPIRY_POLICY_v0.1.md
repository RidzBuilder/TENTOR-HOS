# RAG-10 — Evidence Freshness / Expiry Policy v0.1

**Status:** WORKING CANDIDATE / NON-CANONICAL / NOT ACCEPTED

1. Freshness is scope-specific; no universal TTL is assumed.
2. Evidence must declare observation timestamp and applicable revision/environment.
3. Evidence is STALE_OR_MISMATCHED when applicability to the requested scope/revision/environment cannot be established.
4. Expiry preserves historical evidence but prevents it satisfying a current criterion.
5. Revalidation requires a new qualifying observation.
6. Copying or re-dating an artifact does not refresh observation time.
7. Provider/runtime evidence must be re-evaluated after material provider, adapter, target-runtime, or policy changes.
8. Freshness cannot be inferred from document modification time alone.

No numerical TTL is accepted by this candidate policy; domain-specific TTL requires explicit governance.
