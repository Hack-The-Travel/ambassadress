# -*- coding: utf-8 -*-
from hashlib import md5
import random, string
import requests
from ambassadress._internal_utils import generate_signature, now


def random_string(length):
    """Returns random alphanumeric string in lowercase."""
    return ''.join(random.choice(string.lowercase + string.digits) for _ in range(length))


class TestSignatureGenerator:

    def test_generate_signature(self):
        api_key = random_string(40)
        params = {
            'a': random_string(40),
            'b': random_string(40),
            'c': random_string(40),
            'z': 42,
        }
        assert md5(''.join([params['a'], params['b'], params['c'], str(params['z'])]) + api_key).hexdigest()\
            == generate_signature(params, api_key)


class TestClock:

    def test_now(self):
        ts = now()
        ts_redsms = int(requests.get('https://lk.redsms.ru/get/timestamp.php').text)
        epsilon = 60  # 60 seconds
        assert abs(ts_redsms - ts) < epsilon
