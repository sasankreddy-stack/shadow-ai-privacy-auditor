# Planning Document

Complete this document before writing any code. This is part of the evaluation. Your intent here will be compared against what you actually built in `docs/architecture.md`.

---

# Tech Stack

### Framework / Language

* **Python 3**
* **Streamlit** (Web Application Framework)

### Why did you choose this stack?

I chose Python because it provides excellent support for text processing, regular expressions, and natural language processing libraries. Streamlit allows rapid development of a clean web interface without requiring separate frontend and backend frameworks. This lets me focus on building an accurate detection engine while still delivering a polished application within the hackathon timeline.

---

### Key Libraries

* **Streamlit** – Web interface
* **re (Regular Expressions)** – Detect structured sensitive information
* **spaCy** – Named Entity Recognition (NER) for detecting person names
* **Pytest** – Automated testing
* **JSON** – Store fictional test cases

---

### Detection Approach / AI Provider (if any)

The application will use a **combination** of techniques rather than relying on a single AI model.

* Regular Expressions
* Keyword and phrase matching
* spaCy Named Entity Recognition (NER)

No external AI provider will be used in the initial implementation. This keeps the application simple, fast, private, and free from API costs.

Detection results from all methods will be combined, duplicate findings removed, and then displayed to the user with explanations and redacted output.

---

# Detection Categories

| Category                                           | Detect? | Planned Technique                                                                                                                                |
| -------------------------------------------------- | :-----: | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| Names & contact information                        |   Yes   | spaCy NER for names; Regular Expressions for email addresses and phone numbers                                                                   |
| Government or financial identifiers                |   Yes   | Regular Expressions for Social Security numbers, credit card numbers, and similar identifiers                                                    |
| Passwords, API keys or credentials                 |   Yes   | Regular Expressions for passwords, API keys, bearer tokens, GitHub tokens, AWS keys, and OpenAI keys                                             |
| Medical or sensitive personal information          |   Yes   | Keyword and phrase matching for diseases, diagnoses, prescriptions, and patient information                                                      |
| Employee, client or volunteer information          |   Yes   | Regular Expressions and contextual keywords for employee IDs, client IDs, payroll information, and volunteer identifiers                         |
| Confidential organizational or project information |   Yes   | Keyword and phrase matching for confidential, internal use only, roadmap, acquisition, merger, source code, project codenames, and similar terms |

---

# Phases & Priorities

The project will be developed in three phases.

| Phase       | Target Dates | Goals                                                                                                                                               |
| ----------- | ------------ | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Phase 1** | Day 1        | Complete planning document, create project structure, implement regex detection engine, implement redaction functionality                           |
| **Phase 2** | Days 2–3     | Build Streamlit interface, add highlighting, explanations, risk scoring, copy safe text button, and spaCy name detection                            |
| **Phase 3** | Days 4–5     | Test with fictional examples, reduce false positives, deploy application, complete documentation, record walkthrough video, and finalize submission |

### Build Priority

1. Detection Engine
2. Redaction Engine
3. Testing
4. User Interface
5. Documentation
6. Deployment

The detection engine will be built first because it is the core functionality required by the challenge.

---

# What I'll Cut If Time Is Short

The following stretch goals will be removed first if necessary:

* Browser extension
* Multilingual support
* Real-time monitoring while typing
* Custom user-defined detection rules
* Undo individual redactions

The last feature I would remove is risk scoring because it improves usability but is not required for Tier 1.

The core features that will always remain are:

* Sensitive information detection
* Highlighting
* Explanations
* Redacted text generation
* Safe-text preservation
* Fictional test cases
* Working deployment

---

# Open Questions / Risks

### False Positives

Safe sentences may accidentally be detected as sensitive.

**Mitigation:** Use specific keyword phrases instead of broad keywords and include safe test cases during development.

---

### False Negatives

Some confidential information depends on organizational context and may not be detected.

**Mitigation:** Clearly document this limitation and allow users to review all findings before sharing text.

---

### Name Detection

Named Entity Recognition may occasionally miss names or incorrectly identify non-name words.

**Mitigation:** Use spaCy NER and present detections as recommendations for user review.

---

### Overlapping Matches

A piece of text may match multiple detection rules.

**Mitigation:** Remove duplicate and overlapping detections before highlighting and redaction.

---

### Deployment

spaCy models increase deployment size and may create deployment issues.

**Mitigation:** Test deployment early and allow the application to continue using regex and keyword detection if the spaCy model is unavailable.

---

### Privacy

The application must not store user-submitted text.

**Mitigation:** All processing will occur only during analysis. No user data will be intentionally saved, logged, or shared. Only fictional or synthetic examples will be used for testing.

---

### Success Criteria

The project will be considered successful if it:

* Detects all required categories accurately.
* Highlights detected sensitive information.
* Explains why each finding may be risky.
* Generates a clean redacted version of the text.
* Does not unnecessarily redact safe text.
* Includes at least 10 fictional test cases.
* Is successfully deployed with a live URL.
* Meets all Tier 1 hackathon submission requirements.
