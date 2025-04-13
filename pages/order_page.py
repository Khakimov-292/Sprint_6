import allure
from locators.order_page_locators import OrderLocators
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage


class OrderPage(BasePage):

    @allure.step('Нажатие по кнопке "Заказать" в шапке')
    def click_first_button(self):
        self.find_element(*OrderLocators.ORDER_BUTTON_HEADER).click()

    @allure.step('Нажатие по кнопке "Заказать" в центре формы')
    def click_second_button(self):
        self.go_to_element(*OrderLocators.ORDER_CENTER_BUTTON)

    @allure.step('Заполнение поля "Имя"')
    def user_name(self, name):
        self.find_element(*OrderLocators.NAME).send_keys(name)

    @allure.step('Заполнение поля "Фамилия"')
    def user_last_name(self, last_name):
        self.find_element(*OrderLocators.LAST_NAME).send_keys(last_name)

    @allure.step('Заполнение поля "Адрес"')
    def user_address(self, address):
        self.find_element(*OrderLocators.ADDRESS).send_keys(address)

    @allure.step('Заполнение поля "Метро"')
    def metro(self, metro):
        self.find_element(*OrderLocators.METRO).send_keys(metro)
        self.find_element(*OrderLocators.LIST_STATION).click()

    @allure.step('Заполнение поля "Телефон"')
    def user_phone(self, phone):
        self.find_element(*OrderLocators.NUMBER).send_keys(phone)

    @allure.step('Нажатие на кнопку "Далее"')
    def click_button_next(self):
        self.find_element(*OrderLocators.NEXT_BUTTON).click()

    @allure.step('Заполнение поля "Дата доставки"')
    def date_of_delivery(self, data):
        (self.find_element(*OrderLocators.DATE_DELIVERY)
         .send_keys(data, Keys.ENTER))

    @allure.step('Заполнение поля "Время аренды"')
    def rental_time(self, day):
        self.find_element(*OrderLocators.RENT_TIME).click()
        select_rent_time_locator = (OrderLocators.SELECT_RENT_TIME[0], OrderLocators.SELECT_RENT_TIME[1].format(day))
        self.find_element(*select_rent_time_locator).click()

    @allure.step("Выбор цвета")
    def checkbox_color(self, color):
        if color == 'чёрный жемчуг':
            self.find_element(*OrderLocators.BLACK_COLOR_CHECKBOX).click()
        elif color == 'серая безысходность':
            self.find_element(*OrderLocators.GREY_COLOR_CHECKBOX).click()

    @allure.step('Заполнение поля "Комментарии к заказу"')
    def comment_for_courier(self, comment):
        self.find_element(*OrderLocators.COMMENT).send_keys(comment)

    @allure.step("Нажатие на кнопку Заказать")
    def click_button_order(self):
        self.find_element(*OrderLocators.ORDER_BUTTON).click()

    @allure.step("Нажатие на кнопку 'Да' в окне подтверждения заказа")
    def click_button_confirmations(self):
        self.find_element(*OrderLocators.YES_BUTTON).click()

    @allure.step("Проверка текста окна подтверждения заказа")
    def confirmation_window(self):
        text = self.find_element(*OrderLocators.ORDER_COMPLETED).text
        assert 'Заказ оформлен' in text

    @allure.step("Весь сценарий сценарий")
    def user_rent_order(self,
                        name, last_name, address, metro, number,
                        delivery_date, rent_days, colour, comment):
        self.user_name(name)
        self.user_last_name(last_name)
        self.user_address(address)
        self.metro(metro)
        self.user_phone(number)
        self.click_button_next()
        self.date_of_delivery(delivery_date)
        self.rental_time(rent_days)
        self.checkbox_color(colour)
        self.comment_for_courier(comment)
        self.click_button_order()
        self.click_button_confirmations()
        self.confirmation_window()
