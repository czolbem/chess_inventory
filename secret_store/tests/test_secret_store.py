import os
from django.test import TestCase

from custom_exceptions.exceptions import DjangoSecretKeyException
from secret_store.secret_store import SecretStore

DJANGO_SECRET_KEY_TEST = 'DJANGO_SECRET_KEY_TEST'


class SecretStoreTest(TestCase):

    def tearDown(self):
        os.environ.pop(DJANGO_SECRET_KEY_TEST, None)

    def test_secret_store_exists(self):
        secret_store = SecretStore(DJANGO_SECRET_KEY_TEST)

        self.assertIsNotNone(secret_store)

    def test_secret_store_sets_environment_variable_name(self):
        secret_store = SecretStore(DJANGO_SECRET_KEY_TEST)

        self.assertEqual(secret_store.environment_variable_name, DJANGO_SECRET_KEY_TEST)

    def test_get_django_secret_key_returns_django_secret_key(self):
        secret_store = SecretStore(DJANGO_SECRET_KEY_TEST)
        django_secret_key_expected = 'ThisIsMySecretKey'
        os.environ[DJANGO_SECRET_KEY_TEST] = django_secret_key_expected

        django_secret_key = secret_store.get_django_secret_key()

        self.assertEqual(django_secret_key, django_secret_key_expected)

    def test_get_django_secret_key_throws_exception_when_environment_variable_not_set(self):
        secret_store = SecretStore(DJANGO_SECRET_KEY_TEST)

        with self.assertRaises(DjangoSecretKeyException):
            secret_store.get_django_secret_key()
