from abc import ABC, abstractmethod
from typing import Union

from app.core.errors.failure import Failure
from app.features.bank.domain.entities.bank import Bank
from app.features.bank.domain.interface_repository.params import CreateAccountParams, SubscribeParams


class IBankRepository(ABC):

    @abstractmethod
    def create_account(self, params: CreateAccountParams) -> Union[Failure, bool]:
        pass

    @abstractmethod
    def get_account_list(self) -> Union[Failure, list[Bank]]:
        pass

    @abstractmethod
    def get_account_by_id(self, id: str) -> Failure | Bank:
        pass

    @abstractmethod
    def subscribe(self, params: SubscribeParams) -> Failure | bool:
        pass
