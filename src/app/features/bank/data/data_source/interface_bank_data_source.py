from abc import ABC, abstractmethod
from typing import Union

from app.core.errors.failure import Failure
from app.core.interface_usecase.interface_usecase import NoParams
from app.features.bank.data.models.account_model import AccountModel
from app.features.bank.data.models.bank_model import BankModel
from app.features.bank.domain.interface_repository.params import CreateAccountParams, LoginParams, SubscribeParams


class IBankDataSourceRepository(ABC):

    @abstractmethod
    def create_account(self, params: CreateAccountParams) -> Union[Failure, bool]:
        pass

    @abstractmethod
    def get_account_list(self, params: NoParams) -> BankModel:
        pass

    @abstractmethod
    def get_account_by_id(self, id: str) -> BankModel:
        pass

    @abstractmethod
    def subscribe(self, params: SubscribeParams) -> bool:
        pass

    @abstractmethod
    def login(self, params:LoginParams) -> AccountModel:
        pass
