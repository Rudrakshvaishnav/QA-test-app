# Target file: tests/test_verify_successful_flight_ticket_booking.py
# Generated execution model:
# - language: python
# - test_framework: pytest
# - playwright_api: sync_api
# Run completion: FULL
# Future page files:
# - pages/home_page.py
# - pages/reserve_page.py
# - pages/purchase_page.py

import pytest
import re
from playwright.sync_api import Page, expect

@pytest.fixture
def vtest_base_url() -> str:
    return 'https://blazedemo.com/'

class HomePage:
    PAGE_TYPE = 'home'
    LOCATOR_1 = 'select[name="fromPort"]'
    LOCATOR_2 = 'select[name="toPort"]'
    LOCATOR_3 = 'input.btn'

    def select_boston_as_the_departure_city(self, page: Page) -> None:
        page.locator('select[name="fromPort"]').select_option('Boston')

    def select_london_as_the_destination_city(self, page: Page) -> None:
        page.locator('select[name="toPort"]').select_option('London')

    def click_the_find_flights_button(self, page: Page) -> None:
        page.locator('input.btn').click()


class ReservePage:
    PAGE_TYPE = 'reserve'
    LOCATOR_1 = 'body:nth-of-type(1) > div:nth-of-type(2) > table:nth-of-type(1) > tbody:nth-of-type(1) > tr:nth-of-type(1) > td:nth-of-type(1) > input:nth-of-type(1)'

    def select_the_first_available_flight(self, page: Page) -> None:
        page.locator('body:nth-of-type(1) > div:nth-of-type(2) > table:nth-of-type(1) > tbody:nth-of-type(1) > tr:nth-of-type(1) > td:nth-of-type(1) > input:nth-of-type(1)').click()


class PurchasePage:
    PAGE_TYPE = 'purchase'
    LOCATOR_1 = '#inputName'
    LOCATOR_2 = '#address'
    LOCATOR_3 = '#city'
    LOCATOR_4 = '#state'
    LOCATOR_5 = '#zipCode'
    LOCATOR_6 = '#creditCardNumber'
    LOCATOR_7 = 'input.btn'

    def enter_john_doe_into_the_name_field(self, page: Page) -> None:
        page.locator('#inputName').fill('John Doe')
        expect(page.locator('#inputName')).to_have_value('John Doe')

    def enter_742_evergreen_terrace_into_the_address_field(self, page: Page) -> None:
        page.locator('#address').fill('742 Evergreen Terrace')
        expect(page.locator('#address')).to_have_value('742 Evergreen Terrace')

    def enter_springfield_into_the_city_field(self, page: Page) -> None:
        page.locator('#city').fill('Springfield')
        expect(page.locator('#city')).to_have_value('Springfield')

    def enter_il_into_the_state_field(self, page: Page) -> None:
        page.locator('#state').fill('IL')
        expect(page.locator('#state')).to_have_value('IL')

    def enter_62704_into_the_zip_code_field(self, page: Page) -> None:
        page.locator('#zipCode').fill('62704')
        expect(page.locator('#zipCode')).to_have_value('62704')

    def enter_4111111111111111_into_the_card_number_field(self, page: Page) -> None:
        page.locator('#creditCardNumber').fill('4111111111111111')
        expect(page.locator('#creditCardNumber')).to_have_value('4111111111111111')

    def click_the_complete_purchase_button(self, page: Page) -> None:
        page.locator('input.btn').click()


def test_verify_successful_flight_ticket_booking(page: Page, vtest_base_url: str) -> None:
    page.goto(vtest_base_url)

    home_page = HomePage()
    reserve_page = ReservePage()
    purchase_page = PurchasePage()

    home_page.select_boston_as_the_departure_city(page)
    home_page.select_london_as_the_destination_city(page)
    home_page.click_the_find_flights_button(page)
    reserve_page.select_the_first_available_flight(page)
    purchase_page.enter_john_doe_into_the_name_field(page)
    purchase_page.enter_742_evergreen_terrace_into_the_address_field(page)
    purchase_page.enter_springfield_into_the_city_field(page)
    purchase_page.enter_il_into_the_state_field(page)
    purchase_page.enter_62704_into_the_zip_code_field(page)
    purchase_page.enter_4111111111111111_into_the_card_number_field(page)
    purchase_page.click_the_complete_purchase_button(page)

    assert 'confirmation.php' in page.url
    expect(page.locator('body')).to_contain_text('Thank you for your purchase today!')