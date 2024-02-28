#import pytest
#from src.infra.db.settings.connection import DBConnectionHandler
from .users_repositoy import UsersRepository

def test_inser_user():
    mocked_first_name = 'first'
    mocked_last_name = 'last'
    mocked_age = 34
    
    user_repository = UsersRepository()
    user_repository.inser_user(mocked_first_name, mocked_last_name, mocked_age)
    