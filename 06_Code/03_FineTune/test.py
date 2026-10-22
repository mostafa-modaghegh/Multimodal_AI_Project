from datasets import load_dataset

from load_model import model
from load_processor import processor

from data_collator import VLMDataCollator


dataset = load_dataset(
    "json",
    data_files="../../10_Datasets/Iranian_License_Plate_V1/smolvlm_train.jsonl",
    split="train"
)

collator = VLMDataCollator(

    processor=processor,

    model=model

)

batch = collator(

    [

        dataset[0],

        dataset[1]

    ]

)

print()

print("=" * 50)

print("Batch Shapes")

print("=" * 50)

for key, value in batch.items():

    print(key, value.shape)