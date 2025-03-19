import allure
from base_pages.base_page import BasePage
from locators.personal_account_locators import Locators_account
import time

class AccountPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Находим на странице кнопку Личный кабинет и переходим по ней.')
    def press_button_personal_account(self, locator, locator_text):
        self.wait_visibility_of_element(locator)
        self.click_on_element(locator)
        self.wait_visibility_of_element(locator_text)

        return self.current_urls()

    @allure.step('Авторизуемся.')
    def login(self, email, password):
        self.wait_visibility_of_element(Locators_account.personal_account)
        self.click_on_element(Locators_account.personal_account)
        self.wait_visibility_of_element(Locators_account.entrance)
        self.find_element_on_page(Locators_account.field_email).send_keys(email)
        self.find_element_on_page(Locators_account.field_password).send_keys(password)
        self.click_on_element(Locators_account.button_entrance)

    @allure.step('Переходим в Личный кабинет.')
    def go_to_personal_account(self):
        self.wait_visibility_of_element(Locators_account.personal_account)
        self.click_on_element(Locators_account.personal_account)
        self.wait_visibility_of_element(Locators_account.order_history)

    @allure.step('Переходим в раздел История заказов.')
    def order_history_focused(self):
        self.click_on_element(Locators_account.order_history)
        time.sleep(1)

        return self.check_element_is_focused(Locators_account.order_history)

    @allure.step('Выходим из аккаунта.')
    def logout_of_account(self):
        self.click_on_element(Locators_account.button_exit)
        self.wait_visibility_of_element(Locators_account.button_entrance)

        return self.current_urls()
