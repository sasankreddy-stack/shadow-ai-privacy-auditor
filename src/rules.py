import re


DETECTION_RULES = [
    {
        "category": "EMAIL",
        "pattern": re.compile(
            r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"
        ),
        "placeholder": "[EMAIL]",
        "severity": "medium",
        "explanation": (
            "Email addresses can identify or provide direct contact "
            "information for an individual."
        ),
    },
    {
        "category": "PHONE",
        "pattern": re.compile(
            r"(?<!\d)(?:\+?1[-.\s]?)?"
            r"(?:\(?\d{3}\)?[-.\s]?)"
            r"\d{3}[-.\s]?\d{4}(?!\d)"
        ),
        "placeholder": "[PHONE]",
        "severity": "medium",
        "explanation": (
            "Phone numbers are personal contact information and should "
            "be reviewed before sharing."
        ),
    },
    {
        "category": "SSN",
        "pattern": re.compile(r"\b\d{3}-\d{2}-\d{4}\b"),
        "placeholder": "[SSN]",
        "severity": "high",
        "explanation": (
            "Social Security numbers are highly sensitive government "
            "identifiers."
        ),
    },
    {
        "category": "CREDIT_CARD",
        "pattern": re.compile(r"\b(?:\d[ -]*?){13,16}\b"),
        "placeholder": "[CREDIT_CARD]",
        "severity": "high",
        "explanation": (
            "This number resembles sensitive payment-card information."
        ),
    },
    {
        "category": "PASSWORD",
        "pattern": re.compile(
            r"\b(?:password|passwd|pwd)\s*[:=]\s*[^\s,;]{4,}",
            re.IGNORECASE,
        ),
        "placeholder": "[PASSWORD]",
        "severity": "high",
        "explanation": (
            "Passwords can provide unauthorized access to an account."
        ),
    },
    {
        "category": "API_KEY",
        "pattern": re.compile(
            r"\b(?:"
            r"sk-[A-Za-z0-9_-]{12,}"
            r"|ghp_[A-Za-z0-9]{20,}"
            r"|AKIA[A-Z0-9]{16}"
            r")\b"
        ),
        "placeholder": "[API_KEY]",
        "severity": "high",
        "explanation": (
            "API keys can provide unauthorized access to applications "
            "or cloud services."
        ),
    },
    {
        "category": "EMPLOYEE_ID",
        "pattern": re.compile(
            r"\b(?:EMP|EMPLOYEE|CLIENT|VOL)[-_ ]?\d{3,8}\b",
            re.IGNORECASE,
        ),
        "placeholder": "[EMPLOYEE_ID]",
        "severity": "medium",
        "explanation": (
            "Internal employee, client, or volunteer identifiers should "
            "not be shared publicly."
        ),
    },
]


CONFIDENTIAL_PHRASES = {
    "confidential",
    "internal use only",
    "project codename",
    "unreleased product",
    "acquisition plan",
    "merger plan",
    "trade secret",
    "private source code",
}


MEDICAL_PHRASES = {
    "medical diagnosis",
    "medical record",
    "patient diagnosis",
    "prescription medication",
    "diagnosed with diabetes",
    "diagnosed with cancer",
    "mental health diagnosis",
}
