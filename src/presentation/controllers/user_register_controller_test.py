from src.presentation.controllers.user_register_controller import UserRegisterController
from src.data.testes.user_register import UserRegisterSpy
from src.presentation.http_types.http_response import HttpResponse

class HttpRequestMock():
    
    def __init__(self) -> None:
        self.body = {
            "first_name": "meuTeste",
            "last_name": "sobrenome",
            "age": 18
        }

def test_handle():
    http_request_mock = HttpRequestMock()
    use_case = UserRegisterSpy()
    user_register_controller = UserRegisterController(use_case)
    
    response = user_register_controller.handle(http_request_mock)
    response_first_name = response.body["data"]["attributes"][0]["first_name"]
    response_last_name = response.body["data"]["attributes"][0]["last_name"]
    response_age = response.body["data"]["attributes"][0]["age"]
    
    assert isinstance(response, HttpResponse)
    assert response.status_code == 200
    assert response.body["data"] is not None
    assert response_first_name == http_request_mock.body["first_name"]
    assert response_last_name == http_request_mock.body["last_name"]
    assert response_age == http_request_mock.body["age"]
