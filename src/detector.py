from typing import Any

from rules import (
    CONFIDENTIAL_PHRASES,
    DETECTION_RULES,
    MEDICAL_PHRASES,
)


Detection = dict[str, Any]


def detect_sensitive_text(text: str) -> list[Detection]:
    """Return sensitive-information findings from the supplied text."""
    detections: list[Detection] = []

    for rule in DETECTION_RULES:
        for match in rule["pattern"].finditer(text):
            detections.append(
                {
                    "text": match.group(),
                    "category": rule["category"],
                    "start": match.start(),
                    "end": match.end(),
                    "placeholder": rule["placeholder"],
                    "severity": rule["severity"],
                    "explanation": rule["explanation"],
                }
            )

    detections.extend(
        detect_phrases(
            text=text,
            phrases=MEDICAL_PHRASES,
            category="MEDICAL_INFORMATION",
            placeholder="[MEDICAL_INFO]",
            severity="high",
            explanation=(
                "Medical information is sensitive personal information."
            ),
        )
    )

    detections.extend(
        detect_phrases(
            text=text,
            phrases=CONFIDENTIAL_PHRASES,
            category="CONFIDENTIAL_INFORMATION",
            placeholder="[CONFIDENTIAL_INFO]",
            severity="high",
            explanation=(
                "This phrase may reveal confidential organizational "
                "or project information."
            ),
        )
    )

    return remove_overlaps(detections)


def detect_phrases(
    text: str,
    phrases: set[str],
    category: str,
    placeholder: str,
    severity: str,
    explanation: str,
) -> list[Detection]:
    detections: list[Detection] = []
    lower_text = text.lower()

    for phrase in phrases:
        search_start = 0

        while True:
            start = lower_text.find(phrase, search_start)

            if start == -1:
                break

            end = start + len(phrase)

            detections.append(
                {
                    "text": text[start:end],
                    "category": category,
                    "start": start,
                    "end": end,
                    "placeholder": placeholder,
                    "severity": severity,
                    "explanation": explanation,
                }
            )

            search_start = end

    return detections


def remove_overlaps(
    detections: list[Detection],
) -> list[Detection]:
    """Keep the longest detection when character ranges overlap."""
    sorted_detections = sorted(
        detections,
        key=lambda item: (
            item["start"],
            -(item["end"] - item["start"]),
        ),
    )

    accepted: list[Detection] = []

    for detection in sorted_detections:
        overlaps = any(
            detection["start"] < existing["end"]
            and detection["end"] > existing["start"]
            for existing in accepted
        )

        if not overlaps:
            accepted.append(detection)

    return sorted(
        accepted,
        key=lambda item: item["start"],
    )
