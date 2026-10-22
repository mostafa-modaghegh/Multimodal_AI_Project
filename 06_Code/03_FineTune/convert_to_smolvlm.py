import json
import os

# -----------------------------
# Paths
# -----------------------------

DATASET_DIR = r"D:\Mostafi\Multimodal_AI_Project\10_Datasets\Iranian_License_Plate_V1"

INPUT_FILE = os.path.join(DATASET_DIR, "dataset.json")

OUTPUT_FILE = os.path.join(DATASET_DIR, "smolvlm_train.jsonl")


# -----------------------------
# Converter
# -----------------------------

def convert():

    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        dataset = json.load(f)

    sample_count = 0

    with open(OUTPUT_FILE, "w", encoding="utf-8") as writer:

        for image_sample in dataset:

            image_path = image_sample["image"]

            for conv in image_sample["conversations"]:

                sample = {

                    "messages": [

                        {
                            "role": "user",

                            "content": [

                                {
                                    "type": "image",
                                    "image": image_path
                                },

                                {
                                    "type": "text",
                                    "text": conv["question"]
                                }

                            ]
                        },

                        {
                            "role": "assistant",

                            "content": [

                                {
                                    "type": "text",
                                    "text": conv["answer"]
                                }

                            ]
                        }

                    ]

                }

                writer.write(
                    json.dumps(
                        sample,
                        ensure_ascii=False
                    )
                )

                writer.write("\n")

                sample_count += 1

    print("=" * 50)
    print("Conversion Finished")
    print(f"Training Samples : {sample_count}")
    print(f"Saved File       : {OUTPUT_FILE}")
    print("=" * 50)


# -----------------------------
# Main
# -----------------------------

if __name__ == "__main__":
    convert()