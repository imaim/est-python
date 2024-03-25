from .user_register_validator import user_register_validator

class MockRequest:
    def __init__(self) -> None:
        self.json = None

def test_user_register_validator():
    request = MockRequest()
    print()
    request.json = {
        "first_name": "meunome",
        "last_name": "algumacoisa",
        "age": 23
    }
    
    user_register_validator(request)
    