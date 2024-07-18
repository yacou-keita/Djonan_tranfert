from abc import ABC, abstractmethod
from typing import Union

from app.core.errors.failure import Failure
from app.core.interface_usecase.interface_usecase import NoParams
from app.features.bank.data.models.bank_model import BankModel
from app.features.bank.domain.entities.bank import Bank
from app.features.bank.domain.interface_repository.params import CreateAccountParams


class IBankDataSourceRepository(ABC):

    @abstractmethod
    def create_account(self, params: CreateAccountParams) -> Union[Failure, bool]:
        pass

    @abstractmethod
    def get_account_list(self, params: NoParams) -> BankModel:
        pass
