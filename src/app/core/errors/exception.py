class ServerException(Exception):
    def __init__(self, message="Erreur inattendue") -> None:
        super().__init__(message)
