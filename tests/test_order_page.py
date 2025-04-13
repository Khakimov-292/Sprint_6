import allure
import pytest
from data import OrderData
from locators.order_page_locators import OrderLocators
from pages.order_page import OrderPage
from conftest import driver


class TestOrderPage:
    @allure.title('Проверка заказа самоката')
    @allure.description('Проверяем сценария с двумя наборами данных')
    @pytest.mark.parametrize('button_method, data_order', [('click_first_button', OrderData.FIRST_ORDER),
                                                           ('click_second_button', OrderData.SECOND_ORDER)])
    def test_make_an_order(self, driver, data_order, button_method):
        page = OrderPage(driver)
        page.open_browser()
        getattr(page, button_method)()
        page.user_rent_order(**data_order)
        status = page.find_element(*OrderLocators.ORDER_STATUS)
        assert 'Заказ оформлен' in status.text

