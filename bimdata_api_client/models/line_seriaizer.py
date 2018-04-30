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

from bimdata_api_client.models.point import Point  # noqa: F401,E501


class LineSeriaizer(object):
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
        'end_point': 'Point',
        'start_point': 'Point'
    }

    attribute_map = {
        'end_point': 'end_point',
        'start_point': 'start_point'
    }

    def __init__(self, end_point=None, start_point=None):  # noqa: E501
        """LineSeriaizer - a model defined in Swagger"""  # noqa: E501

        self._end_point = None
        self._start_point = None
        self.discriminator = None

        self.end_point = end_point
        self.start_point = start_point

    @property
    def end_point(self):
        """Gets the end_point of this LineSeriaizer.  # noqa: E501


        :return: The end_point of this LineSeriaizer.  # noqa: E501
        :rtype: Point
        """
        return self._end_point

    @end_point.setter
    def end_point(self, end_point):
        """Sets the end_point of this LineSeriaizer.


        :param end_point: The end_point of this LineSeriaizer.  # noqa: E501
        :type: Point
        """
        if end_point is None:
            raise ValueError("Invalid value for `end_point`, must not be `None`")  # noqa: E501

        self._end_point = end_point

    @property
    def start_point(self):
        """Gets the start_point of this LineSeriaizer.  # noqa: E501


        :return: The start_point of this LineSeriaizer.  # noqa: E501
        :rtype: Point
        """
        return self._start_point

    @start_point.setter
    def start_point(self, start_point):
        """Sets the start_point of this LineSeriaizer.


        :param start_point: The start_point of this LineSeriaizer.  # noqa: E501
        :type: Point
        """
        if start_point is None:
            raise ValueError("Invalid value for `start_point`, must not be `None`")  # noqa: E501

        self._start_point = start_point

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
        if not isinstance(other, LineSeriaizer):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
