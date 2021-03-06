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

from bimdata_api_client.models.rule import Rule  # noqa: F401,E501


class Ruleset(object):
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
        'check_plan_id': 'int',
        'parent_ruleset_id': 'int',
        'name': 'str',
        'description': 'str',
        'rules': 'list[Rule]',
        'rulesets': 'list[str]'
    }

    attribute_map = {
        'id': 'id',
        'check_plan_id': 'check_plan_id',
        'parent_ruleset_id': 'parent_ruleset_id',
        'name': 'name',
        'description': 'description',
        'rules': 'rules',
        'rulesets': 'rulesets'
    }

    def __init__(self, id=None, check_plan_id=None, parent_ruleset_id=None, name=None, description=None, rules=None, rulesets=None):  # noqa: E501
        """Ruleset - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._check_plan_id = None
        self._parent_ruleset_id = None
        self._name = None
        self._description = None
        self._rules = None
        self._rulesets = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if check_plan_id is not None:
            self.check_plan_id = check_plan_id
        if parent_ruleset_id is not None:
            self.parent_ruleset_id = parent_ruleset_id
        self.name = name
        if description is not None:
            self.description = description
        if rules is not None:
            self.rules = rules
        if rulesets is not None:
            self.rulesets = rulesets

    @property
    def id(self):
        """Gets the id of this Ruleset.  # noqa: E501


        :return: The id of this Ruleset.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Ruleset.


        :param id: The id of this Ruleset.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def check_plan_id(self):
        """Gets the check_plan_id of this Ruleset.  # noqa: E501


        :return: The check_plan_id of this Ruleset.  # noqa: E501
        :rtype: int
        """
        return self._check_plan_id

    @check_plan_id.setter
    def check_plan_id(self, check_plan_id):
        """Sets the check_plan_id of this Ruleset.


        :param check_plan_id: The check_plan_id of this Ruleset.  # noqa: E501
        :type: int
        """

        self._check_plan_id = check_plan_id

    @property
    def parent_ruleset_id(self):
        """Gets the parent_ruleset_id of this Ruleset.  # noqa: E501


        :return: The parent_ruleset_id of this Ruleset.  # noqa: E501
        :rtype: int
        """
        return self._parent_ruleset_id

    @parent_ruleset_id.setter
    def parent_ruleset_id(self, parent_ruleset_id):
        """Sets the parent_ruleset_id of this Ruleset.


        :param parent_ruleset_id: The parent_ruleset_id of this Ruleset.  # noqa: E501
        :type: int
        """

        self._parent_ruleset_id = parent_ruleset_id

    @property
    def name(self):
        """Gets the name of this Ruleset.  # noqa: E501


        :return: The name of this Ruleset.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Ruleset.


        :param name: The name of this Ruleset.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def description(self):
        """Gets the description of this Ruleset.  # noqa: E501


        :return: The description of this Ruleset.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Ruleset.


        :param description: The description of this Ruleset.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def rules(self):
        """Gets the rules of this Ruleset.  # noqa: E501


        :return: The rules of this Ruleset.  # noqa: E501
        :rtype: list[Rule]
        """
        return self._rules

    @rules.setter
    def rules(self, rules):
        """Sets the rules of this Ruleset.


        :param rules: The rules of this Ruleset.  # noqa: E501
        :type: list[Rule]
        """

        self._rules = rules

    @property
    def rulesets(self):
        """Gets the rulesets of this Ruleset.  # noqa: E501


        :return: The rulesets of this Ruleset.  # noqa: E501
        :rtype: list[str]
        """
        return self._rulesets

    @rulesets.setter
    def rulesets(self, rulesets):
        """Sets the rulesets of this Ruleset.


        :param rulesets: The rulesets of this Ruleset.  # noqa: E501
        :type: list[str]
        """

        self._rulesets = rulesets

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
        if not isinstance(other, Ruleset):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
