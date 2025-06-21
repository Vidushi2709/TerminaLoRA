import os
import json
import re
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
from peft import PeftModel, PeftConfig

# Load fine-tuned model (CPU-safe)
peft_model_path = "my_finetuned_model"
peft_config = PeftConfig.from_pretrained(peft_model_path)
base_model = AutoModelForCausalLM.from_pretrained(
    peft_config.base_model_name_or_path,
    torch_dtype=torch.float32,
    device_map=None
)
model = PeftModel.from_pretrained(base_model, peft_model_path).to("cpu")
tokenizer = AutoTokenizer.from_pretrained(peft_model_path)

# For logging
LOG_PATH = "logs/trace.jsonl"
os.makedirs("logs", exist_ok=True)

def is_shell_command(line):
    return re.match(r"^(cd|dir|mkdir|rmdir|del|copy|move|echo|ls|rm|git|python|pip|bash|chmod|tar|gzip|grep|venv)\b", line.strip())

def run_cli_agent():
    instruction = input("🧠 Enter your Query:\n> ").strip()

    # Tokenize and generate response
    prompt= f"""You are a helpful CLI assistant. Given an instruction, explain how to do it step-by-step using short, clear shell commands where needed.
    Instruction: {instruction}
    Step-by-step plan:"""
    
    inputs = tokenizer(prompt, return_tensors="pt").to("cpu")

    with torch.no_grad():
        outputs = model.generate(
        **inputs,
        max_new_tokens=256,
        return_dict_in_generate=True,
        output_scores=False
    )

    generated_tokens = outputs.sequences[0][inputs['input_ids'].shape[1]:]
    decoded = tokenizer.decode(generated_tokens, skip_special_tokens=True)

    print("💡Let's solve your problem:\n")
    steps = [line.strip() for line in decoded.split("\n") if line.strip()]
    print("\n💡 AI Plan: \n")
    for i, step in enumerate(steps, 1):
        if "Explanation:" in step:
            command, explanation = step.split("\n Explanation: \n", 1)
            print(f"{i}. 💻 Command: {command.strip()}")
            print(f"   📘 Explanation: {explanation.strip()}")
        else:
            print(f"{i}. {step}")

    # Dry-run shell command if step 1 is a shell command
    if steps and is_shell_command(steps[0]):
        print("\n💻 Dry-run Command:\n")
        print(f"echo {steps[0]}")

    # Log to trace
    with open(LOG_PATH, "a") as f:
        json.dump({"instruction": instruction, "steps": steps}, f)
        f.write("\n")
    print(f"\n📄 Logged to: {LOG_PATH}")

if __name__ == "__main__":
    run_cli_agent()
