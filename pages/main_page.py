import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from conftest import driver
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):

    @allure.step("Переход к вопросу")
    def scroll_to_faq(self, driver):
        element = driver.find_element(By.CLASS_NAME, "accordion")
        driver.execute_script("arguments[0].scrollIntoView(true);", element)

    @allure.step("Извлечение вопроса")
    def get_question(self, driver, index):
        question_locator = (MainPageLocators.QUESTION[0], MainPageLocators.QUESTION[1].format(index))
        question = WebDriverWait(driver, 3).until(ec.element_to_be_clickable(question_locator))
        question.click()
        return question.text

    @allure.step("Извлечение ответа")
    def get_answers(self, driver, index):
        answers_locator = (MainPageLocators.ANSWER[0], MainPageLocators.ANSWER[1].format(index))
        answers = driver.find_element(*answers_locator)
        return answers.text

