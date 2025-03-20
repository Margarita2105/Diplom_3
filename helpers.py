import requests
import random
import string
import allure
import urls
from api.api_methods import ApiMethods
from data import Ingredient

# метод регистрации нового пользователя возвращает список из логина и пароля
# если регистрация не удалась, возвращает пустой список
@allure.step('Регистрируем уникального пользователя.')
def register_new_user_and_return_login_password():
    # метод генерирует строку, состоящую только из букв нижнего регистра, в качестве параметра передаём длину строки
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    # создаём список, чтобы метод мог его вернуть
    login_pass = []

    # генерируем логин, пароль и имя пользователя
    email = generate_random_string(10)+'@mail.com'
    password = generate_random_string(10)
    name = generate_random_string(10)

    # собираем тело запроса
    payload = {
        "email": email,
        "password": password,
        "name": name
    }

    # отправляем запрос на регистрацию пользователя и сохраняем ответ в переменную response
    response = requests.post(urls.user_api, data=payload)

    # если регистрация прошла успешно (код ответа 200), добавляем в список логин и пароль пользователя
    if response.status_code == 200:
        login_pass = [email, password, name]

    # возвращаем список
    return login_pass

@allure.step('Генерируем строку, состоящую только из букв нижнего регистра.')
def generate_random_string(length):
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(length))
    return random_string

data = generate_random_string(10)
data_email = generate_random_string(10)+'@mail.com'
registration = register_new_user_and_return_login_password

@allure.step('Регистрируем уникального пользователя.')
def register_new_user_and_order():
    # метод генерирует строку, состоящую только из букв нижнего регистра, в качестве параметра передаём длину строки
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    # создаём список, чтобы метод мог его вернуть
    login_pass = []

    # генерируем логин, пароль и имя пользователя
    email = generate_random_string(10)+'@mail.com'
    password = generate_random_string(10)
    name = generate_random_string(10)

    # собираем тело запроса
    payload = {
        "email": email,
        "password": password,
        "name": name
    }

    # отправляем запрос на регистрацию пользователя и сохраняем ответ в переменную response
    response = requests.post(urls.user_api, data=payload)

    # если регистрация прошла успешно (код ответа 200), добавляем в список логин и пароль пользователя
    if response.status_code == 200:
        login_pass = [email, password, name]

    token = response.json()['accessToken']
    id_order = ApiMethods.order_new(email, password, Ingredient.ingredient)
    login_pass = [email, password, name, id_order]

    # возвращаем список
    return login_pass
