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


class Classification(object):
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
        'project_id': 'int',
        'name': 'str',
        'notation': 'str',
        'title': 'str'
    }

    attribute_map = {
        'id': 'id',
        'project_id': 'project_id',
        'name': 'name',
        'notation': 'notation',
        'title': 'title'
    }

    def __init__(self, id=None, project_id=None, name=None, notation=None, title=None):  # noqa: E501
        """Classification - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._project_id = None
        self._name = None
        self._notation = None
        self._title = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if project_id is not None:
            self.project_id = project_id
        self.name = name
        self.notation = notation
        if title is not None:
            self.title = title

    @property
    def id(self):
        """Gets the id of this Classification.  # noqa: E501


        :return: The id of this Classification.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Classification.


        :param id: The id of this Classification.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def project_id(self):
        """Gets the project_id of this Classification.  # noqa: E501


        :return: The project_id of this Classification.  # noqa: E501
        :rtype: int
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this Classification.


        :param project_id: The project_id of this Classification.  # noqa: E501
        :type: int
        """

        self._project_id = project_id

    @property
    def name(self):
        """Gets the name of this Classification.  # noqa: E501


        :return: The name of this Classification.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Classification.


        :param name: The name of this Classification.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def notation(self):
        """Gets the notation of this Classification.  # noqa: E501


        :return: The notation of this Classification.  # noqa: E501
        :rtype: str
        """
        return self._notation

    @notation.setter
    def notation(self, notation):
        """Sets the notation of this Classification.


        :param notation: The notation of this Classification.  # noqa: E501
        :type: str
        """
        if notation is None:
            raise ValueError("Invalid value for `notation`, must not be `None`")  # noqa: E501

        self._notation = notation

    @property
    def title(self):
        """Gets the title of this Classification.  # noqa: E501


        :return: The title of this Classification.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this Classification.


        :param title: The title of this Classification.  # noqa: E501
        :type: str
        """

        self._title = title

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
        if not isinstance(other, Classification):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
