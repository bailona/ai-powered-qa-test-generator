import json


def save_test_cases(result, output_file):
    with open(output_file, "w", encoding="utf-8") as file:
        json.dump(result, file, indent=4, ensure_ascii=False)
