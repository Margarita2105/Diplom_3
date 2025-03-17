import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC

from tests.conftest import driver, browser


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Задаем явное ожидание до видимости элемента на странице.')
    def wait_visibility_of_element(self, locator):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(locator))

    @allure.step('Находим элемент на странице.')
    def find_element_on_page(self, locator):
        return self.driver.find_element(*locator)

    @allure.step('Находим элемент на странице и получаем его текст.')
    def text_of_element(self, locator):
        text = self.driver.find_element(*locator).text

        return text

    @allure.step('Находим элемент на странице и нажимаем на него.')
    def click_on_element_chrome(self, locator):
        self.find_element_on_page(locator).click()

    @allure.step('Находим элемент на странице и нажимаем на него.')
    def click_on_element(self, locator):
        if browser == 'chrome':
            self.find_element_on_page(locator).click()
        element = self.find_element_on_page(locator)
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step('Находим элемент на странице и нажимаем на него.')
    def click_on_element_firefox(self, locator):
        element = self.find_element_on_page(locator)
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step('Скролим до элемента.')
    def scroll(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('Вводим урл страницы на которую нужно перейти.')
    def get_url(self, url):
        self.driver.get(url)

    @allure.step('Переходим на открывшуюся страницу в новой вкладке.')
    def get_tab_and_switch(self):
        tabs = self.driver.window_handles
        self.driver.switch_to.window(tabs[1])
        return tabs

    @allure.step('Получаем урл текущей страницы.')
    def current_urls(self):
        return self.driver.current_url

    @allure.step('Проверяем, что элемент в фокусе.')
    def check_element_is_focused(self, locator):
        element = self.driver.find_element(*locator)
        is_focused = self.driver.execute_script("return document.activeElement === arguments[0];", element)
        return is_focused

    @allure.step('Перетаскиваем элемент.')
    def drag_and_drop(self, dry, element_from, element_to):
        if browser == 'chrome':
            from_element = self.driver.find_element(*element_from)
            to_element = self.driver.find_element(*element_to)
            action = ActionChains(dry)
            action.drag_and_drop(from_element, to_element).perform()
            return action.drag_and_drop(from_element, to_element).perform()
        source_element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(element_from))
        target_element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(element_to))
        # JavaScript для перетаскивания
        self.driver.execute_script(
            "function createEvent(typeOfEvent) { " +
            "var event = document.createEvent('CustomEvent'); " +
            "event.initCustomEvent(typeOfEvent, true, true, null); " +
            "event.dataTransfer = { " +
            "data: {}, " +
            "setData: function(key, value) { this.data[key] = value; }, " +
            "getData: function(key) { return this.data[key]; } " +
            "}; " +
            "return event; " +
            "} " +
            "function dispatchEvent(element, typeOfEvent, event) { " +
            "if (element.dispatchEvent) { " +
            "element.dispatchEvent(event); " +
            "} else if (element.fireEvent) { " +
            "element.fireEvent('on' + typeOfEvent, event); " +
            "} " +
            "} " +
            "function simulateHTML5DragAndDrop(element, destination) { " +
            "var dragStartEvent = createEvent('dragstart'); " +
            "dispatchEvent(element, 'dragstart', dragStartEvent); " +
            "var dropEvent = createEvent('drop'); " +
            "dispatchEvent(destination, 'drop', dropEvent); " +
            "var dragEndEvent = createEvent('dragend'); " +
            "dispatchEvent(element, 'dragend', dragEndEvent); " +
            "} " +
            "simulateHTML5DragAndDrop(arguments[0], arguments[1]);",
            source_element,
            target_element
        )

    def visibility_of_element(self):
        WebDriverWait(self.driver, 20)


