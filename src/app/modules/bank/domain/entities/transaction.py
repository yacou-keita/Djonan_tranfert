from app.modules.bank.domain.entities.customer import Customer


class Transaction:
    def __init__(self):
        self.sender: Customer
        self.receiver: Customer
        self.amount: float
