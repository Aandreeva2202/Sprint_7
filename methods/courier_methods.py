import requests
import random
import string
import allure

from urls import COURIER_URL, COURIER_LOGIN_URL

class CourierMethods:

    @staticmethod
    def generate_courier_data():
        # метод генерирует строку, состоящую только из букв нижнего регистра, в качестве параметра передаём длину строки
        def generate_random_string(length):
            letters = string.ascii_lowercase
            random_string = ''.join(random.choice(letters) for i in range(length))
            return random_string
    
        # генерируем логин, пароль и имя курьера
        login = generate_random_string(10)
        password = generate_random_string(10)
        first_name = generate_random_string(10)
    
        # собираем словарь
        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }

        # возвращаем словарь
        return payload 
    
    @staticmethod
    @allure.step("Создать курьера")
    def create_courier(payload):
        return requests.post(COURIER_URL, data=payload)

    @staticmethod
    @allure.step("Логин курьера")
    def login_courier(payload):
        return requests.post(COURIER_LOGIN_URL, data=payload)

    @staticmethod
    @allure.step("Удаление курьера")
    def delete_courier(courier_id):
        return requests.delete(f"{COURIER_URL}/{courier_id}")
