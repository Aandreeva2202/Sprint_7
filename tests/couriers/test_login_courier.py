import pytest
import allure
from methods.courier_methods import CourierMethods


class TestLoginCourier:

    @allure.title('Тест на проверку успешной авторизации курьера')
    @allure. description('для авторизации нужно передать все обязательные поля, успешный запрос возвращает id')
    def test_login_courier_success(self, created_courier):
        courier_data, _ = created_courier
        response = CourierMethods.login_courier(
            {"login": courier_data["login"], "password": courier_data["password"]}
        )
        body = response.json()
        assert (response.status_code == 200 and "id" in body and isinstance(body["id"], int))

    @allure.title('если логина нет, запрос возвращает ошибку')
    def test_login_without_login_returns_error(self, created_courier):
        courier_data, _ = created_courier
        payload = {
            "login": courier_data["login"],
            "password": courier_data["password"],
        }
        del payload["login"]
        response = CourierMethods.login_courier(payload)
        assert response.status_code == 400

    @allure.title('если пароля нет, запрос возвращает ошибку')
    def test_login_without_password_returns_error(self, created_courier):
            courier_data, _ = created_courier
            payload = {
                "login": courier_data["login"],
                "password": courier_data["password"],
            }
            del payload["password"]
            response = CourierMethods.login_courier(payload)
            assert response.status_code == 504

    @allure.title('система вернёт ошибку, если неправильно указать логин или пароль')
    @pytest.mark.parametrize(
        "wrong_field,new_value",
        [
            ("login", "wrong_login_999"),
            ("password", "wrong_password_999"),
        ],
    )
    def test_login_with_wrong_credentials_returns_error(
        self, created_courier, wrong_field, new_value
    ):
        courier_data, _ = created_courier
        payload = {
            "login": courier_data["login"],
            "password": courier_data["password"],
        }
        payload[wrong_field] = new_value
        response  = CourierMethods.login_courier(payload)
        assert response.status_code == 404

    @allure.title('если авторизоваться под несуществующим пользователем, запрос возвращает ошибку')
    def test_login_nonexistent_user_returns_error(self):
        response = CourierMethods.login_courier(
            {"login": "no_such_user_12345", "password": "no_such_pw_12345"}
        )
        assert response.status_code == 404
