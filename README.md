# AI-Powered QA Test Generator

A Python-based QA Engineering project that transforms software requirements into structured test cases, BDD/Gherkin scenarios, test data, edge cases, priorities, and Playwright automation code.

The project currently provides a rule-based test generation foundation and is designed for future integration with Generative AI and Large Language Models (LLMs).

## Project Overview

The goal of this project is to explore how Artificial Intelligence can support Software Quality Engineering by reducing the manual effort required to analyze requirements and design comprehensive test scenarios.

Given a software requirement such as:

> User should be able to reset their password using their registered email.

The system analyzes the requirement and generates a structured test suite containing:

* Positive and negative scenarios
* Test case descriptions
* Preconditions
* Test steps
* Expected results
* Test data
* Edge cases
* Priority classification
* BDD/Gherkin scenarios
* Playwright automation suggestions
* Playwright automation code

## Example

### Input

```text
User should be able to reset their password using their registered email.
```

### Generated Test Cases

| ID    | Scenario                                   | Type     | Priority |
| ----- | ------------------------------------------ | -------- | -------- |
| TC001 | Reset password with valid registered email | Positive | High     |
| TC002 | Reset password with unregistered email     | Negative | High     |
| TC003 | Reset password with invalid email format   | Negative | Medium   |
| TC004 | Reset password with empty email            | Negative | High     |
| TC005 | Reset password using an expired reset link | Negative | High     |

## Key Features

### Requirement Analysis

The system analyzes the input requirement and identifies relevant concepts such as:

* Email
* Password
* Login
* Password reset

### Structured Test Case Generation

Each generated test case can contain:

* Test case ID
* Title
* Type
* Priority
* Description
* Preconditions
* Steps
* Expected result
* Test data
* Edge cases
* Automation suggestion
* Automation code

### BDD / Gherkin

The generator produces BDD scenarios using the standard:

```text
Given
When
Then
```

structure.

### Playwright Automation

The project generates Playwright automation code associated with each test scenario.

Example:

```python
from playwright.sync_api import Page, expect


def test_reset_password(page: Page):
    page.goto("/forgot-password")
    page.fill("#email", "registered_user@example.com")
    page.click("button[type='submit']")
    expect(page.get_by_text("Check your email")).to_be_visible()
```

The generated code is intended as an automation starting point and must be adapted to the actual application.

### JSON Export

Generated test suites are exported to:

```text
data/generated/test_cases.json
```

This makes the generated results available for further processing, reporting, or integration with other QA tools.

## Architecture

```text
Software Requirement
        |
        v
Requirement Analysis
        |
        v
Test Case Generation
        |
        +--------------------+
        |                    |
        v                    v
   BDD / Gherkin        Test Data
        |                    |
        +----------+---------+
                   |
                   v
           Edge Case Analysis
                   |
                   v
        Playwright Generation
                   |
                   v
          Automation Code
                   |
                   v
              JSON Export
```

## Project Structure

```text
03-ai-powered-qa-test-generator/
|
+-- data/
|   +-- generated/
|       +-- reset_password_test_cases.json
|       +-- test_cases.json
|
+-- src/
|   +-- __init__.py
|   +-- ai_generator.py
|   +-- automation_generator.py
|   +-- config.py
|   +-- export_results.py
|   +-- main.py
|   +-- qa_test_generator.py
|
+-- tests/
|   +-- test_qa_test_generator.py
|
+-- .env.example
+-- .gitignore
+-- pytest.ini
+-- requirements.txt
+-- README.md
```

## Technology Stack

| Technology        | Purpose                         |
| ----------------- | ------------------------------- |
| Python 3.12       | Core development language       |
| Pytest            | Automated testing               |
| Playwright        | UI test automation generation   |
| Pandas            | Data processing foundation      |
| NumPy             | Numerical processing foundation |
| OpenAI Python SDK | Future LLM integration          |
| Python Dotenv     | Environment configuration       |
| JSON              | Test result export              |
| BDD / Gherkin     | Behavior-driven test scenarios  |
| Git / GitHub      | Version control and portfolio   |

## Running the Project

### 1. Activate the virtual environment

```powershell
.\.venv\Scripts\Activate.ps1
```

### 2. Run the test generator

The project is executed as a Python module:

```powershell
python -m src.main
```

### 3. Enter a requirement

For example:

```text
User should be able to reset their password using their registered email.
```

The application generates the test suite and saves the results to:

```text
data/generated/test_cases.json
```

## Running Automated Tests

Execute:

```powershell
pytest -v
```

The current automated test suite validates:

* Test case generation
* Positive scenario generation
* Negative scenario generation
* Automation code generation
* Playwright code generation

## Current Test Results

The current project test suite contains five automated tests.

Expected result:

```text
5 passed
```

## GenAI Integration

The project includes a dedicated GenAI integration layer:

```text
src/ai_generator.py
```

The current implementation is intentionally a placeholder.

The project is therefore **not currently dependent on an external LLM API** to generate its test cases.

Instead, the current version establishes the software architecture and QA generation pipeline that can later be connected to a real Generative AI model.

### Planned GenAI capabilities

Future versions can include:

* LLM-based requirement analysis
* AI-generated test cases
* Intelligent edge-case generation
* AI-based test prioritization
* Gherkin generation
* Test data generation
* AI-generated Playwright automation
* Requirement-to-test traceability
* AI-assisted test maintenance
* Comparison between rule-based and LLM-generated test suites

## QA Automation + Data + AI

This project is part of a broader portfolio exploring the intersection of:

```
```
