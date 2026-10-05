# TENTOR HOS V.2 — Ontology Equivalence Gate v0.1

Date: 2026-10-05
Gate: S00-05 / cross-project ontology reconciliation
Status: WORKING / NOT CANONICAL / NOT ACCEPTED

## Purpose

This gate defines how a cross-project concept may be treated as semantically equivalent. Terminology overlap is not sufficient.

## Relation classes

1. SAME_TERM_SAME_MEANING — source definitions and operational role materially match.
2. SAME_TERM_DIFFERENT_MEANING — lexical overlap without semantic equivalence.
3. DIFFERENT_TERM_EQUIVALENT_ROLE_CANDIDATE — distinct vocabulary may describe a comparable role.
4. PARENT_CHILD_CANDIDATE — one concept may contain or specialize another.
5. IMPLEMENTATION_SPECIFIC — provider, runtime, or domain-bound concept.
6. UNRESOLVED — evidence insufficient for equivalence.

## Required evidence for promotion

A candidate relation cannot become canonical equivalence until all seven conditions are met:

1. Definition match.
2. Operational-role match.
3. Boundary/ownership compatibility.
4. Lifecycle compatibility where lifecycle is material.
5. Direct source evidence supporting the mapping.
6. At least one counterexample or adversarial non-equivalence test survives.
7. Scope, version, and domain are explicitly bounded.

## Current cross-project candidate mappings

| Family | Candidate relation | Boundary |
|---|---|---|
| Intent/request | Different terms, potentially equivalent upstream role | Creator brief, agent task, and live-session configuration remain different schemas. |
| Semantic contract/model | Different terms, partially equivalent role | EVO media IR is not a universal agent/task ontology; CCH-OS L0-L7 is not automatically TENTOR HOS layering. |
| Capability | Shared architectural role, different granularity | Workflow stage, capability, domain service, and platform feature must remain distinct. |
| Provider/adapter/tool | Shared implementation role candidate | A provider is not a capability, authority, or operational proof. |
| Authority/policy/approval | Shared governance role candidate | Technical availability does not imply consent, authorization, or compliance. |
| Execution/orchestration | Overlapping role, different temporal semantics | Linear production, compiler execution, and live sessions are not interchangeable. |
| State/history/event/trace | Related lifecycle concepts, not one object | Current state, historical record, audit event, job, session, and trace require explicit boundaries. |
| Evidence/provenance/lineage | Shared traceability family | Design assertion, provider output, CI result, runtime observation, and independent audit have different evidentiary force. |
| Quality/acceptance | Shared governance function, different criteria | Content quality, technical conformance, safety, compliance, and production readiness remain separate gates. |
| Failure/fallback | Shared honesty principle candidate | A substitute is not exact fulfillment unless equivalence is validated and disclosed. |
| Evolution/promotion | Shared governance function candidate | Proposal, source-declared lock, approved design, implemented, tested, independently verified, and production accepted are distinct states. |

## Falsification controls

- Provider swap must not silently change a capability contract.
- Capability availability without authority must deny or hold with observable reason.
- A source-declared PASS without execution evidence must not become implementation verified.
- Reopening history must not silently regenerate external output.
- Fallback must distinguish exact fulfillment, substitute, and partial result.
- Missing source continuation must remain UNKNOWN, not reconstructed from a later version.
- Version-title inconsistency must not be treated as proof of supersession.

## Disposition

This gate strengthens the existing working crosswalk but does not accept any ontology term, equivalence, layer, or architecture as canonical TENTOR HOS V.2.

Next: use these rules while constructing the requirements-to-evidence matrix and counterexample set. Only after those gates should candidate architecture synthesis begin.
