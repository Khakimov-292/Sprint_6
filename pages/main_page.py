import allure

from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):

    @allure.step("Переход к вопросу")
    def scroll_to_faq(self):
        self.go_to_element(MainPageLocators.QUESTION)

    @allure.step("Извлечение вопроса")
    def get_question(self, index):
        question_locator = (MainPageLocators.QUESTION[0], MainPageLocators.QUESTION[1].format(index))
        question = self.wait_for_clickable(question_locator)
        question.click()
        return question.text

    @allure.step("Извлечение ответа")
    def get_answers(self, index):
        answers_locator = (MainPageLocators.ANSWER[0], MainPageLocators.ANSWER[1].format(index))
        answers = self.find_element(*answers_locator)
        return answers.text

