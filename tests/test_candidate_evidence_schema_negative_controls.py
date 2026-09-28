#!/usr/bin/env python3
"""Negative controls for the candidate evidence schema harness.

Synthetic controls only; they do not validate evidence authenticity or TENTOR HOS runtime.
"""
import json
from pathlib import Path

from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[1]
SCHEMA_PATH = ROOT / "schemas/candidate/evidence-record-v0.1.schema.json"
FIXTURES_PATH = ROOT / "tests/fixtures/candidate-evidence-record-fixtures-v0.1.json"


def main() -> int:
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    fixture_set = json.loads(FIXTURES_PATH.read_text(encoding="utf-8"))
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    cases = fixture_set["cases"]
    failures = []

    # Negative control A: deliberately invert the expectation for a valid record.
    valid_case = next(c for c in cases if c["expected_schema_valid"] is True)
    actual_valid = not list(validator.iter_errors(valid_case["record"]))
    deliberately_wrong_expectation = not actual_valid
    if actual_valid == deliberately_wrong_expectation:
        failures.append("negative control A: inverted expectation was not detected")
    else:
        print("PASS negative control A: inverted expectation produces mismatch")

    # Negative control B: remove a mandatory field from a valid synthetic record.
    mutated = json.loads(json.dumps(valid_case["record"]))
    mutated.pop("record_id", None)
    mutation_valid = not list(validator.iter_errors(mutated))
    if mutation_valid:
        failures.append("negative control B: missing required record_id was accepted")
    else:
        print("PASS negative control B: removal of required record_id is rejected")

    # Negative control C: add an undeclared property; schema must reject closed objects.
    mutated = json.loads(json.dumps(valid_case["record"]))
    mutated["unrecognized_control_field"] = "unexpected"
    mutation_valid = not list(validator.iter_errors(mutated))
    if mutation_valid:
        failures.append("negative control C: undeclared root property was accepted")
    else:
        print("PASS negative control C: undeclared root property is rejected")

    print(f"Negative control summary: {3 - len(failures)}/3 passed")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
