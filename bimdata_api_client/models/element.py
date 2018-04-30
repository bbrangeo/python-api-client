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

from bimdata_api_client.models.classification import Classification  # noqa: F401,E501
from bimdata_api_client.models.property_set import PropertySet  # noqa: F401,E501


class Element(object):
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
        'ifc_id': 'int',
        'uuid': 'str',
        'type': 'str',
        'attributes': 'PropertySet',
        'property_sets': 'list[PropertySet]',
        'classifications': 'list[Classification]'
    }

    attribute_map = {
        'id': 'id',
        'ifc_id': 'ifc_id',
        'uuid': 'uuid',
        'type': 'type',
        'attributes': 'attributes',
        'property_sets': 'property_sets',
        'classifications': 'classifications'
    }

    def __init__(self, id=None, ifc_id=None, uuid=None, type=None, attributes=None, property_sets=None, classifications=None):  # noqa: E501
        """Element - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._ifc_id = None
        self._uuid = None
        self._type = None
        self._attributes = None
        self._property_sets = None
        self._classifications = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if ifc_id is not None:
            self.ifc_id = ifc_id
        if uuid is not None:
            self.uuid = uuid
        self.type = type
        if attributes is not None:
            self.attributes = attributes
        if property_sets is not None:
            self.property_sets = property_sets
        if classifications is not None:
            self.classifications = classifications

    @property
    def id(self):
        """Gets the id of this Element.  # noqa: E501


        :return: The id of this Element.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Element.


        :param id: The id of this Element.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def ifc_id(self):
        """Gets the ifc_id of this Element.  # noqa: E501


        :return: The ifc_id of this Element.  # noqa: E501
        :rtype: int
        """
        return self._ifc_id

    @ifc_id.setter
    def ifc_id(self, ifc_id):
        """Sets the ifc_id of this Element.


        :param ifc_id: The ifc_id of this Element.  # noqa: E501
        :type: int
        """

        self._ifc_id = ifc_id

    @property
    def uuid(self):
        """Gets the uuid of this Element.  # noqa: E501


        :return: The uuid of this Element.  # noqa: E501
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this Element.


        :param uuid: The uuid of this Element.  # noqa: E501
        :type: str
        """
        if uuid is not None and len(uuid) > 22:
            raise ValueError("Invalid value for `uuid`, length must be less than or equal to `22`")  # noqa: E501
        if uuid is not None and len(uuid) < 22:
            raise ValueError("Invalid value for `uuid`, length must be greater than or equal to `22`")  # noqa: E501

        self._uuid = uuid

    @property
    def type(self):
        """Gets the type of this Element.  # noqa: E501

        IFC type for the element  # noqa: E501

        :return: The type of this Element.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Element.

        IFC type for the element  # noqa: E501

        :param type: The type of this Element.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def attributes(self):
        """Gets the attributes of this Element.  # noqa: E501


        :return: The attributes of this Element.  # noqa: E501
        :rtype: PropertySet
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """Sets the attributes of this Element.


        :param attributes: The attributes of this Element.  # noqa: E501
        :type: PropertySet
        """

        self._attributes = attributes

    @property
    def property_sets(self):
        """Gets the property_sets of this Element.  # noqa: E501


        :return: The property_sets of this Element.  # noqa: E501
        :rtype: list[PropertySet]
        """
        return self._property_sets

    @property_sets.setter
    def property_sets(self, property_sets):
        """Sets the property_sets of this Element.


        :param property_sets: The property_sets of this Element.  # noqa: E501
        :type: list[PropertySet]
        """

        self._property_sets = property_sets

    @property
    def classifications(self):
        """Gets the classifications of this Element.  # noqa: E501


        :return: The classifications of this Element.  # noqa: E501
        :rtype: list[Classification]
        """
        return self._classifications

    @classifications.setter
    def classifications(self, classifications):
        """Sets the classifications of this Element.


        :param classifications: The classifications of this Element.  # noqa: E501
        :type: list[Classification]
        """

        self._classifications = classifications

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
        if not isinstance(other, Element):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other