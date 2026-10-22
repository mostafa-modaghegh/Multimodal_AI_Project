from transformers import (
    AutoProcessor,
    Idefics3ForConditionalGeneration
)
import torch


MODEL_ID = "HuggingFaceTB/SmolVLM-256M-Instruct"

device = torch.device(
    "cuda" if torch.cuda.is_available() else "cpu"
)

print("Loading model...")
processor = AutoProcessor.from_pretrained(MODEL_ID)
model = Idefics3ForConditionalGeneration.from_pretrained(
    MODEL_ID,
    torch_dtype=torch.float16
)
model.to(device)
print("Model Loaded.\n")


print("=" * 80)
print("TOP LEVEL MODULES")
print("=" * 80)

for name, module in model.named_children():
    print(name, " ---> ", type(module).__name__)

print("\n")
print("=" * 80)
print("CHILDREN OF MODEL")
print("=" * 80)

for name, module in model.model.named_children():
    print(name, " ---> ", type(module).__name__)


print("\n")
print("=" * 80)
print("TEXT MODEL")
print("=" * 80)

for name, module in model.model.text_model.named_children():
    print(name, " ---> ", type(module).__name__)

print("\n")
print("=" * 80)
print("FIRST TRANSFORMER LAYER")
print("=" * 80)

for name, module in model.model.text_model.layers[0].named_children():
    print(name, " ---> ", type(module).__name__)

print("\n")
print("=" * 80)
print("SELF ATTENTION")
print("=" * 80)

for name, module in model.model.text_model.layers[0].self_attn.named_children():
    print(name, " ---> ", type(module).__name__)