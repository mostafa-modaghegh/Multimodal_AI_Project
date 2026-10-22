from transformers import AutoProcessor, AutoModelForImageTextToText
import torch

model_name = "HuggingFaceTB/SmolVLM-256M-Instruct"

print("=" * 60)
print("Loading processor...")
processor = AutoProcessor.from_pretrained(model_name)

print("=" * 60)
print("loading model")
model = AutoModelForImageTextToText.from_pretrained(
    model_name,
    torch_dtype="auto"
)

model = model.to("cuda")

print("=" * 60)
print("Model class:")
print(type(model))

print("=" * 60)
print("Model device:")
print(next(model.parameters()).device)

print("=" * 60)
print("Tensor dtype:")
print(next(model.parameters()).dtype)

print("=" * 60)
print("Model type:")
print(model.config.model_type)

print("=" * 60)
print("Hidden size:")
print(model.config.text_config.hidden_size)

print("=" * 60)
print("Vocabulary size:")
print(model.config.text_config.vocab_size)

print("=" * 60)
print("Number of decoder layers:")
print(model.config.text_config.num_hidden_layers)

print("=" * 60)
print("Done.")