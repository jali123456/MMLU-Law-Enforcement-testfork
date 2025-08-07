# 🔒 Law Enforcement MMLU Dataset

Welcome to the official repository of the **Law Enforcement Massive Multitask Language Understanding (MMLU)** dataset. This open-source initiative aims to benchmark large language models (LLMs) and human performance across a wide array of enforcement domains including criminal law, investigative procedures, digital forensics, and ethical enforcement conduct.

---

## 🌎 Purpose

To provide a high-quality, peer-reviewed benchmark to evaluate reasoning, recall, and decision-making abilities of both AI systems and professionals within the law enforcement ecosystem. This dataset will also be used to compare the performance of different LLMs — including our proprietary system, ELMU Insights.Akta.

---

## 📚 Dataset Overview

- **Format**: JSON Lines (.jsonl)  
- **Type**: Multiple Choice Questions (MCQs)  
- **Domains Covered**:
  - Criminal Procedure Code (CPC)
  - Penal Code
  - Evidence Act
  - Police SOPs
  - AML/CFT
  - Cybercrime Laws
  - Forensics & Investigation  
- **Metadata Tags**:
  - `category`
  - `difficulty`
  - `reference`
  - `explanation`

---

## 🔢 Sample Entry

```json
{
  "id": "LE001",
  "question": "Under Malaysian CPC, what is the maximum remand period a Magistrate can grant for a serious offence?",
  "options": ["7 days", "14 days", "15 days", "21 days"],
  "answer": "15 days",
  "category": "Criminal Procedure",
  "difficulty": "Advanced",
  "reference": "Section 117 CPC",
  "explanation": "For serious offences, the remand can be extended up to 15 days."
}
```
---

## 🚀 Getting Started

1. Fork this repository  
2. Read the [CONTRIBUTING.md](CONTRIBUTING.md) for formatting rules and submission guidelines  
3. Use the provided `sample_question.jsonl` to begin drafting your contributions  
4. Submit a pull request for review  

---

## 👥 Community

Join our discussion board via GitHub or our contributor Slack (invite in [`CONTRIBUTING.md`](CONTRIBUTING.md)).  
We also run periodic **MMLU Data Jams** where contributors co-create and review questions live.

---

## ✅ License

This project is licensed under the **MIT License**.  
Attribution required when reusing the dataset.

---

## ✨ Roadmap

- [x] Prepare repository structure
- [x] Draft contribution guidelines
- [ ] Launch contributor campaign
- [ ] Reach 500 validated questions across 10 categories
- [ ] Release v1.0 dataset
- [ ] Integrate with ELMU Insights.Akta for evaluation
- [ ] Publish benchmark report comparing LLMs

---

## Feedback

Suggestions and opinions (both positive and negative) are greatly welcome. 
Please contact us by sending email to [elmu.ai@elmu.edu.my](mailto:elmu.ai@elmu.edu.my).


