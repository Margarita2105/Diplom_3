from selenium.webdriver.common.by import By

class Locators_password:

    recover_password = (By.XPATH, ".//a[text()='Восстановить пароль']")
    forgot_password = (By.XPATH, ".//h2[text()='Восстановление пароля']")
    recover = (By.XPATH, ".//button[text()='Восстановить']")
    input_email = (By.XPATH, ".//input[@class='text input__textfield text_type_main-default']")
    save_button = (By.XPATH, ".//button[text()='Сохранить']")
    hide_show = (By.XPATH,".//div[@class='input__icon input__icon-action']")
    no_visible_password = (By.XPATH, ".//input[@name='Пароль']")
