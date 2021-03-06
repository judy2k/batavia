import re

from .. utils import TranspileTestCase, BuiltinFunctionTestCase


class HashTests(TranspileTestCase):
    pass


class BuiltinHashFunctionTests(BuiltinFunctionTestCase, TranspileTestCase):
    functions = ["hash"]

    substitutions = {
        '0': [re.compile(r'^-?\d+$')],
    }

    not_implemented = [
        'test_noargs',
    ]
