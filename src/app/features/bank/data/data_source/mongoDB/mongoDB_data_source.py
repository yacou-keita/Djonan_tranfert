from typing import Union
from app.core.errors.exception import ServerException
from app.core.errors.failure import Failure
from app.core.interface_usecase.interface_usecase import NoParams
from app.features.bank.data.data_source.interface_bank_data_source import IBankDataSourceRepository
from app.features.bank.data.models.bank_model import BankModel
from app.features.bank.domain.entities.account import Account
from app.features.bank.domain.entities.bank import Bank
from app.features.bank.domain.interface_repository.params import CreateAccountParams, SubscribeParams


class MongoDBdataSource(IBankDataSourceRepository):

    def __init__(self) -> None:
        self.__list: list[Bank] = []

    def create_account(self, params: CreateAccountParams) -> Union[Failure, bool]:
        try:
            # create_index = len(self.__list) + 1
            create_index = max(
                (account.id for account in self.__list), default=0) + 1
            new_bank = Bank(id=create_index, name=params.name,
                            password=params.password)
            self.__list.append(new_bank)
            return True
        except Exception as error:
            raise ServerException(message=error)

    def get_account_list(self, params: NoParams) -> BankModel:
        try:
            return BankModel.from_json(self.__list)
        except Exception as error:
            raise ServerException(message=error)

    def get_account_by_id(self, id: str) -> BankModel:
        try:
            get_account = next(
                (account for account in self.__list if account.id == id), None)

            if get_account is None:
                raise ServerException(
                    message=f"No account found with id: {id}")

            return BankModel.from_json([get_account])[0]
        except Exception as error:
            raise ServerException(message=error)

    def subscribe(self, params: SubscribeParams) -> bool:
        try:
            get_bank = next(
                (bank for bank in self.__list if bank.id == params.bank_id), None)

            if get_bank is None:
                raise ServerException(
                    message=f"No bank found with id: {params.bank_id}")

            create_index = max(
                [account.id for account in get_bank.accounts], default=0) + 1

            new_subscriber = Account()
            new_subscriber.id = create_index
            new_subscriber.customer = params.customer
            new_subscriber.password = params.password

            get_bank.accounts = [new_subscriber] + get_bank.accounts

            return True
        except Exception as error:
            raise ServerException(message=error)

