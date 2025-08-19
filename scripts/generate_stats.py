import json
from collections import Counter
import os

# Path to the official dataset
INPUT_FILE = "../data/official/mmlu_law_enforcement_official_v0.1.jsonl"
OUTPUT_FILE = "../data/official/stats.json"

def main():
    total_questions = 0
    category_counter = Counter()
    difficulty_counter = Counter()
    
    if not os.path.exists(INPUT_FILE):
        print(f"Input file not found: {INPUT_FILE}")
        return

    with open(INPUT_FILE, 'r', encoding='utf-8') as f:
        for line in f:
            data = json.loads(line)
            total_questions += 1
            category_counter[data.get("category", "Unknown")] += 1
            difficulty_counter[data.get("difficulty", "Unknown")] += 1

    stats = {
        "total_questions": total_questions,
        "category_breakdown": category_counter,
        "difficulty_breakdown": difficulty_counter
    }

    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        json.dump(stats, f, indent=4)

    print(f"✅ Stats written to {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
