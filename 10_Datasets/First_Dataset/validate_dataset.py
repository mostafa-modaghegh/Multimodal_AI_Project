import json
import os


DATASET_PATH = "train.jsonl"


def validate_dataset(dataset_path):

    if not os.path.exists(dataset_path):
        print(f"❌ Dataset file not found: {dataset_path}")
        return


    total_samples = 0
    total_errors = 0


    print("Starting validation...\n")


    with open(dataset_path, "r", encoding="utf-8") as file:

        for line_number, line in enumerate(file, start=1):

            try:
                sample = json.loads(line)

            except json.JSONDecodeError as e:
                print(f"❌ Invalid JSON at line {line_number}")
                print(e)

                total_errors += 1
                continue


            total_samples += 1


            # Check messages

            if "messages" not in sample:
                print(f"❌ Line {line_number}: messages missing")
                total_errors += 1
                continue


            messages = sample["messages"]


            if not isinstance(messages, list):
                print(f"❌ Line {line_number}: messages is not a list")
                total_errors += 1


            for message in messages:

                if "role" not in message:
                    print(f"❌ Line {line_number}: role missing")
                    total_errors += 1


                if "content" not in message:
                    print(f"❌ Line {line_number}: content missing")
                    total_errors += 1
                    continue


                for item in message["content"]:

                    if item["type"] == "image":

                        image_path = item["image"]


                        if not os.path.exists(image_path):

                            print(
                                f"❌ Line {line_number}: "
                                f"Image not found -> {image_path}"
                            )

                            total_errors += 1



    print("\n========================")
    print("Validation finished")
    print("========================")

    print(f"Total samples: {total_samples}")
    print(f"Total errors: {total_errors}")


    if total_errors == 0:
        print("✅ Dataset is valid!")

    else:
        print("⚠️ Dataset contains errors.")



if __name__ == "__main__":

    validate_dataset(DATASET_PATH)