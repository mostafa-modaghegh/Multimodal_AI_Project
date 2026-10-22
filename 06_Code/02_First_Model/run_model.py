from transformers import AutoProcessor, AutoModelForImageTextToText
from PIL import Image 
import torch

model_name = "HuggingFaceTB/SmolVLM-256M-Instruct"

print("Loading processor...")
processor = AutoProcessor.from_pretrained(model_name)

print("Loading model...")
model = AutoModelForImageTextToText.from_pretrained(
    model_name,
    torch_dtype = "auto"
).to("cuda")

image = Image.open("Images/image.jpg")

messages = [
    {
        "role": "user",
        "content": [
            {"type": "image"},
            {"type": "text", "text": "Describe this image."}
        ]
    }
]

prompt = processor.apply_chat_template(
    messages,
    add_generation_prompt=True
)

inputs = processor(
    text=prompt,
    images=image,
    return_tensors="pt"
)

inputs = {k: v.to(model.device) for k, v in inputs.items()}

print("Generating...")

outputs = model.generate(
    **inputs,
    max_new_tokens=100
)

answer = processor.decode(
    outputs[0],
    skip_special_tokens=True
)

print("\n===================")
print(answer)
print("====================")