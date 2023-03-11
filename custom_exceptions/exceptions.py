class DjangoSecretKeyException(Exception):
    def __init__(self, *args: object, environment_variable_name) -> None:
        message = f"Could not find environment variable with the key {environment_variable_name}"
        super().__init__(message, *args)

    def __str__(self) -> str:
        return super().__str__()

