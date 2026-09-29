import requests
import allure

from urls import ORDER_URL
from data import ORDER_DATA_1


class OrderMethods:

    def generate_order_data(color=None):
        if color is not None:
            ORDER_DATA_1["color"] = color
        return ORDER_DATA_1

    @allure.step("Создание заказа")
    def create_order(payload):
        return requests.post(ORDER_URL, json=payload)

    @allure.step("Получение списка заказов")
    def get_orders_list(params=None):
        return requests.get(ORDER_URL, params=params)
    