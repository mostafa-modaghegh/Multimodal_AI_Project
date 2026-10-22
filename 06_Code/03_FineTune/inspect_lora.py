from transformers import (
    AutoProcessor,
    Idefics3ForConditionalGeneration,
)

from peft import (
    get_peft_model,
)

from lora_config import lora_config

MODEL_NAME = "HuggingFaceTB/SmolVLM-256M-Instruct"

print("Loading model...")

processor = AutoProcessor.from_pretrained(MODEL_NAME)

model = Idefics3ForConditionalGeneration.from_pretrained(
    MODEL_NAME,
    torch_dtype="auto",
)

model = get_peft_model(
    model,
    lora_config
)

print("\n==============================")
print("First Transformer Layer")
print("==============================")

layer = model.base_model.model.model.text_model.layers[0]

print(layer.self_attn)

print("\n==============================")
print("Q Projection")
print("==============================")

print(layer.self_attn.q_proj)

print("\n==============================")
print("K Projection")
print("==============================")

print(layer.self_attn.k_proj)

print("\n==============================")
print("V Projection")
print("==============================")

print(layer.self_attn.v_proj)

print("\n==============================")
print("O Projection")
print("==============================")

print(layer.self_attn.o_proj)