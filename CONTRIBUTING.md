# ✍️ Contributing to the Law Enforcement MMLU Dataset

Thank you for your interest in contributing!  
Our mission is to create a high-quality benchmark that reflects the complexity and standards of global law enforcement.

---

## ♻️ Contribution Workflow

1. Fork this repository  
2. Create a new branch: `feature/your-topic`  
3. Add questions to `dataset/questions.jsonl`  
4. Ensure format follows the schema below  
5. Submit a Pull Request with the label `new-question`  

---

## 📚 Question Format

```json
{
  "id": "LE002",
  "question": "Who may file a First Information Report under Section 107 CPC Malaysia?",
  "options": ["Only Police Officers", "Any Person", "Only the Victim", "A Judge"],
  "answer": "Any Person",
  "category": "Criminal Procedure",
  "difficulty": "Intermediate",
  "reference": "Section 107, CPC Malaysia",
  "explanation": "The law permits any person with knowledge of a cognizable offence to initiate an FIR."
}
```

---

## ✏️ Guidelines

To maintain the quality and consistency of the Law Enforcement MMLU Dataset, please follow these guidelines:

### ✅ Question Writing

- Use clear, concise, and **neutral language** (avoid bias or ambiguity)
- Questions must have **one correct answer** only
- Avoid overly technical jargon unless it is necessary and widely understood in the domain

### 🧠 Answer Choices (Options)

- Include **four options** per question
- Distractors (incorrect answers) must be **plausible**, not obviously incorrect
- Ensure no two options are **too similar** or **overlapping in meaning**

### 🏛 Legal and Domain References

- Cite **publicly available** or officially published legal references (e.g. Penal Code, CPC, Evidence Act, SOPs)
- When referencing internal manuals or enforcement guidelines, ensure they are **non-confidential and accessible**

### 🏷 Metadata Labelling

- **Category**: Choose the appropriate domain (e.g., Cybercrime, Criminal Procedure, AML/CFT)
- **Difficulty**: Label as `Basic`, `Intermediate`, or `Advanced`
- **Reference**: Specify the act, section, or source (e.g., "Section 117 CPC")
- **Explanation**: Provide a short, factual justification for the correct answer

### ❌ Common Mistakes to Avoid

- Using outdated or repealed laws  
- Writing questions that are too opinion-based  
- Reusing the same correct answer too often  
- Including explanations that simply restate the question  

---

## ✅ Validation Checklist

Use this checklist before submitting your question:

- [ ] Question is original and clearly written  
- [ ] Includes exactly four answer choices  
- [ ] Correct answer is clearly marked  
- [ ] Explanation is informative and accurate  
- [ ] Metadata (category, difficulty, reference) is complete  
- [ ] JSON syntax is valid and properly formatted  

---

## 📅 Community

- Submit questions or issues via [GitHub Issues](../../issues)  
- Join our Contributor Slack or attend MMLU Data Jams  
- Top contributors may be invited to the review board
