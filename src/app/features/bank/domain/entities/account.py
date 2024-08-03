from typing import List
from app.features.bank.domain.entities.customer import Customer
from app.features.bank.domain.entities.transaction import Transaction


class Account:
    def __init__(self, id: int, customer: Customer, balance: float, transactions: List[Transaction], password: str):
        self.id = id
        self.customer = customer
        self.balance = balance
        self.password = password
        self.transactions = transactions

    def __repr__(self) -> str:
        return f"Account(id:{self.id} , customer:{self.customer}, balance:{self.balance}, transactions:{self.transactions}, password:{self.password})"
