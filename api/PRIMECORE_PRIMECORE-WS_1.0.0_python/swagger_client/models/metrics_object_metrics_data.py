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


class MetricsObjectMetricsData(object):
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
        'current_date_time': 'float',
        'metric_name': 'str',
        'description': 'str',
        'values': 'list[MetricsObjectMetricsDataValues]',
        'x_value_property': 'MetricsObjectMetricsDataXValueProperty',
        'y_value_property': 'MetricsObjectMetricsDataYValueProperty'
    }

    attribute_map = {
        'current_date_time': 'currentDateTime',
        'metric_name': 'metricName',
        'description': 'description',
        'values': 'values',
        'x_value_property': 'XValueProperty',
        'y_value_property': 'YValueProperty'
    }

    def __init__(self, current_date_time=None, metric_name=None, description=None, values=None, x_value_property=None, y_value_property=None):
        """
        MetricsObjectMetricsData - a model defined in Swagger
        """

        self._current_date_time = None
        self._metric_name = None
        self._description = None
        self._values = None
        self._x_value_property = None
        self._y_value_property = None

        if current_date_time is not None:
          self.current_date_time = current_date_time
        if metric_name is not None:
          self.metric_name = metric_name
        if description is not None:
          self.description = description
        if values is not None:
          self.values = values
        if x_value_property is not None:
          self.x_value_property = x_value_property
        if y_value_property is not None:
          self.y_value_property = y_value_property

    @property
    def current_date_time(self):
        """
        Gets the current_date_time of this MetricsObjectMetricsData.

        :return: The current_date_time of this MetricsObjectMetricsData.
        :rtype: float
        """
        return self._current_date_time

    @current_date_time.setter
    def current_date_time(self, current_date_time):
        """
        Sets the current_date_time of this MetricsObjectMetricsData.

        :param current_date_time: The current_date_time of this MetricsObjectMetricsData.
        :type: float
        """

        self._current_date_time = current_date_time

    @property
    def metric_name(self):
        """
        Gets the metric_name of this MetricsObjectMetricsData.

        :return: The metric_name of this MetricsObjectMetricsData.
        :rtype: str
        """
        return self._metric_name

    @metric_name.setter
    def metric_name(self, metric_name):
        """
        Sets the metric_name of this MetricsObjectMetricsData.

        :param metric_name: The metric_name of this MetricsObjectMetricsData.
        :type: str
        """

        self._metric_name = metric_name

    @property
    def description(self):
        """
        Gets the description of this MetricsObjectMetricsData.

        :return: The description of this MetricsObjectMetricsData.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this MetricsObjectMetricsData.

        :param description: The description of this MetricsObjectMetricsData.
        :type: str
        """

        self._description = description

    @property
    def values(self):
        """
        Gets the values of this MetricsObjectMetricsData.

        :return: The values of this MetricsObjectMetricsData.
        :rtype: list[MetricsObjectMetricsDataValues]
        """
        return self._values

    @values.setter
    def values(self, values):
        """
        Sets the values of this MetricsObjectMetricsData.

        :param values: The values of this MetricsObjectMetricsData.
        :type: list[MetricsObjectMetricsDataValues]
        """

        self._values = values

    @property
    def x_value_property(self):
        """
        Gets the x_value_property of this MetricsObjectMetricsData.

        :return: The x_value_property of this MetricsObjectMetricsData.
        :rtype: MetricsObjectMetricsDataXValueProperty
        """
        return self._x_value_property

    @x_value_property.setter
    def x_value_property(self, x_value_property):
        """
        Sets the x_value_property of this MetricsObjectMetricsData.

        :param x_value_property: The x_value_property of this MetricsObjectMetricsData.
        :type: MetricsObjectMetricsDataXValueProperty
        """

        self._x_value_property = x_value_property

    @property
    def y_value_property(self):
        """
        Gets the y_value_property of this MetricsObjectMetricsData.

        :return: The y_value_property of this MetricsObjectMetricsData.
        :rtype: MetricsObjectMetricsDataYValueProperty
        """
        return self._y_value_property

    @y_value_property.setter
    def y_value_property(self, y_value_property):
        """
        Sets the y_value_property of this MetricsObjectMetricsData.

        :param y_value_property: The y_value_property of this MetricsObjectMetricsData.
        :type: MetricsObjectMetricsDataYValueProperty
        """

        self._y_value_property = y_value_property

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
        if not isinstance(other, MetricsObjectMetricsData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
