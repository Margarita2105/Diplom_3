import requests
import urls
import allure

class ApiMethods:

    @staticmethod
    @allure.step('Создаем пользователя.')
    def user_new(email_new: str, password_new: str, name_new : str):
        return requests.post(urls.user_api, json={"email": email_new, "password": password_new, "name": name_new })

    @staticmethod
    @allure.step('Авторизуемся под созданным логином пользователя.')
    def login_user(email_user: str, password_user: str):
        return requests.post(urls.login_user_api, json={"email": email_user, "password": password_user})

    @staticmethod
    @allure.step('Удаляем созданного пользователя после прохождения теста.')
    def user_delete(email_delete, password_delete, name_delete):
        token_response = requests.post(urls.login_user_api, json={"email": email_delete, "password": password_delete, "name": name_delete})
        token = token_response.json()['accessToken']
        return requests.delete(urls.data_user_api, headers={'Authorization': token})

    @staticmethod
    @allure.step('Создаем новый заказ авторизованным пользователем.')
    def order_new(email_user, password_user, ingredients):
        response = requests.post(urls.login_user_api, json={"email": email_user, "password": password_user})
        token = response.json()['accessToken']
        id_order = requests.post(urls.orders_api, json={"ingredients": ingredients}, headers={'Authorization': token}).json()['order']['number']
        return id_order

