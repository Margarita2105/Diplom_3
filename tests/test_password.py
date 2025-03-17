import allure
from base_pages.recover_password_page import PasswordPage
import urls
from locators.password_page_locators import Locators_password

class TestPassword:

    @allure.title('Нажимаем кнопку Восстановить пароль.')  # декораторы
    @allure.description('На странице ищем кнопку, нажимаем, переходим на страницу восстановления пароля, получаем текущий урл, сравниваем текущий урл с урл страницы восстановления пароля.')
    def test_press_button_recover_password(self, browser):
        password_button = PasswordPage(browser)
        password_button.get_url(urls.login_page)
        url = password_button.press_button_recover_password(Locators_password.recover_password, Locators_password.forgot_password)

        assert url == urls.forgot_password_page

    @allure.title('Вводим email.')  # декораторы
    @allure.description(
        'На странице ищем поля для ввода почты, вводим почту, нажимаем на кнопку Восстановить, переходим на страницу изменения пароля, получаем текущий урл, сравниваем текущий урл с урл страницы изменения пароля.')
    def test_mail_input_and_click(self, register, browser):
        password_button = PasswordPage(browser)
        password_button.get_url(urls.forgot_password_page)
        url = password_button.mail_input_and_click(register[0])

        assert url == urls.reset_password

    @allure.title('Проверяем видимость пароля.')  # декораторы
    @allure.description(
        'На странице ищем значек для видимости/сокрытия пароля, нажимаем на значек, проверяем видимость пароля.')
    def test_password_focused(self, browser):
        password_button = PasswordPage(browser)
        password_button.get_url(urls.login_page)

        assert password_button.password_focused()
