from transformers import TrainingArguments

training_args = TrainingArguments(

    output_dir="./outputs",

    num_train_epochs=5,

    per_device_train_batch_size=1,

    gradient_accumulation_steps=2,

    learning_rate=2e-4,

    weight_decay=0.01,

    warmup_steps=10,

    logging_steps=5,

    save_strategy="epoch",

    remove_unused_columns=False,

    report_to="tensorboard",

    seed=42

)