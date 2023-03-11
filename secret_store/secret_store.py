import os

from custom_exceptions.exceptions import DjangoSecretKeyException


class SecretStore:
    """
    Totally legit secret store. Replace.
    """

    def __init__(self, environment_variable_name) -> None:
        self.environment_variable_name = environment_variable_name

    def get_django_secret_key(self) -> str:
        try:
            django_secret_key = os.environ[self.environment_variable_name]
        except KeyError:
            raise DjangoSecretKeyException(environment_variable_name=self.environment_variable_name)
        return django_secret_key
