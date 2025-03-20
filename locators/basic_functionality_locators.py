from selenium.webdriver.common.by import By

class Locators_functionality:

    constructor = (By.XPATH, ".//p[text()='Конструктор']")
    main_page = (By.XPATH, ".//h1[text()='Соберите бургер']")
    order_feed = (By.XPATH, ".//p[text()='Лента Заказов']")
    order_feed_activ = (By.XPATH, ".//h1[text()='Лента Заказов']")
    order = (By.XPATH, ".//li[@class='OrderHistory_listItem__2x95r mb-6']")
    card_order = (By.XPATH, ".//p[text()='Cостав']")
    button_exit = (By.XPATH, "//button[@class= 'Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK']")
    card_ingredient = (By.XPATH, ".//h2[text()='Детали ингредиента']")
    sous = (By.XPATH, ".//img[@alt='Соус Spicy-X']")
    basket = (By.XPATH, ".//div[@class='constructor-element constructor-element_pos_top']")
    count = (By.XPATH, ".//p[@class='text text_type_digits-medium mr-3']")
    active_order = (By.XPATH, ".//p[text()='Ваш заказ начали готовить']")
    place_order = (By.XPATH, ".//button[text()='Оформить заказ']")
    place_order1 = (By.XPATH, ".//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg']")
