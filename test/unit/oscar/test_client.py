#! /usr/bin/python

# Copyright (C) GRyCAP - I3M - UPV
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import unittest
import sys
import os
from mock import MagicMock
from mock import patch

sys.path.append("..")
sys.path.append(".")
sys.path.append("../..")

from scar.providers.oscar.client import OSCARClient


class TestOSCARClient(unittest.TestCase):

    def __init__(self, *args):
        unittest.TestCase.__init__(self, *args)

    @patch('requests.post')
    def test_create_serviced(self, post):
        response = MagicMock("status_code")
        response.status_code = 201
        post.return_value = response
        oscar = OSCARClient({"endpoint": "url", "auth_user": "user", "auth_password": "pass", "ssl_verify": False}, "cid")
        oscar.create_service(key="value")
        self.assertEqual(post.call_args_list[0][0][0], "url/system/services")
        self.assertEqual(post.call_args_list[0][1], {'auth': ('user', 'pass'), 'verify': False, 'json': {'key': 'value'}})
