# TENTOR HOS V.2 — Cross-Project Ontology Crosswalk v0.1 (Working)

**Date:** 2026-09-27  
**Gate:** S00-05 — cross-source reconciliation  
**Status:** WORKING CROSSWALK / NOT CANONICAL / NOT ACCEPTED

## 1. Purpose and rules

This crosswalk aligns terms only to expose similarities and non-equivalences across the supplied ACS, ACOS, ACPA, CCH-OS, EVO, and LCH-OS evidence. It does not declare a universal ontology. Source vocabulary retains its domain meaning. “Candidate relation” means a mapping to investigate, not equivalence.

Evidence references use the reviewed baseline IDs TH-EV-001–061; batch reviews 01–09 are indexed in `docs/evidence/EVIDENCE_REGISTRY_v0.1.md`.

## 2. Crosswalk

| Concept family | ACS / ACOS / ACPA usage | CCH-OS usage | EVO usage | LCH-OS / PBOS usage | Candidate relation | Non-equivalence / boundary |
|---|---|---|---|---|---|---|
| Intent / request | Product input, creator brief, content goal, client requirements | User intent and semantic request through staged pipeline | Input JSON/intent normalized to semantic IR | Creator/live-session goals and host configuration | User/domain intent is upstream of execution planning | A creator brief, arbitrary agent task, and live-session configuration are not interchangeable schemas. |
| Canonical semantic model | Blueprint, content contracts, production plan, agent I/O contracts | Ontology, semantic pipeline, architecture layers | Canonical media IR for scenes, segments, timeline, media and constraints | Persona, session, content and live-host models | Explicit domain model mediates between intent and execution | EVO media IR is not a universal agent/task ontology; CCH-OS L0–L7 is not accepted as TENTOR HOS layering. |
| Capability | Real motion video, product analysis, script/storyboard, content packaging | Capability abstraction separated from tool/adapter | Provider-neutral media capability contracts and resolver | Avatar/voice/live production and platform operations | Capability describes a required outcome/operation independently of a named provider | Granularity differs; output capability, workflow stage, and platform feature must not be conflated. |
| Provider / adapter / tool | Veo, HeyGen, Emergent and other engines/platforms as implementation choices | Adapters and external systems behind governed boundaries | Provider adapters compiled against capability contracts | Avatar/voice providers, platform APIs, live systems | Provider-specific integration realizes capability contracts | Provider is not capability, permission, or proof that an integration is operational. |
| Authority / policy | Human approval and product/content constraints | Authorization, policy, and human override boundaries | Constraints, governance and adapter eligibility | Consent, disclosure, moderation, platform/jurisdiction rules | Permission is evaluated separately from technical capability | A provider being callable does not imply consent, legal basis, platform compliance, or authorization. |
| Execution / orchestration | Production pipeline and generation workflow | Orchestration, runtime and stage execution | Compiler lifecycle, resolution, planning, compilation and execution | Live-session orchestration and control | Execution coordinates validated plans and capability invocation | Linear creator pipeline, compiler stages, and real-time live session have different temporal semantics. |
| State / history / event | Project/history records; restore should not regenerate | State, event, history, trace and recovery distinctions | Job state, idempotency, execution records | Session state and event stream | Durable state and event history need explicit separate models | History display, resumable job, audit event, and live session are not equivalent. |
| Evidence / provenance | Artifact, generation, acceptance, source and promotion evidence | Lineage, traceability, audit and conformance evidence | Diagnostics, mappings, execution provenance and gate status | Session records, consent/disclosure/compliance records | Evidence records should identify subject, method, scope, time, evaluator, result and limits | A design assertion, sample JSON, provider output, CI run, and independent audit have distinct evidentiary force. |
| Quality / acceptance | Product consistency, content requirements, playable real motion video, affiliate output quality | Stage/architecture conformance and adversarial checks | Schema/compiler/provider and E2E gates | Safety, disclosure, moderation and live-session constraints | Requirement-specific acceptance criteria and evidence are needed | Visual/content quality, technical conformance, safety compliance, and production readiness are separate gates. |
| Failure / fallback | Explicit provider failures and no false claim of successful video generation | Failure boundaries and remediation | Diagnostics, unresolved capability, compile/runtime errors | Provider/session interruptions and moderation outcomes | Typed failure and honest partial-result reporting | Fallback output cannot be represented as the requested capability unless equivalence is validated and disclosed. |
| Evolution / promotion | Pattern extraction and experiment promotion gates | Versioned architecture evolution and remediation | Versioned specifications, gate status, governance | Roadmap and platform/policy change handling | Controlled change with provenance, impact, approval and regression evidence | Roadmap status, source-declared lock, and implemented/verified change are not equivalent. |

## 3. Provisional ontology layers for analysis only

These are crosswalk groupings, not a proposed canonical layer stack:

1. **Intent and domain context** — request, actor, objective, domain-specific inputs and constraints.
2. **Semantic contract** — normalized domain entities, required outcomes, invariants and acceptance conditions.
3. **Authority and governance** — identity, permission, consent, policy, resource limits and approval.
4. **Capability and implementation catalog** — capability contracts, providers, adapters, tools, versions and eligibility.
5. **Planning and execution** — plans, orchestration, jobs/sessions, state transitions and invocation.
6. **Evidence and evaluation** — provenance, trace, artifact, tests, evaluator, result and limitations.
7. **Evolution and recovery** — remediation, migration, rollback, promotion, deprecation and regression evidence.

No source is assumed to contain or implement these groupings in this exact structure. Validate against counterexamples before considering a canonical model.

## 4. Required counterexamples and falsification tests

- **Intent/semantic boundary:** same user intent with different domain schemas; determine what is invariant and what remains domain-specific.
- **Capability/provider separation:** provider changes while capability contract remains; test semantic output equivalence and explicitly report non-equivalence.
- **Authority separation:** technically available provider but absent permission/consent; execution must deny or hold with observable reason.
- **Evidence maturity:** specification says PASS but no test run exists; gate must not report implementation verified.
- **State/history distinction:** reopen prior result; must not silently trigger a new provider generation unless explicitly requested.
- **Fallback honesty:** primary capability unavailable; system must distinguish substitute, partial result, and exact fulfillment.
- **Domain boundary:** creator video workflow versus live session, generic task agent, or security agent; reject forced ontology mappings where semantics differ.
- **Evolution governance:** proposed change with no source lineage, impact analysis, approval, or regression test must not be promoted.

## 5. Open issues

- OX-01: canonical actor/identity/tenant/workspace/project/environment ontology.
- OX-02: common requirement, capability, operation, provider, adapter, and tool definitions with domain-specific extensions.
- OX-03: cross-project evidence record and maturity semantics.
- OX-04: authority, consent, policy, approval, and override semantics.
- OX-05: state, event, history, job, session, trace, and artifact lifecycle.
- OX-06: media/content quality versus technical, safety, compliance, and production acceptance.
- OX-07: mapping to AOS/Universe/Multiverse concepts remains unapproved pending operational definitions and countermodels.

## 6. Disposition

This is a working analytical crosswalk only. No equivalence, canonical term, layer, architecture, or TENTOR HOS requirement is accepted. Each future specification clause must cite source evidence and be independently assigned a normative status and acceptance test.
