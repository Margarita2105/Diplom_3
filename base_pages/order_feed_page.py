import allure

from api.api_methods import ApiMethods
from base_pages.base_page import BasePage
from data import Ingredient
from locators.basic_functionality_locators import Locators_functionality
from locators.order_feed_locators import Locators_feed
from locators.personal_account_locators import Locators_account
import time
from selenium.webdriver.common.by import By



class FeedPage(BasePage):

    def __init__(self, driver):
        BasePage.__init__(self, driver)

    @allure.step('Нажимаем на заказ, получаем открытое окно с заказом.')
    def press_order(self, locator, locator_next):
        self.wait_visibility_of_element(locator)
        element = self.find_element_on_page(locator)
        self.scroll(element)
        self.click_on_element(locator)
        self.wait_visibility_of_element(locator_next)

        return self.text_of_element(locator_next)

    @allure.step('Находим на странице заказ и нажимаем на него.')
    def order_in_feed(self, account, order_user, history):
        self.click_on_element(account)
        self.wait_visibility_of_element(history)
        time.sleep(1)
        self.click_on_element(history)
        time.sleep(1)
        self.find_element_on_page(order_user)
        id_in_account = self.text_of_element(order_user)
        self.click_on_element(Locators_feed.order_feed)
        time.sleep(1)
        locator = (By.XPATH, f".//p[text()='{id_in_account}']")
        order_in_feed = self.find_element_on_page(locator)
        return order_in_feed

    @allure.step('Создаем заказ.')
    def order_user(self, dry, element_from, element_to, place, cook, email, password):
        self.login(email, password)
        self.drag_and_drop(dry, element_from, element_to)
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
        self.wait_visibility_of_element(Locators_account.personal_account)
        self.click_on_element(Locators_account.personal_account)
        time.sleep(5)

    @allure.step('Получаем значения счетчиков до и поле заказа.')
    def counter_orders(self, counter, mail, password):
        time.sleep(5)
        count = self.text_of_element(counter)
        ApiMethods.order_new(mail, password, Ingredient.ingredient)
        time.sleep(5)
        count_after = self.text_of_element(counter)

        return count_after > count

    @allure.step('Получаем номер нового заказа в разделе В работе.')
    def number_order(self, number, finaly):
        time.sleep(4)
        number_order = self.text_of_element(number)
        final = self.text_of_element(finaly)
        number_order_final = str(number_order) + str(final)
        return number_order_final
