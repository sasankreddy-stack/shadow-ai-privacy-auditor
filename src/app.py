import html
from typing import Any

import streamlit as st

from detector import detect_sensitive_text
from redactor import redact_text
from risk_score import calculate_risk_score


st.set_page_config(
    page_title="Shadow AI Privacy Auditor",
    page_icon="🛡️",
    layout="wide",
)


def create_highlighted_html(
    text: str,
    detections: list[dict[str, Any]],
) -> str:
    parts: list[str] = []
    cursor = 0

    for detection in detections:
        start = detection["start"]
        end = detection["end"]

        parts.append(html.escape(text[cursor:start]))

        detected_text = html.escape(text[start:end])
        category = html.escape(detection["category"])

        parts.append(
            "<mark style='padding: 2px 5px; "
            "border-radius: 4px;' "
            f"title='{category}'>"
            f"{detected_text}"
            "</mark>"
        )

        cursor = end

    parts.append(html.escape(text[cursor:]))

    return "".join(parts)


st.title("🛡️ Shadow AI Privacy Auditor")

st.write(
    "Review text for sensitive or confidential information before "
    "sharing it with a public AI tool."
)

st.info(
    "This prototype is designed for fictional and synthetic data only. "
    "Submitted text is not intentionally stored."
)

sample_text = (
    "Contact the fictional employee at jordan.lee@example.com or "
    "203-555-0147. Employee ID EMP-2045 is connected to the "
    "confidential acquisition plan. The sample password=DemoPass123."
)

if "input_text" not in st.session_state:
    st.session_state.input_text = ""

text = st.text_area(
    "Paste or type the text you want to review",
    key="input_text",
    height=220,
    placeholder="Enter text here...",
)

button_col1, button_col2, button_col3 = st.columns(3)

with button_col1:
    analyze_clicked = st.button(
        "Analyze Text",
        type="primary",
        use_container_width=True,
    )

with button_col2:
    if st.button(
        "Load Fictional Example",
        use_container_width=True,
    ):
        st.session_state.input_text = sample_text
        st.rerun()

with button_col3:
    if st.button(
        "Clear",
        use_container_width=True,
    ):
        st.session_state.input_text = ""
        st.rerun()

if analyze_clicked:
    if not text.strip():
        st.warning("Enter some text before running the privacy review.")
    else:
        detections = detect_sensitive_text(text)
        redacted_text = redact_text(text, detections)
        risk_score, risk_level = calculate_risk_score(detections)

        st.divider()
        st.subheader("Privacy Review Results")

        metric_col1, metric_col2, metric_col3 = st.columns(3)

        metric_col1.metric("Risk Score", f"{risk_score}/100")
        metric_col2.metric("Risk Level", risk_level)
        metric_col3.metric("Findings", len(detections))

        if not detections:
            st.success(
                "No supported sensitive information was detected. "
                "The text remains unchanged."
            )

            st.subheader("Reviewed Text")
            st.code(text, language=None)
        else:
            st.warning(
                f"{len(detections)} potentially sensitive item(s) "
                "were detected."
            )

            st.subheader("Highlighted Original Text")

            highlighted_text = create_highlighted_html(
                text,
                detections,
            )

            st.markdown(
                f"""
                <div style="
                    border: 1px solid #888;
                    border-radius: 8px;
                    padding: 16px;
                    line-height: 1.8;
                    white-space: pre-wrap;
                ">
                    {highlighted_text}
                </div>
                """,
                unsafe_allow_html=True,
            )

            st.subheader("Detected Information")

            for number, detection in enumerate(
                detections,
                start=1,
            ):
                label = (
                    f"{number}. {detection['category']} — "
                    f"{detection['severity'].title()} Risk"
                )

                with st.expander(label):
                    st.write(
                        f"**Detected:** `{detection['text']}`"
                    )
                    st.write(
                        "**Why it may be risky:** "
                        f"{detection['explanation']}"
                    )
                    st.write(
                        "**Redaction:** "
                        f"`{detection['placeholder']}`"
                    )

            st.subheader("Safer Redacted Text")

            st.text_area(
                "Review and copy the safer version",
                value=redacted_text,
                height=180,
            )

            st.download_button(
                "Download Safe Text",
                data=redacted_text,
                file_name="redacted_text.txt",
                mime="text/plain",
            )
