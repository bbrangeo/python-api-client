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


class SnippetType(object):
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
        'snippet_type': 'str'
    }

    attribute_map = {
        'snippet_type': 'snippet_type'
    }

    def __init__(self, snippet_type=None):  # noqa: E501
        """SnippetType - a model defined in Swagger"""  # noqa: E501

        self._snippet_type = None
        self.discriminator = None

        if snippet_type is not None:
            self.snippet_type = snippet_type

    @property
    def snippet_type(self):
        """Gets the snippet_type of this SnippetType.  # noqa: E501


        :return: The snippet_type of this SnippetType.  # noqa: E501
        :rtype: str
        """
        return self._snippet_type

    @snippet_type.setter
    def snippet_type(self, snippet_type):
        """Sets the snippet_type of this SnippetType.


        :param snippet_type: The snippet_type of this SnippetType.  # noqa: E501
        :type: str
        """
        if snippet_type is not None and len(snippet_type) > 255:
            raise ValueError("Invalid value for `snippet_type`, length must be less than or equal to `255`")  # noqa: E501

        self._snippet_type = snippet_type

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
        if not isinstance(other, SnippetType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
