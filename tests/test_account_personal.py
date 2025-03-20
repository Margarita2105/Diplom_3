import allure

from base_pages.personal_account_page import AccountPage
import urls
from locators.personal_account_locators import Locators_account
from tests.conftest import register

class TestAccount:

    @allure.title('Нажимаем кнопку Личный кабинет.')  # декораторы
    @allure.description('На странице ищем кнопку, нажимаем, переходим на страницу личного кабинета, получаем текущий урл, сравниваем текущий урл с урл страницы личного кабинета.')
    def test_press_button_personal_account(self, browser):
        account_button = AccountPage(browser)
        account_button.get_url(urls.main_page)
        url = account_button.press_button_personal_account(Locators_account.personal_account, Locators_account.entrance)

        assert url == urls.login_page

    @allure.title('Переходим в Историю заказов.')  # декораторы
    @allure.description(
        'Авторизуемся, переходим в личный кабинет, переходим в раздел История заказов, проверяем, что раздел История заказов активен.')
    def test_order_history_focused(self, browser, register):

        account_button = AccountPage(browser)
        account_button.get_url(urls.main_page)
        account_button.login(register[0], register[1])
        account_button.go_to_personal_account()
        assert account_button.order_history_focused()

    @allure.title('Выходим из Личного кабинета.')  # декораторы
    @allure.description(
        'Авторизуемся, переходим в личный кабинет, выходим из Личного кабинета, получаем url текущей страницы, сравниваем с url страницы Входа.')
    def test_logout_of_account(self, browser, register):
        account_button = AccountPage(browser)
        account_button.get_url(urls.main_page)
        account_button.login(register[0], register[1])
        account_button.go_to_personal_account()
        url = account_button.logout_of_account()

        assert url == urls.login_page
