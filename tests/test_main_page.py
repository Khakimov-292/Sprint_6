import allure
import pytest
from conftest import driver
from pages.main_page import MainPage
from data import QuestionsAndAnswers


class TestMainPage:
    @allure.title('Проверка ответов в разделе "Вопросы о важном"')
    @allure.description('Проверяем, что по нажатию на стрелочку с вопросом, открывается нужный ответ')
    @pytest.mark.parametrize('index, question, answer', QuestionsAndAnswers.QUESTIONS_AND_ANSWERS_LIST)
    def test_check_question_and_answer(self, driver, index, question, answer):
        page = MainPage(driver)
        page.open_browser()
        page.scroll_to_faq()
        answer_text = page.get_answers(index)
        question_text = page.get_question(index)
        assert answer_text == answer
        assert question_text == question
