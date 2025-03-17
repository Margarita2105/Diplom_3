import allure
from base_pages.basic_functionality_page import FunctionalityPage
import urls
from locators.basic_functionality_locators import Locators_functionality


class TestFunctionality:

    @allure.title('Нажимаем кнопку Конструктор.')  # декораторы
    @allure.description('На странице ищем кнопку, нажимаем, переходим на главную страницу с Конструктором, получаем текущий урл, сравниваем текущий урл с урл главной страницы.')
    def test_press_button_constructor(self, browser):
        constructor = FunctionalityPage(browser)
        constructor.get_url(urls.login_page)
        url = constructor.press_button(Locators_functionality.constructor)

        assert url == urls.main_page

    @allure.title('Нажимаем кнопку Лента заказов.')  # декораторы
    @allure.description(
        'На странице ищем кнопку, нажимаем, переходим на страницу с заказами, получаем текущий урл, сравниваем текущий урл с урл Ленты заказов.')
    def test_press_button_order_feed(self, browser):
        order_feed = FunctionalityPage(browser)
        order_feed.get_url(urls.main_page)
        url = order_feed.press_button(Locators_functionality.order_feed)

        assert url == urls.order_feed

    @allure.title('Получаем карточку ингредиента.')  # декораторы
    @allure.description(
        'На странице ищем заказ, нажимаем, открывается карточка заказа, в карточке ищем слово Состав.')
    def test_press_button_ingredient(self, browser):
        order = FunctionalityPage(browser)
        order.get_url(urls.main_page)

        assert order.press_button_ingredient(Locators_functionality.sous, Locators_functionality.card_ingredient) == "Детали ингредиента"

    @allure.title('Закрываем карточку заказа.')  # декораторы
    @allure.description(
        'На странице ищем заказ, нажимаем, открывается карточка заказа, нажимаем на крестик, карточка заказа закрывается.')
    def test_press_exit_order(self, browser):
        exit_order = FunctionalityPage(browser)
        exit_order.get_url(urls.main_page)

        assert not exit_order.exit_ingredient(Locators_functionality.sous, Locators_functionality.button_exit, Locators_functionality.card_ingredient, Locators_functionality.constructor)

    @allure.title('Перетаскиваем ингредиент, получаем увеличение каунтера.')  # декораторы
    @allure.description(
        'Запоминаем первоначальное число каунтера ингредиента, перетаскиваем ингредиент, получаем новое значение каунтера, проверяем, что каунтер увеличился.')
    def test_count(self, browser):
        count_ingredient = FunctionalityPage(browser)
        count_ingredient.get_url(urls.main_page)
        count = count_ingredient.count(browser, Locators_functionality.sous, Locators_functionality.basket, Locators_functionality.count)

        assert count

    @allure.step('Проверяем возможность создания заказа авторизованным пользователем, заказ с ингредиентами.')
    def test_order_user(self, register, browser):
        order_user = FunctionalityPage(browser)
        order_user.get_url(urls.main_page)
        active_order = order_user.order_user(browser, Locators_functionality.sous, Locators_functionality.basket,
                                             Locators_functionality.place_order1, Locators_functionality.active_order,
                                             register[0], register[1])

        assert active_order == 'Ваш заказ начали готовить'
