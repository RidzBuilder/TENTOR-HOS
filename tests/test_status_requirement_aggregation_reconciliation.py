"""Synthetic reconciliation tests for candidate requirement/result/lifecycle separation.

Non-normative. These tests exercise the reconciliation contract only.
"""


def assert_transition(name, result, transition, expected):
    allowed = {
        ("PASS", "TESTED"): True,
        ("PASS", "INDEPENDENTLY-VERIFIED"): False,
        ("PASS", "ACCEPTED-FOR-SCOPE"): False,
        ("BLOCKED", "ACCEPTED-FOR-SCOPE"): False,
        ("NOT_RUN", "TESTED"): False,
        ("SOURCE-DECLARED", "TESTED"): False,
        ("TESTED", "INDEPENDENTLY-VERIFIED"): True,
        ("INDEPENDENTLY-VERIFIED", "ACCEPTED-FOR-SCOPE"): True,
    }
    actual = allowed.get((result, transition), False)
    if actual != expected:
        raise AssertionError(f"{name}: expected {expected}, got {actual}")
    print(f"PASS {name}: {actual}")


def main():
    cases = [
        ("PASS can support TESTED when execution evidence exists", "PASS", "TESTED", True),
        ("PASS cannot itself prove independent verification", "PASS", "INDEPENDENTLY-VERIFIED", False),
        ("PASS cannot itself prove acceptance", "PASS", "ACCEPTED-FOR-SCOPE", False),
        ("BLOCKED cannot promote to acceptance", "BLOCKED", "ACCEPTED-FOR-SCOPE", False),
        ("NOT_RUN cannot become tested", "NOT_RUN", "TESTED", False),
        ("source declaration cannot become tested", "SOURCE-DECLARED", "TESTED", False),
        ("tested can enter independent verification gate", "TESTED", "INDEPENDENTLY-VERIFIED", True),
        ("independent verification can enter acceptance gate", "INDEPENDENTLY-VERIFIED", "ACCEPTED-FOR-SCOPE", True),
    ]
    for case in cases:
        assert_transition(*case)
    print("Status/result reconciliation: 8/8 synthetic expectations passed.")
    print("LIMIT: transition contract simulation only; no governance authority or runtime conformance is established.")


if __name__ == "__main__":
    main()
