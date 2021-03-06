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


class Version(object):
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
        'version_id': 'str',
        'detailed_version': 'str'
    }

    attribute_map = {
        'version_id': 'version_id',
        'detailed_version': 'detailed_version'
    }

    def __init__(self, version_id=None, detailed_version=None):  # noqa: E501
        """Version - a model defined in Swagger"""  # noqa: E501

        self._version_id = None
        self._detailed_version = None
        self.discriminator = None

        if version_id is not None:
            self.version_id = version_id
        if detailed_version is not None:
            self.detailed_version = detailed_version

    @property
    def version_id(self):
        """Gets the version_id of this Version.  # noqa: E501


        :return: The version_id of this Version.  # noqa: E501
        :rtype: str
        """
        return self._version_id

    @version_id.setter
    def version_id(self, version_id):
        """Sets the version_id of this Version.


        :param version_id: The version_id of this Version.  # noqa: E501
        :type: str
        """

        self._version_id = version_id

    @property
    def detailed_version(self):
        """Gets the detailed_version of this Version.  # noqa: E501


        :return: The detailed_version of this Version.  # noqa: E501
        :rtype: str
        """
        return self._detailed_version

    @detailed_version.setter
    def detailed_version(self, detailed_version):
        """Sets the detailed_version of this Version.


        :param detailed_version: The detailed_version of this Version.  # noqa: E501
        :type: str
        """

        self._detailed_version = detailed_version

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
        if not isinstance(other, Version):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
