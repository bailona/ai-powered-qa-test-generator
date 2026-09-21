from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()


def generate_with_ai(requirement):
    prompt = f"""
You are a senior QA Automation Engineer and Software Test Analyst.

Analyze the following software requirement:

{requirement}

Generate a structured QA analysis containing:

1. Positive test scenarios
2. Negative test scenarios
3. Edge cases
4. Test data suggestions
5. Priority for each scenario: High, Medium, or Low
6. Gherkin/BDD scenarios
7. Automation suggestions using Playwright with Python

Keep the response practical and focused on software testing.

Do not invent application-specific behavior unless it is clearly identified
as an assumption.
"""

    try:
        response = client.responses.create(
            model="gpt-5.6-luna",
            input=prompt
        )

        usage = response.usage

        return {
            "requirement": requirement,
            "provider": "OpenAI",
            "model": "gpt-5.6-luna",
            "status": "connected",
            "generated_content": response.output_text,
            "usage": {
                "input_tokens": usage.input_tokens,
                "output_tokens": usage.output_tokens,
                "total_tokens": usage.total_tokens
            }
        }

    except Exception as error:
        return {
            "requirement": requirement,
            "provider": "OpenAI",
            "model": "gpt-5.6-luna",
            "status": "error",
            "generated_content": "",
            "error": str(error),
            "usage": {
                "input_tokens": 0,
                "output_tokens": 0,
                "total_tokens": 0
            }
        }
