from typing import Union
from app.core.errors.exception import ServerException
from app.core.errors.failure import Failure
from app.features.bank.data.data_source.interface_bank_data_source import IBankDataSourceRepository
from app.features.bank.domain.entities.bank import Bank
from app.features.bank.domain.interface_repository.params import CreateAccountParams


class MongoDBdataSource(IBankDataSourceRepository):

    def __init__(self) -> None:
        self.__list: list[Bank] = []

    def create_account(self, params: CreateAccountParams) -> Union[Failure, bool]:
        try:
            create_index = len(self.__list) + 1
            new_bank = Bank(id=create_index, name=params.name,
                            password=params.password)
            self.__list.append(new_bank)
            return True
        except Exception as error:
            raise ServerException(message=error)
