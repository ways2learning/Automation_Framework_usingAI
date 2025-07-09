import pytest
from pages.contact_page import ContactPage

@pytest.mark.web
def test_contact_form_presence(page, config):
    contact = ContactPage(page)
    contact.navigate(config.get_base_url() + "/contact_us")
    assert contact.is_form_displayed()

@pytest.mark.web
def test_submit_contact_form(page, config):
    contact = ContactPage(page)
    contact.navigate(config.get_base_url() + "/contact_us")
    contact.submit_form("John", "john@example.com", "Subject", "Message")
    assert contact.is_success_message_visible()