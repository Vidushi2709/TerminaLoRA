### Dynamic Evaluation 
    We manually scored each model’s response using a 3-point scale:
    0 – Incorrect or irrelevant response
    1 – Partially correct but incomplete
    2 – Fully correct and appropriate

### Dynamic Evaluation 

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

### Limitations:
    - Fine-tuned model was trained for 1 epoch on only ~150 instruction-response pairs
    - Lack of generalization across unseen or edge-case tasks
    - Evaluation is subjective but consistent across reviewers