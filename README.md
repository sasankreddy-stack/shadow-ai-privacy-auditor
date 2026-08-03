# Shadow AI Privacy Auditor

**Live Demo:** https://shadow-ai-privacy-auditor-gakjwy6zaqvetiw52pbtgv.streamlit.app/

**Walkthrough Video:**  https://youtu.be/mZY2m2dKmQk

## Overview

Shadow AI Privacy Auditor is a Streamlit web application that helps users identify and redact sensitive or confidential information before sharing text with public AI platforms such as ChatGPT, Gemini, or Copilot.

The application analyzes user-provided text, highlights sensitive information, explains potential privacy risks, and generates a safer redacted version while preserving non-sensitive content.

---

## Features

- Detects multiple categories of sensitive information
- Highlights detected content
- Explains why each finding may be risky
- Generates a redacted version of the text
- Calculates an overall risk score
- Preserves safe text that should not be redacted
- Includes fictional test cases and automated tests

---

## Technologies Used

- Python
- Streamlit
- Regular Expressions (Regex)
- Pytest

---

## Installation

Clone the repository:

```bash
git clone https://github.com/sasankreddy-stack/shadow-ai-privacy-auditor.git
```

Move into the project:

```bash
cd shadow-ai-privacy-auditor
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run src/app.py
```

---

## Project Structure

```text
shadow-ai-privacy-auditor/
├── docs/
├── planning/
├── src/
├── tests/
├── README.md
├── problem_statement.md
└── requirements.txt
```

---

## Testing

Run the automated tests:

```bash
python -m pytest
```

The project also includes fictional manual test cases to verify:

- Sensitive information detection
- Redaction
- Safe text preservation

---

## Privacy

This application is designed for fictional and synthetic data only.

It does not intentionally store user-submitted text or send it to external AI providers.

---

## Known Limitations

- English-language support only
- Regex and keyword detection may not identify all context-dependent confidential information
- Images and PDF files are not analyzed

---

## Future Improvements

- Browser extension
- PDF scanning
- OCR support
- Multilingual detection
- Machine-learning-based entity recognition
- Custom detection rules

---

## Hackathon Submission Checklist

- ✅ Planning document
- ✅ Working application
- ✅ Architecture documentation
- ✅ Reflection documentation
- ✅ Fictional test cases
- ✅ Live deployment URL
- ✅ Walkthrough video
