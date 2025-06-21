# 🧠 CLI Assistant – Fine-Tuned Mini LLM with LoRA

This project demonstrates how to fine-tune a lightweight open-source language model (≤2B parameters) using LoRA for CLI (Command Line Interface) task automation. It includes data collection, model training, evaluation, and a working `agent.py` that responds to terminal instructions with step-by-step shell commands.

---

## 📌 Objective

Build a concise, command-focused CLI assistant that:

* Accepts natural language instructions.
* Returns minimal, actionable shell commands.
* Can dry-run and log actions via a terminal agent.
* Is evaluated against a fixed test set and edge cases.

---

## 📁 Project Structure

```
.
├── data/                      # ≥150 Q&A pairs on command-line tasks
├── my_finetuned_model/       # LoRA adapter files after training
├── cli_agent.py                  # CLI Agent to accept instructions
├── training.ipynb               # Training notebook (LoRA fine-tuning)
├── eval_static.md            # Base vs Fine-tuned outputs + BLEU
├── eval_dynamic.md           # Agent evaluation + scoring table
├── report.md                 # One-page summary of process
├── logs/
│   └── trace.jsonl           # Dynamic logs of CLI queries
├── README.md                 # You are here
└── demo.mp4 / demo.loom      # Demo video (≤5 min)
```

---

## 🛠️ Fine-Tuning Details

* **Base Model:** [TinyLlama-1.1B](https://huggingface.co/cognitivecomputations/TinyLlama-1.1B)
* **Training Approach:** LoRA (Low-Rank Adaptation)
* **Frameworks Used:** 🤗 Transformers, 🤗 PEFT, BitsAndBytes
* **Device:** Kaggle Nb T4 (Free)
* **Dataset:** 150+ curated Q\&A pairs on Git, Bash, Python, `tar`, `grep`, `venv`, etc.
* **Epochs:** 1
* **Precision:** 8-bit 

---

## 🤖 Running the CLI Agent

```bash
python agent.py
```

This launches an interactive shell:

```bash
🧠 Enter your CLI instruction:
> Create a new Git branch and switch to it

💡 AI Plan:
1. git checkout -b new-branch

💻 Dry-run Command:
echo git checkout -b new-branch

📄 Logged to: logs/trace.jsonl
```
