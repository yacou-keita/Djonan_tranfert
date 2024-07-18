
from typing import Union
from app.core.errors.failure import Failure
from app.features.bank.data.data_source.mongoDB.mongoDB_data_source import MongoDBdataSource
from app.features.bank.data.repository.bank_repository import BankRepository
from app.features.bank.domain.interface_repository.params import CreateAccountParams
from app.features.bank.domain.usecases.create_account import CreateAccount


class BankService:

    def __init__(self) -> None:
        self.mongoDBDataSource = MongoDBdataSource()
        self.repository = BankRepository(self.mongoDBDataSource)

    def create_account(self, params: CreateAccountParams) -> Union[Failure, bool]:
        return CreateAccount(self.repository).execute(params)
