from src.infra.db.tests.users_repository import UsersRepositorySpy
from .user_finder import UserFinder


def test_find():
    first_name = 'jo4o'
    
    repo = UsersRepositorySpy()
    user_finder = UserFinder(repo)
    
    response = user_finder.find(first_name)
    
    print(response)
    