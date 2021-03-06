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

from bimdata_api_client.models.ifc_checker_checkplan import IfcCheckerCheckplan  # noqa: F401,E501
from bimdata_api_client.models.ifc_checker_ifc import IfcCheckerIfc  # noqa: F401,E501
from bimdata_api_client.models.ifc_checker_results import IfcCheckerResults  # noqa: F401,E501


class IfcChecker(object):
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
        'creator': 'int',
        'name': 'str',
        'ifc_id': 'int',
        'ifc': 'IfcCheckerIfc',
        'checkplan_id': 'int',
        'results': 'list[IfcCheckerResults]',
        'created_at': 'datetime',
        'updated_at': 'datetime',
        'checkplan': 'IfcCheckerCheckplan'
    }

    attribute_map = {
        'id': 'id',
        'creator': 'creator',
        'name': 'name',
        'ifc_id': 'ifc_id',
        'ifc': 'ifc',
        'checkplan_id': 'checkplan_id',
        'results': 'results',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'checkplan': 'checkplan'
    }

    def __init__(self, id=None, creator=None, name=None, ifc_id=None, ifc=None, checkplan_id=None, results=None, created_at=None, updated_at=None, checkplan=None):  # noqa: E501
        """IfcChecker - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._creator = None
        self._name = None
        self._ifc_id = None
        self._ifc = None
        self._checkplan_id = None
        self._results = None
        self._created_at = None
        self._updated_at = None
        self._checkplan = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if creator is not None:
            self.creator = creator
        if name is not None:
            self.name = name
        self.ifc_id = ifc_id
        if ifc is not None:
            self.ifc = ifc
        self.checkplan_id = checkplan_id
        if results is not None:
            self.results = results
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if checkplan is not None:
            self.checkplan = checkplan

    @property
    def id(self):
        """Gets the id of this IfcChecker.  # noqa: E501


        :return: The id of this IfcChecker.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this IfcChecker.


        :param id: The id of this IfcChecker.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def creator(self):
        """Gets the creator of this IfcChecker.  # noqa: E501


        :return: The creator of this IfcChecker.  # noqa: E501
        :rtype: int
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        """Sets the creator of this IfcChecker.


        :param creator: The creator of this IfcChecker.  # noqa: E501
        :type: int
        """

        self._creator = creator

    @property
    def name(self):
        """Gets the name of this IfcChecker.  # noqa: E501


        :return: The name of this IfcChecker.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this IfcChecker.


        :param name: The name of this IfcChecker.  # noqa: E501
        :type: str
        """
        if name is not None and len(name) > 256:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `256`")  # noqa: E501

        self._name = name

    @property
    def ifc_id(self):
        """Gets the ifc_id of this IfcChecker.  # noqa: E501


        :return: The ifc_id of this IfcChecker.  # noqa: E501
        :rtype: int
        """
        return self._ifc_id

    @ifc_id.setter
    def ifc_id(self, ifc_id):
        """Sets the ifc_id of this IfcChecker.


        :param ifc_id: The ifc_id of this IfcChecker.  # noqa: E501
        :type: int
        """
        if ifc_id is None:
            raise ValueError("Invalid value for `ifc_id`, must not be `None`")  # noqa: E501

        self._ifc_id = ifc_id

    @property
    def ifc(self):
        """Gets the ifc of this IfcChecker.  # noqa: E501


        :return: The ifc of this IfcChecker.  # noqa: E501
        :rtype: IfcCheckerIfc
        """
        return self._ifc

    @ifc.setter
    def ifc(self, ifc):
        """Sets the ifc of this IfcChecker.


        :param ifc: The ifc of this IfcChecker.  # noqa: E501
        :type: IfcCheckerIfc
        """

        self._ifc = ifc

    @property
    def checkplan_id(self):
        """Gets the checkplan_id of this IfcChecker.  # noqa: E501


        :return: The checkplan_id of this IfcChecker.  # noqa: E501
        :rtype: int
        """
        return self._checkplan_id

    @checkplan_id.setter
    def checkplan_id(self, checkplan_id):
        """Sets the checkplan_id of this IfcChecker.


        :param checkplan_id: The checkplan_id of this IfcChecker.  # noqa: E501
        :type: int
        """
        if checkplan_id is None:
            raise ValueError("Invalid value for `checkplan_id`, must not be `None`")  # noqa: E501

        self._checkplan_id = checkplan_id

    @property
    def results(self):
        """Gets the results of this IfcChecker.  # noqa: E501


        :return: The results of this IfcChecker.  # noqa: E501
        :rtype: list[IfcCheckerResults]
        """
        return self._results

    @results.setter
    def results(self, results):
        """Sets the results of this IfcChecker.


        :param results: The results of this IfcChecker.  # noqa: E501
        :type: list[IfcCheckerResults]
        """

        self._results = results

    @property
    def created_at(self):
        """Gets the created_at of this IfcChecker.  # noqa: E501


        :return: The created_at of this IfcChecker.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this IfcChecker.


        :param created_at: The created_at of this IfcChecker.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this IfcChecker.  # noqa: E501


        :return: The updated_at of this IfcChecker.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this IfcChecker.


        :param updated_at: The updated_at of this IfcChecker.  # noqa: E501
        :type: datetime
        """

        self._updated_at = updated_at

    @property
    def checkplan(self):
        """Gets the checkplan of this IfcChecker.  # noqa: E501


        :return: The checkplan of this IfcChecker.  # noqa: E501
        :rtype: IfcCheckerCheckplan
        """
        return self._checkplan

    @checkplan.setter
    def checkplan(self, checkplan):
        """Sets the checkplan of this IfcChecker.


        :param checkplan: The checkplan of this IfcChecker.  # noqa: E501
        :type: IfcCheckerCheckplan
        """

        self._checkplan = checkplan

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
        if not isinstance(other, IfcChecker):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
