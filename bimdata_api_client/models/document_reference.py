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


class DocumentReference(object):
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
        'guid': 'str',
        'referenced_document': 'str',
        'description': 'str'
    }

    attribute_map = {
        'guid': 'guid',
        'referenced_document': 'referenced_document',
        'description': 'description'
    }

    def __init__(self, guid=None, referenced_document=None, description=None):  # noqa: E501
        """DocumentReference - a model defined in Swagger"""  # noqa: E501

        self._guid = None
        self._referenced_document = None
        self._description = None
        self.discriminator = None

        if guid is not None:
            self.guid = guid
        if referenced_document is not None:
            self.referenced_document = referenced_document
        if description is not None:
            self.description = description

    @property
    def guid(self):
        """Gets the guid of this DocumentReference.  # noqa: E501


        :return: The guid of this DocumentReference.  # noqa: E501
        :rtype: str
        """
        return self._guid

    @guid.setter
    def guid(self, guid):
        """Sets the guid of this DocumentReference.


        :param guid: The guid of this DocumentReference.  # noqa: E501
        :type: str
        """

        self._guid = guid

    @property
    def referenced_document(self):
        """Gets the referenced_document of this DocumentReference.  # noqa: E501


        :return: The referenced_document of this DocumentReference.  # noqa: E501
        :rtype: str
        """
        return self._referenced_document

    @referenced_document.setter
    def referenced_document(self, referenced_document):
        """Sets the referenced_document of this DocumentReference.


        :param referenced_document: The referenced_document of this DocumentReference.  # noqa: E501
        :type: str
        """
        if referenced_document is not None and len(referenced_document) > 255:
            raise ValueError("Invalid value for `referenced_document`, length must be less than or equal to `255`")  # noqa: E501

        self._referenced_document = referenced_document

    @property
    def description(self):
        """Gets the description of this DocumentReference.  # noqa: E501


        :return: The description of this DocumentReference.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this DocumentReference.


        :param description: The description of this DocumentReference.  # noqa: E501
        :type: str
        """
        if description is not None and len(description) > 255:
            raise ValueError("Invalid value for `description`, length must be less than or equal to `255`")  # noqa: E501

        self._description = description

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
        if not isinstance(other, DocumentReference):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
