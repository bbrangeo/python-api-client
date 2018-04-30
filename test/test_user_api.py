# coding: utf-8

"""
    BIMData API

    BIMData API documentation  # noqa: E501

    OpenAPI spec version: v1
    Contact: contact@bimdata.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import bimdata_api_client
from bimdata_api_client.api.user_api import UserApi  # noqa: E501
from bimdata_api_client.rest import ApiException


class TestUserApi(unittest.TestCase):
    """UserApi unit test stubs"""

    def setUp(self):
        self.api = bimdata_api_client.api.user_api.UserApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_ask_reset_password_token(self):
        """Test case for ask_reset_password_token

        """
        pass

    def test_full_update_notification(self):
        """Test case for full_update_notification

        """
        pass

    def test_get_notification(self):
        """Test case for get_notification

        """
        pass

    def test_get_self_notifications(self):
        """Test case for get_self_notifications

        """
        pass

    def test_get_self_projects(self):
        """Test case for get_self_projects

        """
        pass

    def test_get_self_user(self):
        """Test case for get_self_user

        """
        pass

    def test_reset_password(self):
        """Test case for reset_password

        """
        pass

    def test_sign_up(self):
        """Test case for sign_up

        """
        pass

    def test_sign_up_with_invitation_token(self):
        """Test case for sign_up_with_invitation_token

        """
        pass

    def test_update_notification(self):
        """Test case for update_notification

        """
        pass

    def test_update_self_user(self):
        """Test case for update_self_user

        """
        pass


if __name__ == '__main__':
    unittest.main()
