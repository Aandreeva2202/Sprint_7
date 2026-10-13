import requests
import pytest
import allure

from methods.order_methods import OrderMethods


class TestCreateOrder:

    @allure.title("Успешное создание заказа")
    @allure. description('создание заказа с разными цветами; ответ содержит track')
    @pytest.mark.parametrize(
        "color,description",
        [
            (["BLACK"], "только BLACK"),
            (["GREY"], "только GREY"),
            (["BLACK", "GREY"], "оба цвета"),
            (None, "цвет не указан"),
        ],
        ids=["black", "grey", "both", "no_color"],
    )
    def test_create_order_with_color_variants(self, color, description):
        order_data = OrderMethods.generate_order_data(color=color)
        response = OrderMethods.create_order(order_data)
        body = response.json()
        assert (response.status_code == 201 and "track" in body and isinstance(body["track"], int))
