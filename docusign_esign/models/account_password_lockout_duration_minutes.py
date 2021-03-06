# coding: utf-8

"""
    DocuSign REST API

    The DocuSign REST API provides you with a powerful, convenient, and simple Web services API for interacting with DocuSign.

    OpenAPI spec version: v2.1
    Contact: devcenter@docusign.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class AccountPasswordLockoutDurationMinutes(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, maximum_minutes=None, minimum_minutes=None):
        """
        AccountPasswordLockoutDurationMinutes - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'maximum_minutes': 'str',
            'minimum_minutes': 'str'
        }

        self.attribute_map = {
            'maximum_minutes': 'maximumMinutes',
            'minimum_minutes': 'minimumMinutes'
        }

        self._maximum_minutes = maximum_minutes
        self._minimum_minutes = minimum_minutes

    @property
    def maximum_minutes(self):
        """
        Gets the maximum_minutes of this AccountPasswordLockoutDurationMinutes.
        

        :return: The maximum_minutes of this AccountPasswordLockoutDurationMinutes.
        :rtype: str
        """
        return self._maximum_minutes

    @maximum_minutes.setter
    def maximum_minutes(self, maximum_minutes):
        """
        Sets the maximum_minutes of this AccountPasswordLockoutDurationMinutes.
        

        :param maximum_minutes: The maximum_minutes of this AccountPasswordLockoutDurationMinutes.
        :type: str
        """

        self._maximum_minutes = maximum_minutes

    @property
    def minimum_minutes(self):
        """
        Gets the minimum_minutes of this AccountPasswordLockoutDurationMinutes.
        

        :return: The minimum_minutes of this AccountPasswordLockoutDurationMinutes.
        :rtype: str
        """
        return self._minimum_minutes

    @minimum_minutes.setter
    def minimum_minutes(self, minimum_minutes):
        """
        Sets the minimum_minutes of this AccountPasswordLockoutDurationMinutes.
        

        :param minimum_minutes: The minimum_minutes of this AccountPasswordLockoutDurationMinutes.
        :type: str
        """

        self._minimum_minutes = minimum_minutes

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
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
