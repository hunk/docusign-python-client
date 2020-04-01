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


class AskAnAdmin(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, email=None, message=None, name=None, phone=None):
        """
        AskAnAdmin - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'email': 'str',
            'message': 'str',
            'name': 'str',
            'phone': 'str'
        }

        self.attribute_map = {
            'email': 'email',
            'message': 'message',
            'name': 'name',
            'phone': 'phone'
        }

        self._email = email
        self._message = message
        self._name = name
        self._phone = phone

    @property
    def email(self):
        """
        Gets the email of this AskAnAdmin.
        

        :return: The email of this AskAnAdmin.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """
        Sets the email of this AskAnAdmin.
        

        :param email: The email of this AskAnAdmin.
        :type: str
        """

        self._email = email

    @property
    def message(self):
        """
        Gets the message of this AskAnAdmin.
        

        :return: The message of this AskAnAdmin.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """
        Sets the message of this AskAnAdmin.
        

        :param message: The message of this AskAnAdmin.
        :type: str
        """

        self._message = message

    @property
    def name(self):
        """
        Gets the name of this AskAnAdmin.
        

        :return: The name of this AskAnAdmin.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this AskAnAdmin.
        

        :param name: The name of this AskAnAdmin.
        :type: str
        """

        self._name = name

    @property
    def phone(self):
        """
        Gets the phone of this AskAnAdmin.
        

        :return: The phone of this AskAnAdmin.
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """
        Sets the phone of this AskAnAdmin.
        

        :param phone: The phone of this AskAnAdmin.
        :type: str
        """

        self._phone = phone

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