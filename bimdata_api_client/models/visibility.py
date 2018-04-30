# coding: utf-8

"""
    BIMData API

    BIMData API documentation  # noqa: E501

    OpenAPI spec version: v1
    Contact: contact@bimdata.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from bimdata_api_client.models.component import Component  # noqa: F401,E501
from bimdata_api_client.models.view_setup_hints import ViewSetupHints  # noqa: F401,E501


class Visibility(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'default_visibility': 'bool',
        'exceptions': 'list[Component]',
        'view_setup_hints': 'ViewSetupHints'
    }

    attribute_map = {
        'default_visibility': 'default_visibility',
        'exceptions': 'exceptions',
        'view_setup_hints': 'view_setup_hints'
    }

    def __init__(self, default_visibility=None, exceptions=None, view_setup_hints=None):  # noqa: E501
        """Visibility - a model defined in Swagger"""  # noqa: E501

        self._default_visibility = None
        self._exceptions = None
        self._view_setup_hints = None
        self.discriminator = None

        if default_visibility is not None:
            self.default_visibility = default_visibility
        self.exceptions = exceptions
        self.view_setup_hints = view_setup_hints

    @property
    def default_visibility(self):
        """Gets the default_visibility of this Visibility.  # noqa: E501


        :return: The default_visibility of this Visibility.  # noqa: E501
        :rtype: bool
        """
        return self._default_visibility

    @default_visibility.setter
    def default_visibility(self, default_visibility):
        """Sets the default_visibility of this Visibility.


        :param default_visibility: The default_visibility of this Visibility.  # noqa: E501
        :type: bool
        """

        self._default_visibility = default_visibility

    @property
    def exceptions(self):
        """Gets the exceptions of this Visibility.  # noqa: E501


        :return: The exceptions of this Visibility.  # noqa: E501
        :rtype: list[Component]
        """
        return self._exceptions

    @exceptions.setter
    def exceptions(self, exceptions):
        """Sets the exceptions of this Visibility.


        :param exceptions: The exceptions of this Visibility.  # noqa: E501
        :type: list[Component]
        """
        if exceptions is None:
            raise ValueError("Invalid value for `exceptions`, must not be `None`")  # noqa: E501

        self._exceptions = exceptions

    @property
    def view_setup_hints(self):
        """Gets the view_setup_hints of this Visibility.  # noqa: E501


        :return: The view_setup_hints of this Visibility.  # noqa: E501
        :rtype: ViewSetupHints
        """
        return self._view_setup_hints

    @view_setup_hints.setter
    def view_setup_hints(self, view_setup_hints):
        """Sets the view_setup_hints of this Visibility.


        :param view_setup_hints: The view_setup_hints of this Visibility.  # noqa: E501
        :type: ViewSetupHints
        """
        if view_setup_hints is None:
            raise ValueError("Invalid value for `view_setup_hints`, must not be `None`")  # noqa: E501

        self._view_setup_hints = view_setup_hints

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Visibility):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
