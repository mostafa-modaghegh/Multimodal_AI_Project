import os
import json


# مسیر دیتاست
DATASET_DIR = r"D:\Mostafi\Multimodal_AI_Project\10_Datasets\Iranian_License_Plate_V1"

# پوشه تصاویر
IMAGE_DIR = os.path.join(DATASET_DIR, "images")

# فایل خروجی
OUTPUT_FILE = os.path.join(DATASET_DIR, "dataset.json")


# بانک سوالات
QUESTION_BANK = [
    "Read the license plate number.",
    "Is there a visible license plate in this image?",
    "Which city does this license plate belong to?",
    "What is the color of the vehicle?",
    "Describe this image."
]


def create_dataset():

    dataset = []

    # دریافت لیست تصاویر
    images = sorted(
        [
            img for img in os.listdir(IMAGE_DIR)
            if img.lower().endswith((".jpg", ".jpeg", ".png"))
        ]
    )

    print(f"Found {len(images)} images")

    for image_name in images:

        sample = {

            "image": f"images/{image_name}",

            "metadata": {

                "vehicle": None,
                "plate_number": None,
                "color": None,
                "plate_city": None,
                "plate_visible": None,
                "description": None

            },

            "conversations": []

        }

        # اضافه کردن سوالات
        for question in QUESTION_BANK:

            sample["conversations"].append(
                {
                    "question": question,
                    "answer": None
                }
            )

        dataset.append(sample)

    # ذخیره JSON
    with open(
        OUTPUT_FILE,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            dataset,
            file,
            ensure_ascii=False,
            indent=2
        )

    print("\nDataset created successfully!")
    print(f"Saved at: {OUTPUT_FILE}")


if __name__ == "__main__":

    create_dataset()