import json
import os

# ======================================================
# Paths
# ======================================================

DATASET_DIR = r"D:\Mostafi\Multimodal_AI_Project\10_Datasets\Iranian_License_Plate_V1"

JSONL_FILE = os.path.join(DATASET_DIR, "smolvlm_train.jsonl")


# ======================================================
# Validation
# ======================================================

total_samples = 0

missing_images = 0

empty_questions = 0

empty_answers = 0

invalid_structure = 0

print("=" * 60)
print("Validating SmolVLM Dataset")
print("=" * 60)


with open(JSONL_FILE, "r", encoding="utf-8") as file:

    for line_number, line in enumerate(file, start=1):

        total_samples += 1

        try:

            sample = json.loads(line)

        except Exception:

            print(f"[Line {line_number}] Invalid JSON")

            invalid_structure += 1

            continue

        # --------------------------------------------------

        if "messages" not in sample:

            print(f"[Line {line_number}] Missing messages")

            invalid_structure += 1

            continue

        if len(sample["messages"]) != 2:

            print(f"[Line {line_number}] Conversation length != 2")

            invalid_structure += 1

            continue

        # --------------------------------------------------

        user = sample["messages"][0]

        assistant = sample["messages"][1]

        # --------------------------------------------------

        try:

            image_path = user["content"][0]["image"]

            question = user["content"][1]["text"]

            answer = assistant["content"][0]["text"]

        except Exception:

            print(f"[Line {line_number}] Invalid message format")

            invalid_structure += 1

            continue

        # --------------------------------------------------

        full_image_path = os.path.join(DATASET_DIR, image_path)

        if not os.path.exists(full_image_path):

            print(f"[Line {line_number}] Missing image : {image_path}")

            missing_images += 1

        # --------------------------------------------------

        if question.strip() == "":

            print(f"[Line {line_number}] Empty question")

            empty_questions += 1

        if answer.strip() == "":

            print(f"[Line {line_number}] Empty answer")

            empty_answers += 1


# ======================================================
# Summary
# ======================================================

print()

print("=" * 60)

print("Validation Report")

print("=" * 60)

print(f"Total Samples      : {total_samples}")

print(f"Missing Images     : {missing_images}")

print(f"Empty Questions    : {empty_questions}")

print(f"Empty Answers      : {empty_answers}")

print(f"Invalid Structures : {invalid_structure}")

print()

if (
    missing_images == 0
    and empty_questions == 0
    and empty_answers == 0
    and invalid_structure == 0
):

    print("✅ Dataset is READY for Fine-tuning.")

else:

    print("❌ Please fix the reported errors before training.")