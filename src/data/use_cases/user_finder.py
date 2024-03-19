#pylint: disable=no-name-in-module
#pylint: disable=broad-exception-raised
from typing import Dict, List
from src.data.interfaces.users_repository import UsersRepositoryInterface
from src.domain.use_cases.user_finder import UserFinder as UserFinderInterface
from src.domain.models.users import Users
from src.erros.types import HttpNotFoundError, HttpBadRequestError

class UserFinder(UserFinderInterface):

    def __init__(self, users_repository: UsersRepositoryInterface) -> None:
        self.__users_repository = users_repository

    def find(self, first_name: str) -> Dict:
        self.__validade_name(first_name)
        users = self.__search_firt_name(first_name)
        response = self.__format_response(users)
        
        return response
        
    def __validade_name(self, first_name: str) -> None:
        if not first_name.isalpha():
            raise HttpBadRequestError('Nome invalido para busca')
    
        if len(first_name) > 18:
            raise HttpBadRequestError('Nome muito grande para busca')
        
    def __search_firt_name(self, first_name: str) -> List[Users]:
        users = self.__users_repository.select_user(first_name)
        if users == []:
            raise HttpNotFoundError('Usuario nao encontrado')
        return users
    
    @classmethod
    def __format_response(cls, users: List[Users]) -> Dict:
        attributes = []
        for user in users:
            attributes.append(
                {"fisrt_name": user.first_name, "age": user.age}
            )
            
        response = {
            "type": "Users",
            "count": len(users),
            "attributes": attributes
        }
        
        return response
    