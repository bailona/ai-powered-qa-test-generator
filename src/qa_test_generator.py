from .automation_generator import generate_automation_code


def analyze_requirement(requirement):
    requirement_lower = requirement.lower()

    return {
        "has_email": "email" in requirement_lower,
        "has_password": "password" in requirement_lower,
        "has_login": "login" in requirement_lower,
        "has_reset": "reset" in requirement_lower,
    }


def generate_test_cases(requirement):
    analysis = analyze_requirement(requirement)

    test_cases = []

    if analysis["has_reset"] and analysis["has_password"]:
        test_cases.extend([
            {
                "id": "TC001",
                "title": "Reset password with valid registered email",
                "type": "Positive",
                "priority": "High",
                "description": "Verify that a registered user can request a password reset.",
                "preconditions": "User has a registered account.",
                "test_steps": [
                    "Open the password reset page.",
                    "Enter a registered email address.",
                    "Submit the reset request."
                ],
                "expected_result": "A password reset email is sent to the registered address.",
                "test_data": "registered_user@example.com",
                "gherkin": [
                    "Given the user has a registered account",
                    "When the user requests a password reset using the registered email",
                    "Then a password reset email should be sent"
                ],
                "edge_cases": [
                    "Email address with uppercase characters",
                    "Email address with leading or trailing spaces",
                    "Very long email address",
                    "Registered email using a different domain"
                ],
                "automation_suggestion": "Automate with Playwright using the password reset page and validate the confirmation message and email notification.",
                "automation_code": generate_automation_code({"id": "TC001"})
            },
            {
                "id": "TC002",
                "title": "Reset password with unregistered email",
                "type": "Negative",
                "priority": "High",
                "description": "Verify the behavior when an unregistered email is submitted.",
                "preconditions": "The email address is not associated with an account.",
                "test_steps": [
                    "Open the password reset page.",
                    "Enter an unregistered email address.",
                    "Submit the reset request."
                ],
                "expected_result": "The system handles the request according to the defined security policy without exposing account information.",
                "test_data": "unknown_user@example.com"
            },
            {
                "id": "TC003",
                "title": "Reset password with invalid email format",
                "type": "Negative",
                "priority": "Medium",
                "description": "Verify validation of an incorrectly formatted email address.",
                "preconditions": "Password reset page is available.",
                "test_steps": [
                    "Open the password reset page.",
                    "Enter an invalid email format.",
                    "Submit the reset request."
                ],
                "expected_result": "The system displays an appropriate email validation message.",
                "test_data": "invalid-email"
            },
            {
                "id": "TC004",
                "title": "Reset password with empty email",
                "type": "Negative",
                "priority": "High",
                "description": "Verify that the reset request cannot be submitted without an email.",
                "preconditions": "Password reset page is available.",
                "test_steps": [
                    "Open the password reset page.",
                    "Leave the email field empty.",
                    "Submit the reset request."
                ],
                "expected_result": "The system requires the email field and does not submit the request.",
                "test_data": "Empty value"
            },
            {
                "id": "TC005",
                "title": "Reset password using an expired reset link",
                "type": "Negative",
                "priority": "High",
                "description": "Verify that an expired password reset link cannot be used.",
                "preconditions": "A password reset link has expired.",
                "test_steps": [
                    "Open the expired password reset link.",
                    "Attempt to define a new password."
                ],
                "expected_result": "The system rejects the expired link and asks the user to request a new reset link.",
                "test_data": "Expired reset token"
            }
        ])
    else:
        test_cases.append({
            "id": "TC001",
            "title": "Valid scenario",
            "type": "Positive",
            "priority": "High",
            "description": "Verify the main successful user flow.",
            "preconditions": "Required application conditions are satisfied.",
            "test_steps": [
                "Execute the main user flow."
            ],
            "expected_result": "The requested operation is completed successfully.",
            "test_data": "Valid input"
        })

    for test_case in test_cases:
        if "automation_code" not in test_case:
            test_case["automation_code"] = generate_automation_code(test_case)

    return {
        "requirement": requirement,
        "analysis": analysis,
        "test_cases": test_cases
    }




