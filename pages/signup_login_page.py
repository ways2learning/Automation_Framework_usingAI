from pages.base_page import BasePage

class SignupLoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

    def is_login_form_visible(self):
        # Checks if the login form heading is visible
        return self.page.locator("div.login-form").is_visible()

    def login(self, email, password):
        self.page.fill("input[data-qa='login-email']", email)
        self.page.fill("input[data-qa='login-password']", password)
        self.page.click("button[data-qa='login-button']")

    def is_login_error_visible(self):
        # Looks for the login error message after failed login
        return self.page.locator("p:has-text('Your email or password is incorrect!')").is_visible()