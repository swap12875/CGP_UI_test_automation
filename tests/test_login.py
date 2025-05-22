import pytest
from playwright.sync_api import Page, expect
from pages.login_page import LoginPage

USERNAME = 'Admin'
PASSWORD = 'admin123'

def test_successful_login(page: Page):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login(USERNAME, PASSWORD)
    
    # Verify successful login
    expect(page).to_have_url('/web/index.php/dashboard/index')
    dashboard_header = page.locator('.oxd-topbar-header-breadcrumb')
    expect(dashboard_header).to_be_visible()
    expect(dashboard_header).to_contain_text('Dashboard')

def test_invalid_credentials(page: Page):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login('invaliduser', 'invalidpass')
    
    # Verify error message
    error_message = login_page.get_error_message()
    assert 'Invalid credentials' in error_message
