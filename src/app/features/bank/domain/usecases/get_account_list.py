from typing import List, Union
from app.core.errors.failure import Failure
from app.core.interface_usecase.interface_usecase import IUseCase, NoParams
from app.features.bank.domain.entities.bank import Bank
from app.features.bank.domain.interface_repository.interface_bank_repository import IBankRepository


class GetAccountList(IUseCase[List[Bank], NoParams]):
    def __init__(self, repository: IBankRepository) -> None:
        self.__repository = repository

    def execute(self, params: NoParams) -> Union[Failure, list[Bank]]:
        return self.__repository.get_account_list(params)
