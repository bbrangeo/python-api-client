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

from bimdata_api_client.models.bitmap import Bitmap  # noqa: F401,E501
from bimdata_api_client.models.clipping_plane import ClippingPlane  # noqa: F401,E501
from bimdata_api_client.models.components_parent import ComponentsParent  # noqa: F401,E501
from bimdata_api_client.models.line_seriaizer import LineSeriaizer  # noqa: F401,E501
from bimdata_api_client.models.orthogonal_camera import OrthogonalCamera  # noqa: F401,E501
from bimdata_api_client.models.perspective_camera import PerspectiveCamera  # noqa: F401,E501
from bimdata_api_client.models.snapshot import Snapshot  # noqa: F401,E501


class Viewpoint(object):
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
        'index': 'int',
        'guid': 'str',
        'orthogonal_camera': 'OrthogonalCamera',
        'perspective_camera': 'PerspectiveCamera',
        'lines': 'list[LineSeriaizer]',
        'clipping_planes': 'list[ClippingPlane]',
        'bitmaps': 'list[Bitmap]',
        'snapshot': 'Snapshot',
        'components': 'ComponentsParent'
    }

    attribute_map = {
        'index': 'index',
        'guid': 'guid',
        'orthogonal_camera': 'orthogonal_camera',
        'perspective_camera': 'perspective_camera',
        'lines': 'lines',
        'clipping_planes': 'clipping_planes',
        'bitmaps': 'bitmaps',
        'snapshot': 'snapshot',
        'components': 'components'
    }

    def __init__(self, index=None, guid=None, orthogonal_camera=None, perspective_camera=None, lines=None, clipping_planes=None, bitmaps=None, snapshot=None, components=None):  # noqa: E501
        """Viewpoint - a model defined in Swagger"""  # noqa: E501

        self._index = None
        self._guid = None
        self._orthogonal_camera = None
        self._perspective_camera = None
        self._lines = None
        self._clipping_planes = None
        self._bitmaps = None
        self._snapshot = None
        self._components = None
        self.discriminator = None

        if index is not None:
            self.index = index
        if guid is not None:
            self.guid = guid
        if orthogonal_camera is not None:
            self.orthogonal_camera = orthogonal_camera
        if perspective_camera is not None:
            self.perspective_camera = perspective_camera
        if lines is not None:
            self.lines = lines
        if clipping_planes is not None:
            self.clipping_planes = clipping_planes
        if bitmaps is not None:
            self.bitmaps = bitmaps
        if snapshot is not None:
            self.snapshot = snapshot
        if components is not None:
            self.components = components

    @property
    def index(self):
        """Gets the index of this Viewpoint.  # noqa: E501


        :return: The index of this Viewpoint.  # noqa: E501
        :rtype: int
        """
        return self._index

    @index.setter
    def index(self, index):
        """Sets the index of this Viewpoint.


        :param index: The index of this Viewpoint.  # noqa: E501
        :type: int
        """
        if index is not None and index > 2147483647:  # noqa: E501
            raise ValueError("Invalid value for `index`, must be a value less than or equal to `2147483647`")  # noqa: E501
        if index is not None and index < -2147483648:  # noqa: E501
            raise ValueError("Invalid value for `index`, must be a value greater than or equal to `-2147483648`")  # noqa: E501

        self._index = index

    @property
    def guid(self):
        """Gets the guid of this Viewpoint.  # noqa: E501


        :return: The guid of this Viewpoint.  # noqa: E501
        :rtype: str
        """
        return self._guid

    @guid.setter
    def guid(self, guid):
        """Sets the guid of this Viewpoint.


        :param guid: The guid of this Viewpoint.  # noqa: E501
        :type: str
        """

        self._guid = guid

    @property
    def orthogonal_camera(self):
        """Gets the orthogonal_camera of this Viewpoint.  # noqa: E501


        :return: The orthogonal_camera of this Viewpoint.  # noqa: E501
        :rtype: OrthogonalCamera
        """
        return self._orthogonal_camera

    @orthogonal_camera.setter
    def orthogonal_camera(self, orthogonal_camera):
        """Sets the orthogonal_camera of this Viewpoint.


        :param orthogonal_camera: The orthogonal_camera of this Viewpoint.  # noqa: E501
        :type: OrthogonalCamera
        """

        self._orthogonal_camera = orthogonal_camera

    @property
    def perspective_camera(self):
        """Gets the perspective_camera of this Viewpoint.  # noqa: E501


        :return: The perspective_camera of this Viewpoint.  # noqa: E501
        :rtype: PerspectiveCamera
        """
        return self._perspective_camera

    @perspective_camera.setter
    def perspective_camera(self, perspective_camera):
        """Sets the perspective_camera of this Viewpoint.


        :param perspective_camera: The perspective_camera of this Viewpoint.  # noqa: E501
        :type: PerspectiveCamera
        """

        self._perspective_camera = perspective_camera

    @property
    def lines(self):
        """Gets the lines of this Viewpoint.  # noqa: E501


        :return: The lines of this Viewpoint.  # noqa: E501
        :rtype: list[LineSeriaizer]
        """
        return self._lines

    @lines.setter
    def lines(self, lines):
        """Sets the lines of this Viewpoint.


        :param lines: The lines of this Viewpoint.  # noqa: E501
        :type: list[LineSeriaizer]
        """

        self._lines = lines

    @property
    def clipping_planes(self):
        """Gets the clipping_planes of this Viewpoint.  # noqa: E501


        :return: The clipping_planes of this Viewpoint.  # noqa: E501
        :rtype: list[ClippingPlane]
        """
        return self._clipping_planes

    @clipping_planes.setter
    def clipping_planes(self, clipping_planes):
        """Sets the clipping_planes of this Viewpoint.


        :param clipping_planes: The clipping_planes of this Viewpoint.  # noqa: E501
        :type: list[ClippingPlane]
        """

        self._clipping_planes = clipping_planes

    @property
    def bitmaps(self):
        """Gets the bitmaps of this Viewpoint.  # noqa: E501


        :return: The bitmaps of this Viewpoint.  # noqa: E501
        :rtype: list[Bitmap]
        """
        return self._bitmaps

    @bitmaps.setter
    def bitmaps(self, bitmaps):
        """Sets the bitmaps of this Viewpoint.


        :param bitmaps: The bitmaps of this Viewpoint.  # noqa: E501
        :type: list[Bitmap]
        """

        self._bitmaps = bitmaps

    @property
    def snapshot(self):
        """Gets the snapshot of this Viewpoint.  # noqa: E501


        :return: The snapshot of this Viewpoint.  # noqa: E501
        :rtype: Snapshot
        """
        return self._snapshot

    @snapshot.setter
    def snapshot(self, snapshot):
        """Sets the snapshot of this Viewpoint.


        :param snapshot: The snapshot of this Viewpoint.  # noqa: E501
        :type: Snapshot
        """

        self._snapshot = snapshot

    @property
    def components(self):
        """Gets the components of this Viewpoint.  # noqa: E501


        :return: The components of this Viewpoint.  # noqa: E501
        :rtype: ComponentsParent
        """
        return self._components

    @components.setter
    def components(self, components):
        """Sets the components of this Viewpoint.


        :param components: The components of this Viewpoint.  # noqa: E501
        :type: ComponentsParent
        """

        self._components = components

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
        if not isinstance(other, Viewpoint):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
