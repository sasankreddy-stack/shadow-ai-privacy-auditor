# Project Reflection

## Project Summary

The Shadow AI Privacy Auditor is a web application designed to help users identify sensitive or confidential information before sharing text with public AI platforms such as ChatGPT, Gemini, or Copilot.

The application analyzes user-provided text, identifies potentially sensitive information, highlights risky content, explains why each item may be sensitive, and generates a safer redacted version. The project was built using Python and Streamlit with a focus on privacy, simplicity, and ease of use.

---

# What We Built

The application includes the following features:

- Text input for user-provided content
- Detection of multiple categories of sensitive information
- Visual highlighting of detected information
- Explanations for why each item may be risky
- Automatic generation of redacted text
- Risk scoring based on detected findings
- Fictional test cases to validate detection accuracy
- Safe examples that remain unchanged

The application was designed to satisfy all Tier 1 hackathon requirements.

---

# Technical Decisions

Python was selected because of its excellent support for text processing and regular expressions.

Streamlit was chosen because it provides a simple way to build and deploy an interactive web application without requiring separate frontend and backend development.

Regular expressions were used for structured information such as:

- Email addresses
- Phone numbers
- Social Security numbers
- Credit cards
- Passwords
- API keys
- Employee IDs

Keyword matching was used for:

- Medical information
- Confidential organizational information

This combination provided a lightweight solution that performs well without requiring external AI services.

---

# Challenges

Several challenges were encountered during development.

The primary challenge was balancing accurate detection while avoiding false positives. Broad keywords sometimes matched safe sentences, so more specific phrases were used whenever possible.

Another challenge was ensuring that only detected information was replaced while preserving all non-sensitive text.

Testing with both risky and safe examples helped improve reliability.

---

# Tradeoffs

To keep the application simple and reliable within the hackathon timeframe, several design decisions were made.

Instead of using a large language model or external AI provider, the application relies on regular expressions and keyword matching.

This approach offers:

- Faster execution
- Better privacy
- No API costs
- Simpler deployment

The tradeoff is that context-dependent confidential information may not always be detected.

---

# Responsible AI and Privacy

Privacy was a major design goal.

The application:

- Does not intentionally store user text
- Uses only fictional and synthetic test data
- Processes text only during analysis
- Avoids sending data to external AI providers

These decisions reduce privacy risks while demonstrating responsible AI practices.

---

# AI Tools Used

AI-assisted development tools were used to:

- Brainstorm the application design
- Improve documentation
- Generate sample fictional test cases
- Review code structure
- Refine regular expressions

All generated code and documentation were reviewed, tested, and modified before inclusion in the final project.

---

# Future Improvements

Possible future enhancements include:

- Browser extension
- PDF and document scanning
- OCR support for screenshots
- Multilingual detection
- Machine-learning-based entity recognition
- User-defined custom detection rules
- More advanced risk scoring

---

# Lessons Learned

This project demonstrated that a practical privacy auditing tool can be built using lightweight techniques such as regular expressions and keyword matching.

Building accurate detection requires careful testing with both risky and safe examples.

The project also reinforced the importance of protecting sensitive information before interacting with public AI systems.