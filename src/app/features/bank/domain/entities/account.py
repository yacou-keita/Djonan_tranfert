from app.features.bank.domain.entities.customer import Customer
from app.features.bank.domain.entities.transaction import Transaction


class Account:
    def __init__(self):
        self.id: int
        self.customer: Customer
        self.balance: float = 0
        self.password: str
        self.transactions: list[Transaction] = []
