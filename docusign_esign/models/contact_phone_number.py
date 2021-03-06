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


class ContactPhoneNumber(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, phone_number=None, phone_type=None):
        """
        ContactPhoneNumber - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'phone_number': 'str',
            'phone_type': 'str'
        }

        self.attribute_map = {
            'phone_number': 'phoneNumber',
            'phone_type': 'phoneType'
        }

        self._phone_number = phone_number
        self._phone_type = phone_type

    @property
    def phone_number(self):
        """
        Gets the phone_number of this ContactPhoneNumber.
        

        :return: The phone_number of this ContactPhoneNumber.
        :rtype: str
        """
        return self._phone_number

    @phone_number.setter
    def phone_number(self, phone_number):
        """
        Sets the phone_number of this ContactPhoneNumber.
        

        :param phone_number: The phone_number of this ContactPhoneNumber.
        :type: str
        """

        self._phone_number = phone_number

    @property
    def phone_type(self):
        """
        Gets the phone_type of this ContactPhoneNumber.
        

        :return: The phone_type of this ContactPhoneNumber.
        :rtype: str
        """
        return self._phone_type

    @phone_type.setter
    def phone_type(self, phone_type):
        """
        Sets the phone_type of this ContactPhoneNumber.
        

        :param phone_type: The phone_type of this ContactPhoneNumber.
        :type: str
        """

        self._phone_type = phone_type

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
