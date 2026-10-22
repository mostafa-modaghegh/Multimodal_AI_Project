from pathlib import Path

from transformers import (
    AutoProcessor,
    Idefics3ForConditionalGeneration,
)


BASE_DIR = Path(__file__).resolve().parent

CHECKPOINT = BASE_DIR / "outputs" / "final_checkpoint"

print("=" * 60)
print("Loading Fine-Tuned Checkpoint")
print("=" * 60)

print(CHECKPOINT)

model = Idefics3ForConditionalGeneration.from_pretrained(

    CHECKPOINT,

    torch_dtype="auto",

    device_map="auto"

)

processor = AutoProcessor.from_pretrained(

    CHECKPOINT

)

print()

print("✓ Fine-Tuned Model Loaded")

print("✓ Processor Loaded")

print("=" * 60)