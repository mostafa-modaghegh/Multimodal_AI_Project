from transformers import (
    AutoProcessor,
    Idefics3ForConditionalGeneration,
)

from peft import (
    get_peft_model,
)

from lora_config import lora_config

MODEL_NAME = "HuggingFaceTB/SmolVLM-256M-Instruct"

print("Loading Model...")

processor = AutoProcessor.from_pretrained(MODEL_NAME)

model = Idefics3ForConditionalGeneration.from_pretrained(
    MODEL_NAME,
    torch_dtype="auto",
)

print("Model Loaded.\n")

print("Applying LoRA...")

model = get_peft_model(
    model,
    lora_config
)

print("LoRA Installed Successfully.\n")

print("Trainable Parameters")

model.print_trainable_parameters()