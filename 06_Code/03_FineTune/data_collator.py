'''from dataclasses import dataclass
import torch


@dataclass
class VLMDataCollator:

    processor: any
    model: any

    def __call__(self, examples):

        texts = [

            self.processor.apply_chat_template(

                example["messages"],

                tokenize=False,

                add_generation_prompt=False

            )

            for example in examples

        ]

        images = [

            [

                item["image"]

                for item in example["messages"][0]["content"]

                if item["type"] == "image"

            ]

            for example in examples

        ]

        batch = self.processor(

            text=texts,

            images=images,

            padding=True,

            return_tensors="pt"

        )

        labels = batch["input_ids"].clone()

        # Ignore Padding

        labels[
            labels == self.processor.tokenizer.pad_token_id
        ] = -100

        # Ignore Image Tokens

        labels[
            labels == self.model.config.image_token_id
        ] = -100

        batch["labels"] = labels

        return batch
'''

from dataclasses import dataclass
from PIL import Image
import os
import torch


@dataclass
class VLMDataCollator:

    processor: any
    model: any

    DATASET_ROOT = r"D:\Mostafi\Multimodal_AI_Project\10_Datasets\Iranian_License_Plate_V1"

    def __call__(self, examples):

        texts = []
        images = []

        for example in examples:

            # --------------------------
            # ساخت Prompt
            # --------------------------

            prompt = self.processor.apply_chat_template(

                example["messages"],

                tokenize=False,

                add_generation_prompt=False

            )

            texts.append(prompt)

            # --------------------------
            # بارگذاری تصاویر
            # --------------------------

            sample_images = []

            for item in example["messages"][0]["content"]:

                if item["type"] == "image":

                    image_path = os.path.join(

                        self.DATASET_ROOT,

                        item["image"]

                    )

                    image = Image.open(image_path).convert("RGB")

                    sample_images.append(image)

            images.append(sample_images)

        # --------------------------
        # Processor
        # --------------------------

        batch = self.processor(

            text=texts,

            images=images,

            padding=True,

            return_tensors="pt"

        )

        # --------------------------
        # Labels
        # --------------------------

        labels = batch["input_ids"].clone()

        # حذف PAD

        labels[
            labels == self.processor.tokenizer.pad_token_id
        ] = -100

        # حذف Image Tokens

        labels[
            labels == self.model.config.image_token_id
        ] = -100

        batch["labels"] = labels

        return batch
