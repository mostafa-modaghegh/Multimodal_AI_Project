from transformers import Trainer

from load_model import model
from load_processor import processor
from load_dataset import dataset
from training_args import training_args
from data_collator import VLMDataCollator


def main():

    print("=" * 60)
    print("Creating Data Collator...")
    print("=" * 60)

    collator = VLMDataCollator(

        processor=processor,

        model=model

    )

    print("✓ Data Collator Ready")

    print()

    print("=" * 60)
    print("Creating Trainer...")
    print("=" * 60)

    trainer = Trainer(

        model=model,

        args=training_args,

        train_dataset=dataset,

        data_collator=collator,

        processing_class=processor

    )

    print("✓ Trainer Ready")

    print()

    print("=" * 60)
    print("Starting Fine-Tuning...")
    print("=" * 60)

    trainer.train()

    print()

    print("=" * 60)
    print("Saving LoRA Adapter...")
    print("=" * 60)

    trainer.save_model("./outputs/final_checkpoint")

    print("✓ Training Finished Successfully")


if __name__ == "__main__":

    main()