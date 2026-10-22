from pathlib import Path

import torch
from PIL import Image

from load_checkpoint import model, processor

# -----------------------------------------------------

IMAGE_PATH = "test_images/plate001.jpg"

QUESTION = "What is the color of car?"

# -----------------------------------------------------

image = Image.open(IMAGE_PATH).convert("RGB")

messages = [

    {

        "role": "user",

        "content": [

            {

                "type": "image",

                "image": image

            },

            {

                "type": "text",

                "text": QUESTION

            }

        ]

    }

]

prompt = processor.apply_chat_template(

    messages,

    tokenize=False,

    add_generation_prompt=True

)

inputs = processor(

    text=prompt,

    images=image,

    return_tensors="pt"

)

inputs = {

    k: v.to(model.device)

    for k, v in inputs.items()

}

with torch.no_grad():

    generated_ids = model.generate(

        **inputs,

        max_new_tokens=32,

        do_sample=False

    )

output = processor.batch_decode(

    generated_ids,

    skip_special_tokens=True

)[0]

print()

print("=" * 60)

print("MODEL OUTPUT")

print("=" * 60)

print(output)