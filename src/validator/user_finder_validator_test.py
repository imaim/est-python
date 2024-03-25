from .user_finder_validator import user_finder_validator

class MockRequest:
    def __init__(self) -> None:
        self.args = None

def test_user_finder_validator():
    request = MockRequest()
    print()
    request.args = {
        "first_name": "imaim",
    }
    
    user_finder_validator(request)
    