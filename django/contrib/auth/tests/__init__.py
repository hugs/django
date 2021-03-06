from django.contrib.auth.tests.basic import BASIC_TESTS
from django.contrib.auth.tests.views import PasswordResetTest
from django.contrib.auth.tests.forms import FORM_TESTS
from django.contrib.auth.tests.tokens import TOKEN_GENERATOR_TESTS

__test__ = {
    'BASIC_TESTS': BASIC_TESTS,
    'PASSWORDRESET_TESTS': PasswordResetTest,
    'FORM_TESTS': FORM_TESTS,
    'TOKEN_GENERATOR_TESTS': TOKEN_GENERATOR_TESTS
}
