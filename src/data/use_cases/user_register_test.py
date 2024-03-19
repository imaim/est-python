from src.infra.db.tests.users_repository import UsersRepositorySpy
from .user_register import UserRegister


def test_regiter():
    first_name = "ola"
    last_name = "aqui"
    age = 3
    
    repo = UsersRepositorySpy()
    user_regiter = UserRegister(repo)
    
    response = user_regiter.register(first_name, last_name, age)
    
    assert repo.inser_user_attributes["first_name"] == first_name
    assert repo.inser_user_attributes["last_name"] == last_name
    assert repo.inser_user_attributes["age"] == age
    
    assert response["type"] == "Users"
    assert response["count"] == 1
    assert response["attributes"]
    
def test_register_first_name_erro():
    first_name = "olf3243432325555"
    last_name = "aqui"
    age = 3
    
    repo = UsersRepositorySpy()
    user_regiter = UserRegister(repo)
    
    try:
        user_regiter.register(first_name, last_name, age)
        assert False
    except Exception as exception:
        assert str(exception) == 'Nome invalido para cadastro'
        