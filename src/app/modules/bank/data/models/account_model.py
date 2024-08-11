from typing import List
from app.modules.bank.domain.entities.account import Account
from app.modules.bank.domain.entities.customer import Customer
from app.modules.bank.domain.entities.transaction import Transaction


class AccountModel(Account):
    def __init__(self, id: int, customer: Customer, balance: float, transactions: List[Transaction]):
        super().__init__(id=id, customer=customer, balance=balance,
                         transactions=transactions, password="")

    @staticmethod
    def fromJson(account: Account):
        return AccountModel(id=account.id, customer=account.customer, balance=account.balance, transactions=account.transactions)
