from src.qa_test_generator import generate_test_cases
from src.ai_generator import generate_with_ai
from src.export_results import save_test_cases, save_ai_analysis


def main():
    requirement = input("\nEnter the software requirement:\n> ")

    if not requirement.strip():
        print("Requirement cannot be empty.")
        return

    result = generate_test_cases(requirement)
    ai_status = generate_with_ai(requirement)

    test_cases_file = "data/generated/test_cases.json"
    ai_analysis_file = "data/generated/ai_analysis.json"

    save_test_cases(result, test_cases_file)
    save_ai_analysis(ai_status, ai_analysis_file)

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
    print(f"Model: {ai_status['model']}")
    print(f"Status: {ai_status['status']}")

    if ai_status["status"] == "connected":
        print(f"Tokens used: {ai_status['usage']['total_tokens']}")
        print("GenAI analysis generated successfully.")
    else:
        print("GenAI analysis could not be generated.")
        print(f"Error: {ai_status['error']}")

    print(f"\nTest cases saved to: {test_cases_file}")
    print(f"AI analysis saved to: {ai_analysis_file}")


if __name__ == "__main__":
    main()
