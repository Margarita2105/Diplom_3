import allure
from base_pages.order_feed_page import FeedPage
import urls
from locators.basic_functionality_locators import Locators_functionality
from locators.order_feed_locators import Locators_feed


class TestFeed():


    @allure.title('Получаем карточку заказа.')  # декораторы
    @allure.description(
        'На странице ищем заказ, нажимаем, открывается карточка заказа, в карточке ищем слово Состав.')
    def test_press_button_order(self, browser):
        order = FeedPage(browser)
        order.get_url(urls.order_feed)

        assert order.press_order(Locators_feed.order_in_feed, Locators_functionality.card_order) == "Cостав"


    @allure.title('Проверяем отображение заказов пользователя.')  # декораторы
    @allure.description('Проверяем, что заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов».')
    def test_feed_user(self, browser, order):
        feed = FeedPage(browser)
        feed.get_url(urls.order_feed)
        feed.login(order[0], order[1])

        assert feed.order_in_feed(Locators_feed.personal_account, Locators_feed.order_in_account, Locators_feed.history_orders)


    @allure.title('Проверяем счётчик Выполнено за всё время.')  # декораторы
    @allure.description(
        'Проверяем, что при создании нового заказа счётчик Выполнено за всё время увеличивается.')
    def test_all_time_Completed_counter(self, browser, register):
        counter = FeedPage(browser)
        counter.get_url(urls.order_feed)

        assert counter.counter_orders(Locators_feed.counter, register[0], register[1])

    @allure.title('Проверяем счётчик Выполнено за сегодня.')  # декораторы
    @allure.description(
        'Проверяем, что при создании нового заказа счётчик Выполнено за сегодня увеличивается.')
    def test_Completed_counter_now(self, browser, register):
        counter = FeedPage(browser)
        counter.get_url(urls.order_feed)

        assert counter.counter_orders(Locators_feed.counter_now, register[0], register[1])

    @allure.title('Проверяем номер заказа в разделе В работе.')  # декораторы
    @allure.description(
        'Проверяем, что при создании нового заказа счётчик Выполнено за всё время увеличивается.')
    def test_number_order(self, browser, order):
        order_number = FeedPage(browser)
        order_number.get_url(urls.order_feed)
        number = '0'+str(order[3])

        assert number in order_number.number_order(Locators_feed.at_work, Locators_feed.final)
