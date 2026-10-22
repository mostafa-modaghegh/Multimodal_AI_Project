from datasets import load_dataset
from transformers import AutoProcessor
from PIL import Image
import os

DATASET_DIR = r"D:\Mostafi\Multimodal_AI_Project\10_Datasets\Iranian_License_Plate_V1"

JSONL_PATH = os.path.join(DATASET_DIR, "smolvlm_train.jsonl")

processor = AutoProcessor.from_pretrained(
    "HuggingFaceTB/SmolVLM-256M-Instruct"
)

dataset = load_dataset(
    "json",
    data_files=JSONL_PATH,
    split="train"
)

sample = dataset[0]

messages = sample["messages"]

image_path = os.path.join(
    DATASET_DIR,
    messages[0]["content"][0]["image"]
)

image = Image.open(image_path).convert("RGB")

text = processor.apply_chat_template(
    messages,
    add_generation_prompt=False
)

inputs = processor(
    text=text,
    images=image,
    return_tensors="pt"
)

print("\nShapes")
print("----------------")

for key, value in inputs.items():
    print(key, value.shape)

print("=" * 80)
print("Decoded Input")
print("=" * 80)

decoded = processor.decode(
    inputs["input_ids"][0],
    skip_special_tokens=False
)

print(decoded)