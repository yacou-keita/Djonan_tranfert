from typing import Union
from app.core.errors.exception import ServerException
from app.core.errors.failure import Failure
from app.core.interface_usecase.interface_usecase import NoParams
from app.features.bank.data.data_source.interface_bank_data_source import IBankDataSourceRepository
from app.features.bank.domain.entities.bank import Bank
from app.features.bank.domain.interface_repository.interface_bank_repository import IBankRepository
from app.features.bank.domain.interface_repository.params import CreateAccountParams


class BankRepository(IBankRepository):

    def __init__(self, bankRepository: IBankDataSourceRepository) -> None:
        self.__bankRepository = bankRepository

    def create_account(self, params: CreateAccountParams) -> Union[Failure, bool]:
        try:
            return self.__bankRepository.create_account(params)
        except ServerException as message:
            return Failure(message)

    def get_account_list(self, params: NoParams) -> Failure | list[Bank]:
        try:
            return self.__bankRepository.get_account_list(params)
        except ServerException as message:
            return Failure(message)
