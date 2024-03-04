from src.infra.db.repository.users_repository import UsersRepository
from .user_finder import UserFinder


def test_find():
    user_finder = UserFinder()
    