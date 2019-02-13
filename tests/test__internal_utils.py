# -*- coding: utf-8 -*-
from ambassadress._internal_utils import generate_secret


class TestUtils:

    def test_generate_secret(self):
        ts = '5f585bae-9879-4a29-9a15-36d634b78da1'
        api_key = 'dea2a9818d496d4f85fdbfa14bda1aaa'
        secret = '6d57bc1ff00c42cbc5804988ca30a8c8'  # md5(ts + api_key)
        assert generate_secret(ts, api_key) == secret
