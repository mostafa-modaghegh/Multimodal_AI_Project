from transformers import AutoProcessor 
from PIL import Image

model_name = "HuggingFaceTB/SmolVLM-256M-Instruct"

processor = AutoProcessor.from_pretrained(model_name)

image = Image.open("Images/test.jpg").convert("RGB")

inputs = processor(
    images=image,
    text="<image>Describe this image.",
    return_tensors="pt"
)

print("=" * 50)

print(inputs.keys())

print("=" * 50)

for key, value in inputs.items():
    print(f"{key}")
    print(f"shape : {value.shape}")
    print(f"dtype : {value.dtype}")
    print()