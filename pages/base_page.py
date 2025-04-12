import allure
from data import Urls
from locators.base_page_locators import BasePageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as eс
from locators.order_page_locators import OrderLocators


class BasePage:

    @allure.step("Открытие браузера")
    def open_browser(self, driver):
        driver.get(Urls.MAIN_PAGE_URL)

    @allure.step('Нажатие на кнопку "Заказать" в шапке')
    def click_order_button(self, driver):
        driver.find_element(*OrderLocators.ORDER_BUTTON_HEADER).click()

    @allure.step('Нажатие на логотип "Самокат"')
    def click_scooter_button(self, driver):
        driver.find_element(*BasePageLocators.SCOOTER_BUTTON).click()

    @allure.step('Нажатие на логотип "Дзен"')
    def click_dzen_button(self, driver):
        driver.find_element(*BasePageLocators.YANDEX_BUTTON).click()

    @allure.step("Переключение вкладки")
    def switching_to_the_tab(self, driver):
        driver.switch_to.window(driver.window_handles[1])

    @allure.step("Ожидание загрузки страницы")
    def wait_for_page_load(self, driver):
        WebDriverWait(driver, 10).until(
            eс.url_to_be(Urls.DZEN_URL))

    @allure.step("Ожидание пока элемент будет кликабельным")
    def wait_for_clickable(self, locator):
        return WebDriverWait(self.driver, 3).until(ec.element_to_be_clickable(locator))

    @allure.step("Поиск элемента")
    def find_element(self, locator):
        return self.driver.find_element(*locator)

    @allure.step("Переход до нужного элемента")
    def go_to_element(self, locator):
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

