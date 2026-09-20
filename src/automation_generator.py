def generate_automation_code(test_case):
    test_id = test_case.get("id", "TC001")

    if test_id == "TC001":
        return '''from playwright.sync_api import Page, expect


def test_reset_password(page: Page):
    page.goto("/forgot-password")
    page.fill("#email", "registered_user@example.com")
    page.click("button[type='submit']")
    expect(page.get_by_text("Check your email")).to_be_visible()
'''

    if test_id == "TC002":
        return '''from playwright.sync_api import Page, expect


def test_reset_password_unregistered_email(page: Page):
    page.goto("/forgot-password")
    page.fill("#email", "unknown_user@example.com")
    page.click("button[type='submit']")
    expect(page.get_by_text("Check your email")).to_be_visible()
'''

    if test_id == "TC003":
        return '''from playwright.sync_api import Page, expect


def test_reset_password_invalid_email(page: Page):
    page.goto("/forgot-password")
    page.fill("#email", "invalid-email")
    page.click("button[type='submit']")
    expect(page.get_by_text("valid email")).to_be_visible()
'''

    if test_id == "TC004":
        return '''from playwright.sync_api import Page, expect


def test_reset_password_empty_email(page: Page):
    page.goto("/forgot-password")
    page.click("button[type='submit']")
    expect(page.get_by_text("required")).to_be_visible()
'''

    if test_id == "TC005":
        return '''from playwright.sync_api import Page, expect


def test_reset_password_expired_link(page: Page):
    page.goto("/forgot-password?token=expired")
    expect(page.get_by_text("expired")).to_be_visible()
'''

    return '''from playwright.sync_api import Page


def test_generated_scenario(page: Page):
    page.goto("/forgot-password")
'''
