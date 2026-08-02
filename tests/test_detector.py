import json
import sys
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC_DIR = PROJECT_ROOT / "src"

sys.path.insert(0, str(SRC_DIR))

from detector import detect_sensitive_text  # noqa: E402
from redactor import redact_text  # noqa: E402


def load_test_cases() -> list[dict]:
    test_file = PROJECT_ROOT / "tests" / "test_cases.json"

    with test_file.open("r", encoding="utf-8") as file:
        return json.load(file)


def test_expected_categories() -> None:
    for case in load_test_cases():
        detections = detect_sensitive_text(case["input"])

        actual_categories = {
            item["category"]
            for item in detections
        }

        for expected_category in case["expected_categories"]:
            assert expected_category in actual_categories, (
                f"Case {case['id']} failed. "
                f"Expected {expected_category}, "
                f"but found {actual_categories}"
            )


def test_safe_examples_remain_unchanged() -> None:
    for case in load_test_cases():
        if not case["safe_text"]:
            continue

        detections = detect_sensitive_text(case["input"])
        redacted = redact_text(case["input"], detections)

        assert detections == [], (
            f"Safe case {case['id']} produced detections: {detections}"
        )

        assert redacted == case["input"], (
            f"Safe case {case['id']} was changed."
        )
