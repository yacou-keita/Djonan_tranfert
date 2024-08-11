from abc import ABC, abstractmethod
from typing import List, Union


from app.core.errors.failure import Failure
from app.modules.bank.domain.entities.account import Account
from app.modules.bank.domain.entities.bank import Bank
from app.modules.bank.domain.interface_repository.params import CreateAccountParams, LoginParams, SubscribeParams


class IBankRepository(ABC):

    @abstractmethod
    def create_account(self, params: CreateAccountParams) -> Union[Failure, bool]:
        pass

    @abstractmethod
    def get_account_list(self) -> Union[Failure, List[Bank]]:
        pass

    @abstractmethod
    def get_account_by_id(self, id: str) -> Union[Failure, Bank]:
        pass

    @abstractmethod
    def subscribe(self, params: SubscribeParams) -> Union[Failure, bool]:
        pass

    @abstractmethod
    def login(self, params: LoginParams) -> Union[Failure, Account]:
        pass
