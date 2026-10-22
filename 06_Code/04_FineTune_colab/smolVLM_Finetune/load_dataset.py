from datasets import load_dataset

DATASET_PATH = r"smolvlm_train.jsonl"

dataset = load_dataset(
    "json",
    data_files=DATASET_PATH,
    split="train"
)

print(dataset)

print("\nNumber of Samples:")
print(len(dataset))

print("\nFirst Sample:")
print(dataset[0])