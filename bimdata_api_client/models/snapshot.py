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


class Snapshot(object):
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
        'snapshot_type': 'str',
        'snapshot_data': 'str'
    }

    attribute_map = {
        'snapshot_type': 'snapshot_type',
        'snapshot_data': 'snapshot_data'
    }

    def __init__(self, snapshot_type=None, snapshot_data=None):  # noqa: E501
        """Snapshot - a model defined in Swagger"""  # noqa: E501

        self._snapshot_type = None
        self._snapshot_data = None
        self.discriminator = None

        self.snapshot_type = snapshot_type
        self.snapshot_data = snapshot_data

    @property
    def snapshot_type(self):
        """Gets the snapshot_type of this Snapshot.  # noqa: E501


        :return: The snapshot_type of this Snapshot.  # noqa: E501
        :rtype: str
        """
        return self._snapshot_type

    @snapshot_type.setter
    def snapshot_type(self, snapshot_type):
        """Sets the snapshot_type of this Snapshot.


        :param snapshot_type: The snapshot_type of this Snapshot.  # noqa: E501
        :type: str
        """
        if snapshot_type is None:
            raise ValueError("Invalid value for `snapshot_type`, must not be `None`")  # noqa: E501
        if snapshot_type is not None and len(snapshot_type) > 255:
            raise ValueError("Invalid value for `snapshot_type`, length must be less than or equal to `255`")  # noqa: E501

        self._snapshot_type = snapshot_type

    @property
    def snapshot_data(self):
        """Gets the snapshot_data of this Snapshot.  # noqa: E501


        :return: The snapshot_data of this Snapshot.  # noqa: E501
        :rtype: str
        """
        return self._snapshot_data

    @snapshot_data.setter
    def snapshot_data(self, snapshot_data):
        """Sets the snapshot_data of this Snapshot.


        :param snapshot_data: The snapshot_data of this Snapshot.  # noqa: E501
        :type: str
        """
        if snapshot_data is None:
            raise ValueError("Invalid value for `snapshot_data`, must not be `None`")  # noqa: E501

        self._snapshot_data = snapshot_data

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
        if not isinstance(other, Snapshot):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other