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


class BimSnippet(object):
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
        'snippet_type': 'str',
        'is_external': 'bool',
        'reference': 'str',
        'reference_schema': 'str'
    }

    attribute_map = {
        'snippet_type': 'snippet_type',
        'is_external': 'is_external',
        'reference': 'reference',
        'reference_schema': 'reference_schema'
    }

    def __init__(self, snippet_type=None, is_external=None, reference=None, reference_schema=None):  # noqa: E501
        """BimSnippet - a model defined in Swagger"""  # noqa: E501

        self._snippet_type = None
        self._is_external = None
        self._reference = None
        self._reference_schema = None
        self.discriminator = None

        self.snippet_type = snippet_type
        if is_external is not None:
            self.is_external = is_external
        self.reference = reference
        self.reference_schema = reference_schema

    @property
    def snippet_type(self):
        """Gets the snippet_type of this BimSnippet.  # noqa: E501


        :return: The snippet_type of this BimSnippet.  # noqa: E501
        :rtype: str
        """
        return self._snippet_type

    @snippet_type.setter
    def snippet_type(self, snippet_type):
        """Sets the snippet_type of this BimSnippet.


        :param snippet_type: The snippet_type of this BimSnippet.  # noqa: E501
        :type: str
        """
        if snippet_type is None:
            raise ValueError("Invalid value for `snippet_type`, must not be `None`")  # noqa: E501
        if snippet_type is not None and len(snippet_type) > 255:
            raise ValueError("Invalid value for `snippet_type`, length must be less than or equal to `255`")  # noqa: E501

        self._snippet_type = snippet_type

    @property
    def is_external(self):
        """Gets the is_external of this BimSnippet.  # noqa: E501


        :return: The is_external of this BimSnippet.  # noqa: E501
        :rtype: bool
        """
        return self._is_external

    @is_external.setter
    def is_external(self, is_external):
        """Sets the is_external of this BimSnippet.


        :param is_external: The is_external of this BimSnippet.  # noqa: E501
        :type: bool
        """

        self._is_external = is_external

    @property
    def reference(self):
        """Gets the reference of this BimSnippet.  # noqa: E501


        :return: The reference of this BimSnippet.  # noqa: E501
        :rtype: str
        """
        return self._reference

    @reference.setter
    def reference(self, reference):
        """Sets the reference of this BimSnippet.


        :param reference: The reference of this BimSnippet.  # noqa: E501
        :type: str
        """
        if reference is None:
            raise ValueError("Invalid value for `reference`, must not be `None`")  # noqa: E501
        if reference is not None and len(reference) > 255:
            raise ValueError("Invalid value for `reference`, length must be less than or equal to `255`")  # noqa: E501

        self._reference = reference

    @property
    def reference_schema(self):
        """Gets the reference_schema of this BimSnippet.  # noqa: E501


        :return: The reference_schema of this BimSnippet.  # noqa: E501
        :rtype: str
        """
        return self._reference_schema

    @reference_schema.setter
    def reference_schema(self, reference_schema):
        """Sets the reference_schema of this BimSnippet.


        :param reference_schema: The reference_schema of this BimSnippet.  # noqa: E501
        :type: str
        """
        if reference_schema is None:
            raise ValueError("Invalid value for `reference_schema`, must not be `None`")  # noqa: E501
        if reference_schema is not None and len(reference_schema) > 255:
            raise ValueError("Invalid value for `reference_schema`, length must be less than or equal to `255`")  # noqa: E501

        self._reference_schema = reference_schema

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
        if not isinstance(other, BimSnippet):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
