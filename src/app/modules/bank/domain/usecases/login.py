from typing import Union
from app.core.errors.failure import Failure
from app.core.interface_usecase.interface_usecase import IUseCase
from app.modules.bank.domain.entities.account import Account
from app.modules.bank.domain.interface_repository.interface_bank_repository import IBankRepository
from app.modules.bank.domain.interface_repository.params import LoginParams


class Login(IUseCase[Account, LoginParams]):
    def __init__(self, repository: IBankRepository) -> None:
        self.__repository = repository

    def execute(self, params: LoginParams) -> Union[Failure, Account]:
        return self.__repository.login(params)
