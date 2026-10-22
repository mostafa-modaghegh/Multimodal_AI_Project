from transformers import AutoProcessor

MODEL_ID = "HuggingFaceTB/SmolVLM2-500M-Video-Instruct"

print("Loading Processor...")

processor = AutoProcessor.from_pretrained(
    MODEL_ID
)

print("Processor Loaded.")