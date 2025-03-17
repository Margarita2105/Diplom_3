from selenium.webdriver.common.by import By

class Locators_account:

    personal_account = (By.XPATH, ".//p[text()='Личный Кабинет']")
    entrance = (By.XPATH, ".//h2[text()='Вход']")
    order_history = (By.XPATH, ".//a[text()='История заказов']")
    field_password = (By.XPATH, ".//input[@name='Пароль']")
    field_email = (By.XPATH, ".//input[@name='name']")
    button_entrance = (By.XPATH, ".//button[text()='Войти']")
    button_exit = (By.XPATH, ".//button[text()='Выход']")
