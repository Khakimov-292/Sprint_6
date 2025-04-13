import allure
from conftest import driver
from data import Urls
from pages.main_page import MainPage


class TestURL:
    @allure.title('Проверка ссылки логотипа')
    def test_main_page(self, driver):
        page = MainPage(driver)
        page.open_browser()
        page.click_order_button()
        page.click_scooter_button()
        actual_url = page.receiving_current_url
        assert actual_url == Urls.MAIN_PAGE_URL

    @allure.title('Проверка ссылки "Яндекс"')
    def test_dzen_url(self, driver):
        page = MainPage(driver)
        page.open_browser()
        page.click_dzen_button()
        page.switching_to_the_tab()
        page.wait_for_page_load()
        actual_url = page.receiving_current_url
        assert actual_url == Urls.DZEN_URL
