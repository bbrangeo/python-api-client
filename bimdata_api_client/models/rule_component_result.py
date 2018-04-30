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


class RuleComponentResult(object):
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
        'name': 'str',
        'rule_result_id': 'int',
        'created_at': 'datetime',
        'updated_at': 'datetime',
        'results': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'rule_result_id': 'rule_result_id',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'results': 'results'
    }

    def __init__(self, id=None, name=None, rule_result_id=None, created_at=None, updated_at=None, results=None):  # noqa: E501
        """RuleComponentResult - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._name = None
        self._rule_result_id = None
        self._created_at = None
        self._updated_at = None
        self._results = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.name = name
        self.rule_result_id = rule_result_id
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if results is not None:
            self.results = results

    @property
    def id(self):
        """Gets the id of this RuleComponentResult.  # noqa: E501


        :return: The id of this RuleComponentResult.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this RuleComponentResult.


        :param id: The id of this RuleComponentResult.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this RuleComponentResult.  # noqa: E501


        :return: The name of this RuleComponentResult.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this RuleComponentResult.


        :param name: The name of this RuleComponentResult.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def rule_result_id(self):
        """Gets the rule_result_id of this RuleComponentResult.  # noqa: E501


        :return: The rule_result_id of this RuleComponentResult.  # noqa: E501
        :rtype: int
        """
        return self._rule_result_id

    @rule_result_id.setter
    def rule_result_id(self, rule_result_id):
        """Sets the rule_result_id of this RuleComponentResult.


        :param rule_result_id: The rule_result_id of this RuleComponentResult.  # noqa: E501
        :type: int
        """
        if rule_result_id is None:
            raise ValueError("Invalid value for `rule_result_id`, must not be `None`")  # noqa: E501

        self._rule_result_id = rule_result_id

    @property
    def created_at(self):
        """Gets the created_at of this RuleComponentResult.  # noqa: E501


        :return: The created_at of this RuleComponentResult.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this RuleComponentResult.


        :param created_at: The created_at of this RuleComponentResult.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this RuleComponentResult.  # noqa: E501


        :return: The updated_at of this RuleComponentResult.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this RuleComponentResult.


        :param updated_at: The updated_at of this RuleComponentResult.  # noqa: E501
        :type: datetime
        """

        self._updated_at = updated_at

    @property
    def results(self):
        """Gets the results of this RuleComponentResult.  # noqa: E501


        :return: The results of this RuleComponentResult.  # noqa: E501
        :rtype: str
        """
        return self._results

    @results.setter
    def results(self, results):
        """Sets the results of this RuleComponentResult.


        :param results: The results of this RuleComponentResult.  # noqa: E501
        :type: str
        """

        self._results = results

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
        if not isinstance(other, RuleComponentResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
