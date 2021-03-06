# coding: utf-8

"""
    PRIMECORE_PRIMECORE-WS

    API Definition of primecore

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class InlineResponse2002DeviceTypeCounts(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
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
        'device_type': 'str',
        'count': 'float'
    }

    attribute_map = {
        'device_type': 'deviceType',
        'count': 'count'
    }

    def __init__(self, device_type=None, count=None):
        """
        InlineResponse2002DeviceTypeCounts - a model defined in Swagger
        """

        self._device_type = None
        self._count = None

        if device_type is not None:
          self.device_type = device_type
        if count is not None:
          self.count = count

    @property
    def device_type(self):
        """
        Gets the device_type of this InlineResponse2002DeviceTypeCounts.

        :return: The device_type of this InlineResponse2002DeviceTypeCounts.
        :rtype: str
        """
        return self._device_type

    @device_type.setter
    def device_type(self, device_type):
        """
        Sets the device_type of this InlineResponse2002DeviceTypeCounts.

        :param device_type: The device_type of this InlineResponse2002DeviceTypeCounts.
        :type: str
        """

        self._device_type = device_type

    @property
    def count(self):
        """
        Gets the count of this InlineResponse2002DeviceTypeCounts.

        :return: The count of this InlineResponse2002DeviceTypeCounts.
        :rtype: float
        """
        return self._count

    @count.setter
    def count(self, count):
        """
        Sets the count of this InlineResponse2002DeviceTypeCounts.

        :param count: The count of this InlineResponse2002DeviceTypeCounts.
        :type: float
        """

        self._count = count

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, InlineResponse2002DeviceTypeCounts):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
