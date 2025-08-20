# 🏆 MMLU Law Enforcement Leaderboard

This leaderboard showcases the performance of various Language Models (LLMs) tested using the MMLU-Law-Enforcement dataset in a **zero-shot setting**.

These results help benchmark the capability of each model in answering Malaysian law enforcement-related multiple-choice questions (MCQs) without prior fine-tuning.

---

## 📊 Evaluation Results

| Run Date       | Model                | Language       | Total Questions | Correct | Accuracy (%) |
|----------------|----------------------|----------------|------------------|---------|---------------|
| 07-May-2025    | ELMU Insights         | English        | 29               | 19      | 65.5%         |
| 20-May-2025    | ELMU Insights         | English        | 100              | 86      | 86.0%         |
| 25-June-2025   | ELMU Insights         | Bahasa Melayu  | 100              | 97      | 97.0%         |
| 09-July-2025   | ELMU Insights         | English        | 100              | 99      | 99.0%         |
| 09-July-2025   | ChatGPT              | English        | 100              | 97      | 97.0%         |
| 09-July-2025   | Claude               | English        | 100              | 97      | 97.0%         |
| 09-July-2025   | ChatGPT              | Bahasa Melayu  | 100              | 98      | 98.0%         |
| 09-July-2025   | Claude               | Bahasa Melayu  | 100              | 94      | 94.0%         |

---

## 📥 How to Submit Your Model

Want to test your own model?

1. Download the evaluation dataset from [`evaluations/`](../../evaluations/)
2. Run your model on the questions (zero-shot, no fine-tuning)
3. Format your results with the following fields:
   - `model_name`, `date`, `language`, `total_questions`, `correct`, `accuracy`
4. Submit a Pull Request (PR) with your results in a `.json` or `.md` file
5. Your model’s score will appear in the next leaderboard update

---

## 📌 Notes

- All evaluations are performed using **zero-shot prompting**
- The dataset will grow over time — accuracy is relative to versioned releases
- Models are tested **without additional plugins or fine-tuning**

---

## 🧠 Why This Matters

This leaderboard helps researchers, enforcement practitioners, and LLM developers:
- Benchmark their models on localized, real-world legal content
- Compare multilingual performance (English vs Bahasa Melayu)
- Understand the current state-of-the-art in law enforcement QA tasks

Join us in improving legal intelligence with better data 🚔📈

