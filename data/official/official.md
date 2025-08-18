# 📁 Official Question Depository

This section contains the **official and verified** multiple-choice questions (MCQs) contributed to the MMLU Law Enforcement project. These questions form the core dataset used to evaluate and fine-tune various LLMs for law enforcement, legal, and governance applications.

All questions in this depository have been reviewed and validated by Subject Matter Experts (SMEs) from enforcement, legal, and academic backgrounds.

---

## 📌 Dataset Overview

- **Total Questions (v0.1)**: 287
- **Format**: `.jsonl` and `.xlsx`
- **Language Support**: English
- **Tags**: Category, Difficulty Level, Act & Section Reference, Explanation
- **Review Status**: SME Verified ✅

Each item in the dataset follows this structure:

```json
{
  "id": "LE0001",
  "question": "A Chief Executive directs a person to produce a document, but the document is not in that person's custody. What is the person required to do?",
  "options": [
    "Ignore the directive",
    "Inform the Chief Executive and take steps to obtain the document",
    "Pay a fine",
    "Serve imprisonment for a term not exceeding three years"
  ],
  "answer": "B) Inform the Chief Executive and take steps to obtain the document",
  "category": "Knowledge-based",
  "difficulty": "Basic",
  "reference": "Section 14(2) Cyber Security Act 2024 (Act 854)",
  "explanation": "According to the Cyber Security Act, the person must inform the Chief Executive that they do not have custody and take reasonable steps to obtain the document.",
  "language": "en",
  "review_status": "approved",
  "reviewer": "SME",
  "date_reviewed": "2025-04-22"
}
```

---

## ⚠️ Contributions

- **Only verified questions are listed here.**
- Community-contributed questions must go through review before being included here. Please refer to ![CONTRIBUTING.md](CONTRIBUTING.md) for submission guidelines.

---

## 🧠 Use Case

This official set is used for:
- Zero-shot benchmarking of LLMs
- Fine-tuning experiments for Malaysia-specific law enforcement tasks.
- Serving as a ground truth corpus for validation and training.

---

## 🔄 Updates

This dataset is versioned. As more SME-approved questions are added, this file and associated metadata will be updated. Please refer to the changelog below.

### **Changelog**

- v0.1 (2025-08-15): Initial upload of 287 verified questions.
