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

### Summarizing what the scores tell:
    - The fine-tuned model showed improvements in instructional clarity for tasks like Git branching.
    - Equal ROUGE-L scores in some cases indicate both models performed similarly or were exact matches.
    - Slightly lower fine-tuned scores may reflect stylistic divergence rather than actual quality reduction. 

The fine-tuned model was trained on approximately 150 instruction–response pairs for only 1 epoch. As a result, while some improvements are visible in certain instruction categories (e.g., Git operations), the overall changes in ROUGE-L scores remain subtle. 