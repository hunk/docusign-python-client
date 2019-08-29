# coding: utf-8

"""
    DocuSign REST API

    The DocuSign REST API provides you with a powerful, convenient, and simple Web services API for interacting with DocuSign.

    OpenAPI spec version: v2
    Contact: devcenter@docusign.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class CompleteSignHashResponse(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, documents=None, redirection_url=None, remaining_signature_requests=None):
        """
        CompleteSignHashResponse - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'documents': 'list[SignHashDocument]',
            'redirection_url': 'str',
            'remaining_signature_requests': 'str'
        }

        self.attribute_map = {
            'documents': 'documents',
            'redirection_url': 'redirectionUrl',
            'remaining_signature_requests': 'remainingSignatureRequests'
        }

        self._documents = documents
        self._redirection_url = redirection_url
        self._remaining_signature_requests = remaining_signature_requests

    @property
    def documents(self):
        """
        Gets the documents of this CompleteSignHashResponse.
        Complex element contains the details on the documents in the envelope.

        :return: The documents of this CompleteSignHashResponse.
        :rtype: list[SignHashDocument]
        """
        return self._documents

    @documents.setter
    def documents(self, documents):
        """
        Sets the documents of this CompleteSignHashResponse.
        Complex element contains the details on the documents in the envelope.

        :param documents: The documents of this CompleteSignHashResponse.
        :type: list[SignHashDocument]
        """

        self._documents = documents

    @property
    def redirection_url(self):
        """
        Gets the redirection_url of this CompleteSignHashResponse.
        

        :return: The redirection_url of this CompleteSignHashResponse.
        :rtype: str
        """
        return self._redirection_url

    @redirection_url.setter
    def redirection_url(self, redirection_url):
        """
        Sets the redirection_url of this CompleteSignHashResponse.
        

        :param redirection_url: The redirection_url of this CompleteSignHashResponse.
        :type: str
        """

        self._redirection_url = redirection_url

    @property
    def remaining_signature_requests(self):
        """
        Gets the remaining_signature_requests of this CompleteSignHashResponse.
        

        :return: The remaining_signature_requests of this CompleteSignHashResponse.
        :rtype: str
        """
        return self._remaining_signature_requests

    @remaining_signature_requests.setter
    def remaining_signature_requests(self, remaining_signature_requests):
        """
        Sets the remaining_signature_requests of this CompleteSignHashResponse.
        

        :param remaining_signature_requests: The remaining_signature_requests of this CompleteSignHashResponse.
        :type: str
        """

        self._remaining_signature_requests = remaining_signature_requests

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