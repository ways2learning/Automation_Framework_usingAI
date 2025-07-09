from pages.base_page import BasePage

class ContactPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

    def is_form_displayed(self):
        # Verify contact form is present
        return self.page.locator("form[method='post']").is_visible()

    def submit_form(self, name, email, subject, message):
        self.page.fill("input[data-qa='name']", name)
        self.page.fill("input[data-qa='email']", email)
        self.page.fill("input[data-qa='subject']", subject)
        self.page.fill("textarea[data-qa='message']", message)

        # Uploading a dummy file if required (you can remove this line if unnecessary)
        self.page.set_input_files("input[name='upload_file']", "test_data/sample.txt")

        self.page.click("input[data-qa='submit-button']")
        self.page.on("dialog", lambda dialog: dialog.accept())  # Accept alert if shown

    def is_success_message_visible(self):
        # Confirm the success message appears
        return self.page.locator("div.status.alert-success").is_visible()