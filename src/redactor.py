from typing import Any


def redact_text(
    text: str,
    detections: list[dict[str, Any]],
) -> str:
    """Replace detected ranges without changing safe text."""
    redacted_text = text

    sorted_detections = sorted(
        detections,
        key=lambda item: item["start"],
        reverse=True,
    )

    for detection in sorted_detections:
        start = detection["start"]
        end = detection["end"]

        redacted_text = (
            redacted_text[:start]
            + detection["placeholder"]
            + redacted_text[end:]
        )

    return redacted_text
