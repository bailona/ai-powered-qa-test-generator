from unittest.mock import MagicMock, patch

from src.qa_test_generator import generate_test_cases
from src.ai_generator import generate_with_ai


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


def test_generate_with_ai():
    mock_response = MagicMock()

    mock_response.output_text = "Mocked QA analysis"
    mock_response.usage.input_tokens = 10
    mock_response.usage.output_tokens = 20
    mock_response.usage.total_tokens = 30

    with patch(
        "src.ai_generator.client.responses.create",
        return_value=mock_response,
    ) as mock_create:

        result = generate_with_ai(
            "User should be able to reset their password."
        )

    mock_create.assert_called_once()

    assert result["provider"] == "OpenAI"
    assert result["model"] == "gpt-5.6-luna"
    assert result["status"] == "connected"
    assert result["generated_content"] == "Mocked QA analysis"
    assert result["usage"]["total_tokens"] == 30
