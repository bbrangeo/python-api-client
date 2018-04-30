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


class ProjectRootFolder(object):
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
        'created_at': 'datetime',
        'updated_at': 'datetime',
        'lft': 'int',
        'rght': 'int',
        'tree_id': 'int',
        'level': 'int',
        'creator': 'int',
        'project': 'int',
        'parent': 'int'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'lft': 'lft',
        'rght': 'rght',
        'tree_id': 'tree_id',
        'level': 'level',
        'creator': 'creator',
        'project': 'project',
        'parent': 'parent'
    }

    def __init__(self, id=None, name=None, created_at=None, updated_at=None, lft=None, rght=None, tree_id=None, level=None, creator=None, project=None, parent=None):  # noqa: E501
        """ProjectRootFolder - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._name = None
        self._created_at = None
        self._updated_at = None
        self._lft = None
        self._rght = None
        self._tree_id = None
        self._level = None
        self._creator = None
        self._project = None
        self._parent = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.name = name
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if lft is not None:
            self.lft = lft
        if rght is not None:
            self.rght = rght
        if tree_id is not None:
            self.tree_id = tree_id
        if level is not None:
            self.level = level
        if creator is not None:
            self.creator = creator
        if project is not None:
            self.project = project
        if parent is not None:
            self.parent = parent

    @property
    def id(self):
        """Gets the id of this ProjectRootFolder.  # noqa: E501


        :return: The id of this ProjectRootFolder.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ProjectRootFolder.


        :param id: The id of this ProjectRootFolder.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this ProjectRootFolder.  # noqa: E501


        :return: The name of this ProjectRootFolder.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ProjectRootFolder.


        :param name: The name of this ProjectRootFolder.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if name is not None and len(name) > 255:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `255`")  # noqa: E501

        self._name = name

    @property
    def created_at(self):
        """Gets the created_at of this ProjectRootFolder.  # noqa: E501


        :return: The created_at of this ProjectRootFolder.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this ProjectRootFolder.


        :param created_at: The created_at of this ProjectRootFolder.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this ProjectRootFolder.  # noqa: E501


        :return: The updated_at of this ProjectRootFolder.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this ProjectRootFolder.


        :param updated_at: The updated_at of this ProjectRootFolder.  # noqa: E501
        :type: datetime
        """

        self._updated_at = updated_at

    @property
    def lft(self):
        """Gets the lft of this ProjectRootFolder.  # noqa: E501


        :return: The lft of this ProjectRootFolder.  # noqa: E501
        :rtype: int
        """
        return self._lft

    @lft.setter
    def lft(self, lft):
        """Sets the lft of this ProjectRootFolder.


        :param lft: The lft of this ProjectRootFolder.  # noqa: E501
        :type: int
        """

        self._lft = lft

    @property
    def rght(self):
        """Gets the rght of this ProjectRootFolder.  # noqa: E501


        :return: The rght of this ProjectRootFolder.  # noqa: E501
        :rtype: int
        """
        return self._rght

    @rght.setter
    def rght(self, rght):
        """Sets the rght of this ProjectRootFolder.


        :param rght: The rght of this ProjectRootFolder.  # noqa: E501
        :type: int
        """

        self._rght = rght

    @property
    def tree_id(self):
        """Gets the tree_id of this ProjectRootFolder.  # noqa: E501


        :return: The tree_id of this ProjectRootFolder.  # noqa: E501
        :rtype: int
        """
        return self._tree_id

    @tree_id.setter
    def tree_id(self, tree_id):
        """Sets the tree_id of this ProjectRootFolder.


        :param tree_id: The tree_id of this ProjectRootFolder.  # noqa: E501
        :type: int
        """

        self._tree_id = tree_id

    @property
    def level(self):
        """Gets the level of this ProjectRootFolder.  # noqa: E501


        :return: The level of this ProjectRootFolder.  # noqa: E501
        :rtype: int
        """
        return self._level

    @level.setter
    def level(self, level):
        """Sets the level of this ProjectRootFolder.


        :param level: The level of this ProjectRootFolder.  # noqa: E501
        :type: int
        """

        self._level = level

    @property
    def creator(self):
        """Gets the creator of this ProjectRootFolder.  # noqa: E501


        :return: The creator of this ProjectRootFolder.  # noqa: E501
        :rtype: int
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        """Sets the creator of this ProjectRootFolder.


        :param creator: The creator of this ProjectRootFolder.  # noqa: E501
        :type: int
        """

        self._creator = creator

    @property
    def project(self):
        """Gets the project of this ProjectRootFolder.  # noqa: E501


        :return: The project of this ProjectRootFolder.  # noqa: E501
        :rtype: int
        """
        return self._project

    @project.setter
    def project(self, project):
        """Sets the project of this ProjectRootFolder.


        :param project: The project of this ProjectRootFolder.  # noqa: E501
        :type: int
        """

        self._project = project

    @property
    def parent(self):
        """Gets the parent of this ProjectRootFolder.  # noqa: E501


        :return: The parent of this ProjectRootFolder.  # noqa: E501
        :rtype: int
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """Sets the parent of this ProjectRootFolder.


        :param parent: The parent of this ProjectRootFolder.  # noqa: E501
        :type: int
        """

        self._parent = parent

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
        if not isinstance(other, ProjectRootFolder):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
