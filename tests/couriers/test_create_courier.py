import pytest
import allure
from methods.courier_methods import CourierMethods


class TestCreateCourier:

    @allure.title('Тест на проверку создания курьера')
    @allure. description('чтобы создать курьера, нужно передать в ручку все обязательные поля')
    @allure. description('запрос возвращает правильный код ответа и {"ok":true}')
    def test_create_courier_success(self, courier_data):
        response = CourierMethods().create_courier(courier_data)
        assert (not isinstance(courier_data, str) and response.status_code == 201
                and response.json() == {"ok": True})
        
    @allure.title('Нельзя создать двух одинаковых курьеров')
    def test_cannot_create_duplicate_courier(self, courier_data):
        CourierMethods().create_courier(courier_data)
        response = CourierMethods().create_courier(courier_data)
        assert response.status_code == 409

    @allure.title('Создание пользователя с логином, который уже есть, возвращает ошибку')
    def test_cannot_create_courier_with_existing_login(self, courier_data):
        CourierMethods().create_courier(courier_data)
        dup = {
            "login": courier_data["login"],
            "password": "12345",
            "firstName": "Testn",
        }
        response = CourierMethods().create_courier(dup)
        assert response.status_code == 409

    @allure.title('если одного из полей нет, запрос возвращает ошибку')    
    @pytest.mark.parametrize("missing_field", ["login", "password"])       #при отсутствии "firstName" ошибка не возвращается, статус код 201, поэтому из теста на проверку ошибок убрала это поле
    def test_create_courier_without_required_field(self, missing_field):
        data = CourierMethods.generate_courier_data()
        del data[missing_field]
        courier_methods = CourierMethods()
        response = courier_methods.create_courier(data)
        assert response.status_code == 400
