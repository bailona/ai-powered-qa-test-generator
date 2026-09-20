from src.qa_test_generator import generate_test_cases
from src.ai_generator import generate_with_ai
from src.export_results import save_test_cases


def main():
    requirement = input("\nEnter the software requirement:\n> ")

    if not requirement.strip():
        print("Requirement cannot be empty.")
        return

    result = generate_test_cases(requirement)
    ai_status = generate_with_ai(requirement)

    output_file = "data/generated/test_cases.json"
    save_test_cases(result, output_file)

    print("\n========================================")
    print("AI-Powered QA Test Generator")
    print("========================================")

    print(f"\nRequirement:\n{result['requirement']}")

    print(f"\nGenerated test cases: {len(result['test_cases'])}")

    for test_case in result["test_cases"]:
        print(f"\n[{test_case['id']}] {test_case['title']}")
        print(f"Type: {test_case['type']}")
        print(f"Priority: {test_case['priority']}")

    print("\n----------------------------------------")
    print("GenAI Integration")
    print("----------------------------------------")
    print(f"Provider: {ai_status['provider']}")
    print(f"Status: {ai_status['status']}")
    print(ai_status["message"])

    print(f"\nResults saved to: {output_file}")


if __name__ == "__main__":
    main()


