import allure
from base_pages.base_page import BasePage
from locators.password_page_locators import Locators_password


class PasswordPage(BasePage):

    def __init__(self, driver):
        BasePage.__init__(self, driver)

    @allure.step('Находим на странице кнопку Восстановить пароль и переходим по ней.')
    def press_button_recover_password(self, locator, locator_text):
        element = self.find_element_on_page(locator)
        self.scroll(element)
        self.wait_visibility_of_element(locator)
        self.click_on_element(locator)
        self.wait_visibility_of_element(locator_text)

        return self.current_urls()

    @allure.step('Вводим email и нажимаем на кнопку Восстановить.')
    def mail_input_and_click(self, email):
        self.find_element_on_page(Locators_password.input_email).send_keys(email)
        self.click_on_element(Locators_password.recover)
        self.wait_visibility_of_element(Locators_password.save_button)

        return self.current_urls()

    @allure.step('Пароль в фокусе.')
    def password_focused(self):
        self.find_element_on_page(Locators_password.hide_show)
        self.click_on_element(Locators_password.hide_show)
        return self.check_element_is_focused(Locators_password.no_visible_password)
