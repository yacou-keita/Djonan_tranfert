
from typing import List, Union
from app.core.errors.failure import Failure
from app.core.interface_usecase.interface_usecase import NoParams
from app.features.bank.data.data_source.mongoDB.mongoDB_data_source import MongoDBdataSource
from app.features.bank.data.repository.bank_repository import BankRepository
from app.features.bank.domain.entities.account import Account
from app.features.bank.domain.entities.bank import Bank
from app.features.bank.domain.interface_repository.params import CreateAccountParams, LoginParams, SubscribeParams
from app.features.bank.domain.usecases.create_account import CreateAccount
from app.features.bank.domain.usecases.get_account_by_id import GetAccountByID
from app.features.bank.domain.usecases.get_account_list import GetAccountList
from app.features.bank.domain.usecases.login import Login
from app.features.bank.domain.usecases.subcribe import Subscribe


class BankService:

    def __init__(self) -> None:
        self.mongoDBDataSource = MongoDBdataSource()
        self.repository = BankRepository(self.mongoDBDataSource)

    def create_account(self, params: CreateAccountParams) -> Union[Failure, bool]:
        return CreateAccount(self.repository).execute(params)

    def get_account_list(self, params: NoParams) -> Failure | List[Bank]:
        return GetAccountList(self.repository).execute(params)

    def get_account_by_id(self, id: str) -> Union[Failure , Bank]:
        return GetAccountByID(self.repository).execute(id)

    def subscribe(self, params: SubscribeParams) -> Union[Failure , bool]:
        return Subscribe(self.repository).execute(params)
    
    def login(self, params: LoginParams) -> Union[Failure , Account]:
        return Login(self.repository).execute(params)
