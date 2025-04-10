import allure
import pytest
from data import OrderData
from pages.order_page import OrderPage
from conftest import driver


class TestOrderPage:
    @allure.title('Проверка заказа самоката')
    @allure.description('Проверяем сценария с двумя наборами данных')
    @pytest.mark.parametrize('button_method, data_order', [('click_first_button', OrderData.FIRST_ORDER),
                                                           ('click_second_button', OrderData.SECOND_ORDER)])
    def test_make_an_order(self, driver, data_order, button_method):
        page = OrderPage()
        page.open_browser(driver)
        getattr(page, button_method)(driver)
        page.user_rent_order(driver, **data_order)
        page.confirmation_window(driver)


