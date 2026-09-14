# Target file: tests/test_end_to_end_complete_shopping_journey_on_swag_labs.py
# Generated execution model:
# - language: python
# - test_framework: pytest
# - playwright_api: sync_api
# Run completion: FULL
# Future page files:
# - pages/login_page.py
# - pages/listing_page.py
# - pages/product_detail_page.py
# - pages/cart_page.py
# - pages/content_page.py
# - pages/step_two_page.py

import os
import pytest
import re
from playwright.sync_api import Page, expect

@pytest.fixture
def vtest_base_url() -> str:
    return 'https://www.saucedemo.com/'

@pytest.fixture
def test_data() -> dict:
    return {
        'username': 'standard_user',
        'password': os.environ.get('VTEST_DATA_PASSWORD', ""),
        'first_name': 'John',
        'last_name': 'Doe',
        'postal_code': '12345',
    }

class LoginPage:
    PAGE_TYPE = 'login'
    LOCATOR_1 = '#user-name'
    LOCATOR_2 = '#password'
    LOCATOR_3 = '#login-button'

    def enter_standard_user_into_the_username_field(self, page: Page, test_data: dict) -> None:
        page.locator('#user-name').fill(test_data['username'])
        expect(page.locator('#user-name')).to_have_value(test_data['username'])

    def enter_secret_sauce_into_the_password_field(self, page: Page, test_data: dict) -> None:
        page.locator('#password').fill(test_data['password'])
        expect(page.locator('#password')).to_have_value(test_data['password'])

    def click_the_login_button(self, page: Page, test_data: dict) -> None:
        page.locator('#login-button').click()


class ListingPage:
    PAGE_TYPE = 'listing'
    LOCATOR_1 = '#item_4_title_link'

    def click_the_sauce_labs_backpack_product_link(self, page: Page, test_data: dict) -> None:
        page.locator('#item_4_title_link').click()


class ProductDetailPage:
    PAGE_TYPE = 'product_detail'
    LOCATOR_1 = '#add-to-cart'
    LOCATOR_2 = 'a[data-test="shopping-cart-link"]'

    def click_the_add_to_cart_button(self, page: Page, test_data: dict) -> None:
        page.locator('#add-to-cart').click()

    def click_the_cart_icon(self, page: Page, test_data: dict) -> None:
        page.locator('a[data-test="shopping-cart-link"]').click()


class CartPage:
    PAGE_TYPE = 'cart'
    LOCATOR_1 = '#checkout'

    def click_the_checkout_button(self, page: Page, test_data: dict) -> None:
        page.locator('#checkout').click()


class ContentPage:
    PAGE_TYPE = 'content'
    LOCATOR_1 = '#first-name'
    LOCATOR_2 = '#last-name'
    LOCATOR_3 = '#postal-code'
    LOCATOR_4 = '#continue'

    def enter_john_into_the_first_name_field(self, page: Page, test_data: dict) -> None:
        page.locator('#first-name').fill(test_data['first_name'])
        expect(page.locator('#first-name')).to_have_value(test_data['first_name'])

    def enter_doe_into_the_last_name_field(self, page: Page, test_data: dict) -> None:
        page.locator('#last-name').fill(test_data['last_name'])
        expect(page.locator('#last-name')).to_have_value(test_data['last_name'])

    def enter_12345_into_the_postal_code_field(self, page: Page, test_data: dict) -> None:
        page.locator('#postal-code').fill(test_data['postal_code'])
        expect(page.locator('#postal-code')).to_have_value(test_data['postal_code'])

    def click_the_continue_button(self, page: Page, test_data: dict) -> None:
        page.locator('#continue').click()


class StepTwoPage:
    PAGE_TYPE = 'step_two'
    LOCATOR_1 = '#finish'

    def click_the_finish_button(self, page: Page, test_data: dict) -> None:
        page.locator('#finish').click()


def test_end_to_end_complete_shopping_journey_on_swag_labs(page: Page, vtest_base_url: str, test_data: dict) -> None:
    page.goto(vtest_base_url)

    login_page = LoginPage()
    listing_page = ListingPage()
    product_detail_page = ProductDetailPage()
    cart_page = CartPage()
    content_page = ContentPage()
    step_two_page = StepTwoPage()

    login_page.enter_standard_user_into_the_username_field(page, test_data)
    login_page.enter_secret_sauce_into_the_password_field(page, test_data)
    login_page.click_the_login_button(page, test_data)
    listing_page.click_the_sauce_labs_backpack_product_link(page, test_data)
    product_detail_page.click_the_add_to_cart_button(page, test_data)
    product_detail_page.click_the_cart_icon(page, test_data)
    cart_page.click_the_checkout_button(page, test_data)
    content_page.enter_john_into_the_first_name_field(page, test_data)
    content_page.enter_doe_into_the_last_name_field(page, test_data)
    content_page.enter_12345_into_the_postal_code_field(page, test_data)
    content_page.click_the_continue_button(page, test_data)
    step_two_page.click_the_finish_button(page, test_data)

    assert 'checkout-complete.html' in page.url
    expect(page.locator('body')).to_contain_text('Thank you for your order!')