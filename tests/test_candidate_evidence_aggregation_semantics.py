"""Synthetic candidate evidence aggregation semantics test harness.

Non-normative. This file tests candidate rules only; it is not production gate logic.
"""

from dataclasses import dataclass
from enum import Enum


class State(str, Enum):
    INVALID = "INVALID"
    NOT_APPLICABLE = "NOT_APPLICABLE"
    INSUFFICIENT = "INSUFFICIENT"
    STALE_OR_MISMATCHED = "STALE_OR_MISMATCHED"
    CONFLICTED = "CONFLICTED"
    FAIL = "FAIL"
    PASS = "PASS"
    BLOCKED = "BLOCKED"
    NOT_RUN = "NOT_RUN"
    INCONCLUSIVE = "INCONCLUSIVE"


@dataclass(frozen=True)
class Evidence:
    state: State
    mandatory: bool = True


def resolve_gate(evidence):
    mandatory = [e.state for e in evidence if e.mandatory]
    if not mandatory:
        return "UNSCOPED"
    if State.FAIL in mandatory:
        return "FAIL"
    if State.BLOCKED in mandatory:
        return "BLOCKED"
    if State.INCONCLUSIVE in mandatory or State.CONFLICTED in mandatory:
        return "INCONCLUSIVE"
    if State.NOT_RUN in mandatory:
        return "NOT_RUN"
    if all(s == State.PASS for s in mandatory):
        return "PASS"
    return "INCONCLUSIVE"


def run_case(name, evidence, expected):
    actual = resolve_gate(evidence)
    if actual != expected:
        raise AssertionError(f"{name}: expected {expected}, got {actual}")
    print(f"PASS {name}: {actual}")


def main():
    cases = [
        ("mandatory fail dominates", [Evidence(State.PASS), Evidence(State.FAIL)], "FAIL"),
        ("blocked without failure", [Evidence(State.PASS), Evidence(State.BLOCKED)], "BLOCKED"),
        ("inconclusive without failure/block", [Evidence(State.PASS), Evidence(State.INCONCLUSIVE)], "INCONCLUSIVE"),
        ("conflict blocks promotion", [Evidence(State.PASS), Evidence(State.CONFLICTED)], "INCONCLUSIVE"),
        ("not run remains not run", [Evidence(State.PASS), Evidence(State.NOT_RUN)], "NOT_RUN"),
        ("all mandatory pass", [Evidence(State.PASS), Evidence(State.PASS)], "PASS"),
        ("optional failure does not fail mandatory gate", [Evidence(State.PASS), Evidence(State.FAIL, mandatory=False)], "PASS"),
        ("no mandatory criteria is unscoped", [Evidence(State.PASS, mandatory=False)], "UNSCOPED"),
        ("invalid evidence cannot become pass", [Evidence(State.INVALID)], "INCONCLUSIVE"),
        ("blocked plus fail remains fail", [Evidence(State.BLOCKED), Evidence(State.FAIL)], "FAIL"),
    ]
    for name, evidence, expected in cases:
        run_case(name, evidence, expected)
    print("Candidate aggregation semantics: 10/10 synthetic expectations passed.")
    print("LIMIT: synthetic policy execution only; no canonical gate, authenticity, or production conformance is established.")


if __name__ == "__main__":
    main()
