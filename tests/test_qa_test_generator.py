from src.qa_test_generator import generate_test_cases


REQUIREMENT = "User should be able to reset their password using their registered email."


def test_reset_password_generates_five_test_cases():
    result = generate_test_cases(REQUIREMENT)

    assert len(result["test_cases"]) == 5


def test_first_test_case_is_positive():
    result = generate_test_cases(REQUIREMENT)

    first_case = result["test_cases"][0]

    assert first_case["id"] == "TC001"
    assert first_case["type"] == "Positive"


def test_negative_test_cases_are_generated():
    result = generate_test_cases(REQUIREMENT)

    negative_cases = [
        test_case
        for test_case in result["test_cases"]
        if test_case["type"] == "Negative"
    ]

    assert len(negative_cases) == 4


def test_all_test_cases_have_automation_code():
    result = generate_test_cases(REQUIREMENT)

    for test_case in result["test_cases"]:
        assert "automation_code" in test_case
        assert test_case["automation_code"]


def test_automation_code_uses_playwright():
    result = generate_test_cases(REQUIREMENT)

    for test_case in result["test_cases"]:
        assert "playwright" in test_case["automation_code"].lower()

