# Shadow AI Privacy Auditor – Architecture

## Overview

Shadow AI Privacy Auditor is a Streamlit-based web application that helps users identify and redact sensitive information before sharing text with public AI platforms such as ChatGPT, Gemini, or Copilot.

The application analyzes text locally using regular expressions and keyword matching to identify sensitive information, highlights risky content, explains why it may be sensitive, and generates a safer redacted version.

---

# System Architecture

```
User
   │
   ▼
Streamlit Web Interface
   │
   ▼
Detection Engine
   ├── Regular Expressions
   ├── Medical Keyword Detection
   ├── Confidential Information Detection
   └── Employee Identifier Detection
   │
   ▼
Detection Results
   │
   ├── Risk Score
   ├── Highlighted Text
   ├── Detection Explanations
   └── Redacted Text
   │
   ▼
User Reviews Safe Output
```

---

# Detection Design

The application combines multiple detection techniques.

## Regular Expressions

Used for detecting:

- Email addresses
- Phone numbers
- Social Security numbers
- Credit card numbers
- Passwords
- API keys
- Employee IDs

Regular expressions provide accurate detection for structured patterns.

---

## Keyword Detection

Keyword and phrase matching detects:

- Medical information
- Confidential organizational information

Examples include:

- confidential
- internal use only
- acquisition plan
- medical record
- patient diagnosis

---

# Redaction Process

The application replaces detected information with placeholders.

Examples:

```
john@example.com
```

↓

```
[EMAIL]
```

```
EMP-2045
```

↓

```
[EMPLOYEE_ID]
```

Only detected entities are replaced to preserve the rest of the original text.

---

# Risk Scoring

Each finding contributes to an overall risk score.

Severity levels:

- Low
- Medium
- High

The total score helps users quickly assess whether the text is safe to share.

---

# Privacy Design

The application is designed with privacy in mind.

- User text is processed only during analysis.
- No user text is intentionally stored.
- No databases are used.
- Only fictional and synthetic test cases are included.

---

# Limitations

Current limitations include:

- English-language support only.
- Keyword-based confidential detection may miss context-specific information.
- Name detection is limited compared to enterprise NER solutions.
- Images and documents are not analyzed.

---

# Future Improvements

Future enhancements may include:

- Browser extension
- PDF scanning
- OCR support
- Multilingual detection
- Machine-learning-based entity detection
- Custom detection rules