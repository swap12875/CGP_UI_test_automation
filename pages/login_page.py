from playwright.sync_api import Page, expect

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.username_input = page.locator('input[name="username"]')
        self.password_input = page.locator('input[name="password"]')
        self.login_button = page.locator('button[type="submit"]')
        self.error_message = page.locator('.oxd-alert-content-text')

    def navigate(self):
        self.page.goto('/')
        # Wait for the login form to be visible
        expect(self.username_input).to_be_visible(timeout=10000)

    def login(self, username: str, password: str):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()

    def get_error_message(self) -> str:
        self.error_message.wait_for(timeout=5000)
        return self.error_message.text_content()
