from typing import List, Union
from app.core.errors.exception import ServerException
from app.core.errors.failure import Failure
from app.core.interface_usecase.interface_usecase import NoParams
from app.modules.bank.data.data_source.interface_bank_data_source import IBankDataSourceRepository
from app.modules.bank.domain.entities.account import Account
from app.modules.bank.domain.entities.bank import Bank
from app.modules.bank.domain.interface_repository.interface_bank_repository import IBankRepository
from app.modules.bank.domain.interface_repository.params import CreateAccountParams, LoginParams, SubscribeParams


class BankRepository(IBankRepository):

    def __init__(self, bankRepository: IBankDataSourceRepository) -> None:
        self.__bankRepository = bankRepository

    def create_account(self, params: CreateAccountParams) -> Union[Failure, bool]:
        try:
            return self.__bankRepository.create_account(params)
        except ServerException as message:
            return Failure(message)

    def get_account_list(self, params: NoParams) -> Union[Failure, List[Bank]]:
        try:
            return self.__bankRepository.get_account_list(params)
        except ServerException as message:
            return Failure(message)

    def get_account_by_id(self, id: str) -> Union[Failure | Bank]:
        try:
            return self.__bankRepository.get_account_by_id(id)
        except ServerException as message:
            return Failure(message)

    def subscribe(self, params: SubscribeParams) -> Union[Failure, bool]:
        try:
            return self.__bankRepository.subscribe(params)
        except ServerException as message:
            return Failure(message)

    def login(self, params: LoginParams) -> Union[Failure, Account]:
        try:
            return self.__bankRepository.login(params)
        except ServerException as message:
            return Failure(message)
