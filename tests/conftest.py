import pytest
from selenium import webdriver
from data import Ingredient
from api.api_methods import ApiMethods
from helpers import register_new_user_and_return_login_password, register_new_user_and_order


class WebdriverFactory:
    """Фабрика для создания WebDriver на основе переданного имени браузера."""

    @staticmethod
    def getWebdriver(browserName):
        """Метод создает и возвращает WebDriver для указанного браузера."""
        if browserName == "firefox":
            return webdriver.Firefox()
        elif browserName == "chrome":
            return webdriver.Chrome()
        else:
            raise ValueError(f"Unsupported browser: {browserName}")


def pytest_addoption(parser):
    """
    Добавляет аргумент командной строки '--browser' для выбора браузера.
    По умолчанию используется Chrome.
    """
    parser.addoption("--browser", action="store", default="chrome", help="Browser to run tests on")

@pytest.fixture
def browser(request):

    browser_name = request.config.getoption("--browser")  # Получаем значение из --browser
    driver = WebdriverFactory.getWebdriver(browser_name)  # Создаем WebDriver
    yield driver  # Передаем WebDriver в тест
    driver.quit()

@pytest.fixture # фикстура, которая создает драйвер
def driver():
    driver = webdriver.Chrome()
    yield  driver

    driver.quit()

@pytest.fixture
def register():
    register = register_new_user_and_return_login_password()

    yield register
    ApiMethods.user_delete(register[0], register[1], register[2])

@pytest.fixture
def order():
    regist = register_new_user_and_order()
    ApiMethods.order_new(regist[0], regist[1], Ingredient.ingredient)

    yield regist
    ApiMethods.user_delete(regist[0], regist[1], regist[2])

@pytest.fixture
def register_login():
    register_login = register_new_user_and_return_login_password()
    ApiMethods.login_user(register_login[0], register_login[1])

    yield register_login
    ApiMethods.user_delete(register_login[0], register_login[1], register_login[2])
