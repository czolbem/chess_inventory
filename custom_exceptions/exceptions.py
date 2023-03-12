class DjangoSecretKeyException(Exception):
    def __init__(self, *args: object, environment_variable_name) -> None:
        message = f"Could not find environment variable with the key {environment_variable_name}"
        super().__init__(message, *args)


class InvalidPgnException(Exception):
    def __init__(self, *args: object) -> None:
        message = "Supplied PGN is not valid"
        super().__init__(message, *args)
