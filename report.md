# 📝 Report: CLI Assistant – Fine-tuning a Compact LLM for Command-Line Help

## 📂 Data Source

* **Source**: [StackExchange Data Explorer](https://data.stackexchange.com/)
* **Query**:
  Extracted \~150 high-quality Bash/Git/Grep Q\&A pairs using SQL from accepted answers on Stack Overflow.

  ```sql
  SELECT TOP 150
    Posts.Title,
    Posts.Body,
    Answers.Body AS Answer
  FROM Posts
  JOIN Posts AS Answers ON Posts.AcceptedAnswerId = Answers.Id
  WHERE Posts.Tags LIKE '%bash%' OR Posts.Tags LIKE '%git%' OR Posts.Tags LIKE '%grep%'
  AND Posts.PostTypeId = 1
  ORDER BY Posts.Score DESC
  ```
* **Post-processing**:
  Converted into instructions and response pattern for finetuning, cleaned and saved into a JSON file (`Data\data_for_finetuning.json`).
  The cod used is in: Data\data.py

## 🧠 Model & Fine-Tuning

* **Base Model**: [`TinyLlama/TinyLlama-1.1B-Chat-v1.0`](https://huggingface.co/TinyLlama/TinyLlama-1.1B-Chat-v1.0)

* **Method**: LoRA fine-tuning using Hugging Face `PEFT`

* **Training Details**:

  * **Output Directory**: `./results`
  * **Epochs**: 1
  * **Batch Size**: 1 (per device)
  * **Optimizer**: `paged_adamw_8bit`
  * **Logging Steps**: 10
  * **Save Steps**: 100
  * **Save Total Limit**: 2
  * **Mixed Precision**: Disabled (`fp16=False`)
  * **Reporting**: Disabled (`report_to="none"`)

* **Platform**: Kaggle T4 GPU

* **Training Time**: \~15 minutes

* **LoRA Adapter Size**: \~8.61 MB

## 📊 Evaluation Summary

### Static Evaluation (ROUGE-L)

| Instruction                                     | ROUGE-L (Base) | ROUGE-L (Fine-Tuned)   |
| --------------------------------------          | -------------- | --------------------   |
| Create a Git branch                             | 0.2882         | 0.3371                 |
| Compress folder                                 | 0.2604         | 0.2604                 |
| List Python files recursively                   | 0.2652         | 0.2652                 |
| Set up venv + install `requests`                | 0.375          | 0.3111                 |
| First 10 lines of `output.log`                  | 0.2736         | 0.1798                 |
| Delete all `.tmp` files (edge case)             | 0.1667         | 0.1667                 |
| Check if a Python package is installed          | 0.2667         | 0.2667                 |
| List all installed Python packages and versions.| 0.2626         | 0.2626                 |

### Dynamic Evaluation (0-2 scale)

| Instruction                                     | Dynamic (Base) | Dynamic (Fine-Tuned)   |
| --------------------------------------          | -------------- | --------------------   |
| Create a Git branch                             | 1              | 2                      |
| Compress folder                                 | 0              | 0                      |
| List Python files recursively                   | 1              | 1                      |
| Set up venv + install `requests`                | 0.5            | 1.5                    |
| First 10 lines of `output.log`                  | 1              | 0.5                    |
| Delete all `.tmp` files (edge case)             | 1              | 1                      |
| Check if a Python package is installed          | 0.5            | 0.5                    |
| List all installed Python packages and versions.| 0.4            | 0.4                    |


## 💡 Future Improvements

1. **Train for More Epochs** – Current training was only for 1 epoch. More epochs would likely improve BLEU/ROUGE further.
2. **Multilingual CLI Support** – Extend dataset and model to support CLI instructions in other languages (e.g., Bash in Spanish, Hindi tech users), expanding accessibility.
3. **Humor-Driven Instruction Tuning** - Explore the impact of humor and informal language on model comprehension and user engagement during command generation tasks — potentially improving learning retention in educational tools.