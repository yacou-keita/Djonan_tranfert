from abc import ABC, abstractmethod
from typing import Union

from app.core.errors.failure import Failure
from app.features.bank.domain.entities.bank import Bank
from app.features.bank.domain.interface_repository.params import CreateAccountParams


class IBankRepository(ABC):

    @abstractmethod
    def create_account(self, params: CreateAccountParams) -> Union[Failure, bool]:
        pass

    @abstractmethod
    def get_account_list(self) -> Union[Failure, list[Bank]]:
        pass
