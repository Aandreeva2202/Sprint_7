import allure

from methods.order_methods import OrderMethods


class TestOrdersList:

    @allure.title("в тело ответа возвращается список заказов")
    def test_get_orders_list_returns_list(self):
        response = OrderMethods.get_orders_list()
        body = response.json()
        assert (response.status_code == 200 and "orders" in body and isinstance(body["orders"], list))
