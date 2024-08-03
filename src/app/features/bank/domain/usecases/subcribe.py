from typing import Union
from app.core.errors.failure import Failure
from app.core.interface_usecase.interface_usecase import IUseCase
from app.features.bank.domain.entities.bank import Bank
from app.features.bank.domain.interface_repository.interface_bank_repository import IBankRepository
from app.features.bank.domain.interface_repository.params import SubscribeParams


class Subscribe(IUseCase[bool, SubscribeParams]):
    def __init__(self, repository: IBankRepository) -> None:
        self.__repository = repository

    def execute(self, params: SubscribeParams) -> Union[Failure , Bank]:
        return self.__repository.subscribe(params)
