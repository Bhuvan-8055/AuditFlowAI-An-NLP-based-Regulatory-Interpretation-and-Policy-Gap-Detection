import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
from peft import PeftModel

base_model_id = "meta-llama/Meta-Llama-3-8B"
lora_path = "llama_legal_lora"
output_path = "llama_legal_merged"

tokenizer = AutoTokenizer.from_pretrained(base_model_id)

model = AutoModelForCausalLM.from_pretrained(
    base_model_id,
    torch_dtype=torch.float16,
    device_map=None
)

model = PeftModel.from_pretrained(
    model,
    lora_path,
    device_map=None
)

model = model.merge_and_unload()

model.save_pretrained(output_path, safe_serialization=True)
tokenizer.save_pretrained(output_path)
