from typing import Union
from app.core.errors.exception import ServerException
from app.core.errors.failure import Failure
from app.features.bank.data.data_source.interface_bank_data_source import IBankDataSourceRepository
from app.features.bank.domain.interface_repository.params import CreateAccountParams


class BankRepository:

    def __init__(self, bankRepository: IBankDataSourceRepository) -> None:
        self.__bankRepository = bankRepository

    def create_account(self, params: CreateAccountParams) -> Union[Failure, bool]:
        try:
            return self.__bankRepository.create_account(params)
        except ServerException as message:
            return Failure(message)
