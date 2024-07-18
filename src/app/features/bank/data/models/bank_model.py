from app.features.bank.domain.entities.account import Account
from app.features.bank.domain.entities.bank import Bank


class BankModel(Bank):

    def __init__(self, id: int, name: str, password: str, accounts: list[Account] = []) -> None:
        super().__init__(id=id, name=name, accounts=accounts, password=password)

    @staticmethod
    def from_json(bank_list: list[Bank]):
        return [BankModel(id=bank.id, name=bank.name, password="", accounts=bank.accounts) for bank in bank_list]
