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


class RecipientIdentityPhoneNumber(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, country_code=None, extension=None, number=None):
        """
        RecipientIdentityPhoneNumber - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'country_code': 'str',
            'extension': 'str',
            'number': 'str'
        }

        self.attribute_map = {
            'country_code': 'countryCode',
            'extension': 'extension',
            'number': 'number'
        }

        self._country_code = country_code
        self._extension = extension
        self._number = number

    @property
    def country_code(self):
        """
        Gets the country_code of this RecipientIdentityPhoneNumber.
        

        :return: The country_code of this RecipientIdentityPhoneNumber.
        :rtype: str
        """
        return self._country_code

    @country_code.setter
    def country_code(self, country_code):
        """
        Sets the country_code of this RecipientIdentityPhoneNumber.
        

        :param country_code: The country_code of this RecipientIdentityPhoneNumber.
        :type: str
        """

        self._country_code = country_code

    @property
    def extension(self):
        """
        Gets the extension of this RecipientIdentityPhoneNumber.
        

        :return: The extension of this RecipientIdentityPhoneNumber.
        :rtype: str
        """
        return self._extension

    @extension.setter
    def extension(self, extension):
        """
        Sets the extension of this RecipientIdentityPhoneNumber.
        

        :param extension: The extension of this RecipientIdentityPhoneNumber.
        :type: str
        """

        self._extension = extension

    @property
    def number(self):
        """
        Gets the number of this RecipientIdentityPhoneNumber.
        

        :return: The number of this RecipientIdentityPhoneNumber.
        :rtype: str
        """
        return self._number

    @number.setter
    def number(self, number):
        """
        Sets the number of this RecipientIdentityPhoneNumber.
        

        :param number: The number of this RecipientIdentityPhoneNumber.
        :type: str
        """

        self._number = number

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
