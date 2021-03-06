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


class Notification(object):
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
        'id': 'int',
        'template': 'int',
        'receiver': 'int',
        'created_at': 'datetime',
        'values': 'str',
        'seen': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'template': 'template',
        'receiver': 'receiver',
        'created_at': 'created_at',
        'values': 'values',
        'seen': 'seen'
    }

    def __init__(self, id=None, template=None, receiver=None, created_at=None, values=None, seen=None):  # noqa: E501
        """Notification - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._template = None
        self._receiver = None
        self._created_at = None
        self._values = None
        self._seen = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if template is not None:
            self.template = template
        if receiver is not None:
            self.receiver = receiver
        if created_at is not None:
            self.created_at = created_at
        if values is not None:
            self.values = values
        if seen is not None:
            self.seen = seen

    @property
    def id(self):
        """Gets the id of this Notification.  # noqa: E501


        :return: The id of this Notification.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Notification.


        :param id: The id of this Notification.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def template(self):
        """Gets the template of this Notification.  # noqa: E501


        :return: The template of this Notification.  # noqa: E501
        :rtype: int
        """
        return self._template

    @template.setter
    def template(self, template):
        """Sets the template of this Notification.


        :param template: The template of this Notification.  # noqa: E501
        :type: int
        """

        self._template = template

    @property
    def receiver(self):
        """Gets the receiver of this Notification.  # noqa: E501


        :return: The receiver of this Notification.  # noqa: E501
        :rtype: int
        """
        return self._receiver

    @receiver.setter
    def receiver(self, receiver):
        """Sets the receiver of this Notification.


        :param receiver: The receiver of this Notification.  # noqa: E501
        :type: int
        """

        self._receiver = receiver

    @property
    def created_at(self):
        """Gets the created_at of this Notification.  # noqa: E501


        :return: The created_at of this Notification.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Notification.


        :param created_at: The created_at of this Notification.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def values(self):
        """Gets the values of this Notification.  # noqa: E501


        :return: The values of this Notification.  # noqa: E501
        :rtype: str
        """
        return self._values

    @values.setter
    def values(self, values):
        """Sets the values of this Notification.


        :param values: The values of this Notification.  # noqa: E501
        :type: str
        """

        self._values = values

    @property
    def seen(self):
        """Gets the seen of this Notification.  # noqa: E501


        :return: The seen of this Notification.  # noqa: E501
        :rtype: bool
        """
        return self._seen

    @seen.setter
    def seen(self, seen):
        """Sets the seen of this Notification.


        :param seen: The seen of this Notification.  # noqa: E501
        :type: bool
        """

        self._seen = seen

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
        if not isinstance(other, Notification):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
