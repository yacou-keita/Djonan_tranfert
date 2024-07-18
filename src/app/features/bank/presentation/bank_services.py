
from typing import Union
from app.core.errors.failure import Failure
from app.core.interface_usecase.interface_usecase import NoParams
from app.features.bank.data.data_source.mongoDB.mongoDB_data_source import MongoDBdataSource
from app.features.bank.data.repository.bank_repository import BankRepository
from app.features.bank.domain.entities.bank import Bank
from app.features.bank.domain.interface_repository.params import CreateAccountParams
from app.features.bank.domain.usecases.create_account import CreateAccount
from app.features.bank.domain.usecases.get_account_list import GetAccountList


class BankService:

    def __init__(self) -> None:
        self.mongoDBDataSource = MongoDBdataSource()
        self.repository = BankRepository(self.mongoDBDataSource)

    def create_account(self, params: CreateAccountParams) -> Union[Failure, bool]:
        return CreateAccount(self.repository).execute(params)

    def get_account_list(self, params: NoParams) -> Failure | list[Bank]:
        return GetAccountList(self.repository).execute(params)
