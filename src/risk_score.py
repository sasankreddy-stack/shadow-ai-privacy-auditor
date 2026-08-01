from typing import Any


SEVERITY_POINTS = {
    "low": 5,
    "medium": 15,
    "high": 30,
}


def calculate_risk_score(
    detections: list[dict[str, Any]],
) -> tuple[int, str]:
    score = sum(
        SEVERITY_POINTS.get(item["severity"], 0)
        for item in detections
    )

    score = min(score, 100)

    if score >= 60:
        level = "High"
    elif score >= 25:
        level = "Medium"
    else:
        level = "Low"

    return score, level
