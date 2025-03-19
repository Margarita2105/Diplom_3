import allure

from base_pages.base_page import BasePage
from locators.basic_functionality_locators import Locators_functionality
from tests.conftest import driver
from locators.personal_account_locators import Locators_account


class FunctionalityPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Находим на странице нужную кнопку и переходим по ней.')
    def press_button(self, locator):
        self.click_on_element(locator)

        return self.current_urls()

    @allure.step('Находим на странице ингредиент и нажимаем на него.')
    def press_button_ingredient(self, locator, locator_next):
        self.wait_visibility_of_element(locator)
        element = self.find_element_on_page(locator)
        self.scroll(element)
        self.click_on_element(locator)
        self.wait_visibility_of_element(locator_next)

        return self.text_of_element(locator_next)

    @allure.step('Закрываем карточку ингредиента.')
    def exit_ingredient(self, locator, locator_exit, locator_next, locator_main):
        self.press_button_ingredient(locator, locator_next)
        self.wait_visibility_of_element(locator_exit)
        self.click_on_element(locator_exit)
        self.wait_visibility_of_element(locator_main)
        self.click_on_element(locator_main)

        return self.check_element_is_focused(locator_exit)

    @allure.step('Перетаскиваем ингредиент, получаем увеличение каунтера.')
    def count(self, dry, element_from, element_to, count):
        before = self.text_of_element(count)
        self.drag_and_drop(dry, element_from, element_to)
        after = self.text_of_element(count)

        return after > before

    @allure.step('Создаем заказ.')
    def order_user(self, dry, element_from, element_to, place, cook, email, password):
        self.login(email, password)
        self.drag_and_drop(dry, element_from, element_to)
        self.wait_visibility_of_element(place)
        self.click_on_element(place)
        self.wait_visibility_of_element(cook)

        return self.text_of_element(cook)

    @allure.step('Авторизуемся.')
    def login(self, email, password):
        self.wait_visibility_of_element(Locators_account.personal_account)
        self.click_on_element(Locators_account.personal_account)
        self.wait_visibility_of_element(Locators_account.entrance)
        self.find_element_on_page(Locators_account.field_email).send_keys(email)
        self.find_element_on_page(Locators_account.field_password).send_keys(password)
        self.click_on_element(Locators_account.button_entrance)
        self.click_on_element(Locators_functionality.constructor)
