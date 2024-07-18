from app.features.bank.domain.entities.bank import Bank


class BankModel(Bank):

    def __init__(self) -> None:
        super().__init__()

    @staticmethod
    def from_json():
        pass
