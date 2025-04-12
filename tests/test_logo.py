import allure
from conftest import driver
from data import Urls
from pages.base_page import BasePage


class TestURL:
    @allure.title('Проверка ссылки логотипа')
    def test_main_page(self, driver):
        base_page = BasePage(driver)
        base_page.open_browser()
        base_page.click_order_button()
        base_page.click_scooter_button()
        assert driver.current_url == Urls.MAIN_PAGE_URL

    @allure.title('Проверка ссылки "Яндекс"')
    def test_dzen_url(self, driver):
        base_page = BasePage(driver)
        base_page.open_browser()
        base_page.click_dzen_button()
        base_page.switching_to_the_tab()
        base_page.wait_for_page_load()
        assert driver.current_url == Urls.DZEN_URL
