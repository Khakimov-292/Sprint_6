import allure
from conftest import driver
from pages.base_page import BasePage


class TestURL:
    @allure.title('Проверка ссылки логотипа')
    def test_main_page(self, driver):
        base_page = BasePage()
        base_page.open_browser(driver)
        base_page.click_order_button(driver)
        base_page.click_scooter_button(driver)
        base_page.should_main_page_url(driver)

    @allure.title('Проверка ссылки "Яндекс"')
    def test_dzen_url(self, driver):
        base_page = BasePage()
        base_page.open_browser(driver)
        base_page.click_dzen_button(driver)
        base_page.switching_to_the_tab(driver)
        base_page.wait_for_page_load(driver)
        base_page.should_dzen_url(driver)