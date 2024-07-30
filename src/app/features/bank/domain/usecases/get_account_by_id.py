from app.core.errors.failure import Failure
from app.core.interface_usecase.interface_usecase import IUseCase
from app.features.bank.domain.entities.bank import Bank
from app.features.bank.domain.interface_repository.interface_bank_repository import IBankRepository


class GetAccountByID(IUseCase[Bank, str]):
    def __init__(self, repository: IBankRepository) -> None:
        self.__repository = repository

    def execute(self, id: str) -> Failure | Bank:
        return self.__repository.get_account_by_id(id)
