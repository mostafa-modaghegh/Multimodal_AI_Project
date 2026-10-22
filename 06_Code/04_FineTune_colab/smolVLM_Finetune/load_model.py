from transformers import Idefics3ForConditionalGeneration

MODEL_ID = "HuggingFaceTB/SmolVLM2-500M-Video-Instruct"

print("Loading Model...")

model = Idefics3ForConditionalGeneration.from_pretrained(
    MODEL_ID,
    torch_dtype="auto",
    device_map="auto"
)

print("Model Loaded.")

print("Enable Gradient Checkpointing...")

model.gradient_checkpointing_enable()
model.config.use_cache = False

print("Gradient Checkpointing Enabled.")