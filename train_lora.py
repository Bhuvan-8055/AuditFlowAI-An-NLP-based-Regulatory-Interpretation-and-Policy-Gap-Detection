from datasets import load_dataset
from transformers import AutoModelForCausalLM, TrainingArguments
from peft import LoraConfig, get_peft_model
from trl import SFTTrainer

model_id = "meta-llama/Meta-Llama-3-8B"

model = AutoModelForCausalLM.from_pretrained(
    model_id,
    load_in_4bit=True,
    device_map="auto"
)

dataset = load_dataset(
    "json",
    data_files="indiclegalqa_instruction.jsonl",
    split="train"
)

lora = LoraConfig(
    r=8,
    lora_alpha=16,
    lora_dropout=0.05,
    target_modules=["q_proj", "v_proj"],
    task_type="CAUSAL_LM"
)

model = get_peft_model(model, lora)

args = TrainingArguments(
    output_dir="llama_legal_lora",
    per_device_train_batch_size=1,
    gradient_accumulation_steps=4,
    num_train_epochs=2,
    fp16=False,
    bf16=False,
    optim="paged_adamw_8bit",
    logging_steps=50,
    save_strategy="epoch",
    report_to="none"
)

trainer = SFTTrainer(
    model=model,
    train_dataset=dataset,
    args=args,
    formatting_func=lambda x: (
        f"### Instruction:\n{x['instruction']}\n\n"
        f"### Input:\n{x['input']}\n\n"
        f"### Answer:\n{x['output']}"
    )
)

trainer.train()
model.save_pretrained("llama_legal_lora")
