from app.features.bank.domain.entities.account import Account


class Bank:
    def __init__(self, id: int, name: str, password: str, accounts: list[Account] = []) -> None:
        self.id = id
        self.name = name
        self.accounts = accounts
        self.password = password
        self.is_active = True

    def __repr__(self) -> str:
        return f"Bank({self.id} , {self.name} , {self.accounts} , {self.password} , {self.is_active})"
