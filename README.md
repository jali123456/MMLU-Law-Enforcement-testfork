# 🔒 Law Enforcement MMLU Dataset

Welcome to the official repository of the **Law Enforcement Massive Multitask Language Understanding (MMLU)** dataset. This open-source initiative aims to benchmark large language models (LLMs) and human performance across a wide array of enforcement domains including criminal law, investigative procedures, digital forensics, and ethical enforcement conduct.

---

## 🌎 Purpose

To provide a high-quality, peer-reviewed benchmark to evaluate reasoning, recall, and decision-making ability of both AI systems and professionals within the law enforcement and governance ecosystem.

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
