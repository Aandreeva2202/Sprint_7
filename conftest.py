import pytest

from methods.courier_methods import CourierMethods


@pytest.fixture
def courier_data():
    return CourierMethods().generate_courier_data()

@pytest.fixture
def created_courier(courier_data):
    response = CourierMethods().create_courier(courier_data)
    login_resp = CourierMethods().login_courier(
        {"login": courier_data["login"], "password": courier_data["password"]}
    )
    courier_id = login_resp.json().get("id")
    yield courier_data, courier_id, response
    if courier_id:
        CourierMethods().delete_courier(courier_id)
