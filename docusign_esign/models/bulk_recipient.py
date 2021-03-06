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


class BulkRecipient(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, access_code=None, email=None, error_details=None, identification=None, name=None, note=None, phone_number=None, recipient_signature_provider_info=None, row_number=None, tab_labels=None):
        """
        BulkRecipient - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'access_code': 'str',
            'email': 'str',
            'error_details': 'list[ErrorDetails]',
            'identification': 'str',
            'name': 'str',
            'note': 'str',
            'phone_number': 'str',
            'recipient_signature_provider_info': 'list[BulkRecipientSignatureProvider]',
            'row_number': 'str',
            'tab_labels': 'list[BulkRecipientTabLabel]'
        }

        self.attribute_map = {
            'access_code': 'accessCode',
            'email': 'email',
            'error_details': 'errorDetails',
            'identification': 'identification',
            'name': 'name',
            'note': 'note',
            'phone_number': 'phoneNumber',
            'recipient_signature_provider_info': 'recipientSignatureProviderInfo',
            'row_number': 'rowNumber',
            'tab_labels': 'tabLabels'
        }

        self._access_code = access_code
        self._email = email
        self._error_details = error_details
        self._identification = identification
        self._name = name
        self._note = note
        self._phone_number = phone_number
        self._recipient_signature_provider_info = recipient_signature_provider_info
        self._row_number = row_number
        self._tab_labels = tab_labels

    @property
    def access_code(self):
        """
        Gets the access_code of this BulkRecipient.
        If a value is provided, the recipient must enter the value as the access code to view and sign the envelope.   Maximum Length: 50 characters and it must conform to the account's access code format setting.  If blank, but the signer `accessCode` property is set in the envelope, then that value is used.  If blank and the signer `accessCode` property is not set, then the access code is not required.

        :return: The access_code of this BulkRecipient.
        :rtype: str
        """
        return self._access_code

    @access_code.setter
    def access_code(self, access_code):
        """
        Sets the access_code of this BulkRecipient.
        If a value is provided, the recipient must enter the value as the access code to view and sign the envelope.   Maximum Length: 50 characters and it must conform to the account's access code format setting.  If blank, but the signer `accessCode` property is set in the envelope, then that value is used.  If blank and the signer `accessCode` property is not set, then the access code is not required.

        :param access_code: The access_code of this BulkRecipient.
        :type: str
        """

        self._access_code = access_code

    @property
    def email(self):
        """
        Gets the email of this BulkRecipient.
        Specifies the recipient's email address.   Maximum length: 100 characters.

        :return: The email of this BulkRecipient.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """
        Sets the email of this BulkRecipient.
        Specifies the recipient's email address.   Maximum length: 100 characters.

        :param email: The email of this BulkRecipient.
        :type: str
        """

        self._email = email

    @property
    def error_details(self):
        """
        Gets the error_details of this BulkRecipient.
        Array or errors.

        :return: The error_details of this BulkRecipient.
        :rtype: list[ErrorDetails]
        """
        return self._error_details

    @error_details.setter
    def error_details(self, error_details):
        """
        Sets the error_details of this BulkRecipient.
        Array or errors.

        :param error_details: The error_details of this BulkRecipient.
        :type: list[ErrorDetails]
        """

        self._error_details = error_details

    @property
    def identification(self):
        """
        Gets the identification of this BulkRecipient.
        Specifies the authentication check used for the signer. If blank then no authentication check is required for the signer. Only one value can be used in this field.  The acceptable values are:  * KBA: Enables the normal ID check authentication set up for your account. * Phone: Enables phone authentication. * SMS: Enables SMS authentication.

        :return: The identification of this BulkRecipient.
        :rtype: str
        """
        return self._identification

    @identification.setter
    def identification(self, identification):
        """
        Sets the identification of this BulkRecipient.
        Specifies the authentication check used for the signer. If blank then no authentication check is required for the signer. Only one value can be used in this field.  The acceptable values are:  * KBA: Enables the normal ID check authentication set up for your account. * Phone: Enables phone authentication. * SMS: Enables SMS authentication.

        :param identification: The identification of this BulkRecipient.
        :type: str
        """

        self._identification = identification

    @property
    def name(self):
        """
        Gets the name of this BulkRecipient.
        Specifies the recipient's name.   Maximum length: 50 characters.

        :return: The name of this BulkRecipient.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this BulkRecipient.
        Specifies the recipient's name.   Maximum length: 50 characters.

        :param name: The name of this BulkRecipient.
        :type: str
        """

        self._name = name

    @property
    def note(self):
        """
        Gets the note of this BulkRecipient.
        Specifies a note that is unique to this recipient. This note is sent to the recipient via the signing email. The note displays in the signing UI near the upper left corner of the document on the signing screen.  Maximum Length: 1000 characters.

        :return: The note of this BulkRecipient.
        :rtype: str
        """
        return self._note

    @note.setter
    def note(self, note):
        """
        Sets the note of this BulkRecipient.
        Specifies a note that is unique to this recipient. This note is sent to the recipient via the signing email. The note displays in the signing UI near the upper left corner of the document on the signing screen.  Maximum Length: 1000 characters.

        :param note: The note of this BulkRecipient.
        :type: str
        """

        self._note = note

    @property
    def phone_number(self):
        """
        Gets the phone_number of this BulkRecipient.
        This is only used if the Identification field value is Phone or SMS. The value for this field can be a valid telephone number or, if Phone, usersupplied (SMS authentication cannot use a user supplied number). Parenthesis and dashes can be used in the telephone number.  If `usersupplied` is used, the signer supplies his or her own telephone number.

        :return: The phone_number of this BulkRecipient.
        :rtype: str
        """
        return self._phone_number

    @phone_number.setter
    def phone_number(self, phone_number):
        """
        Sets the phone_number of this BulkRecipient.
        This is only used if the Identification field value is Phone or SMS. The value for this field can be a valid telephone number or, if Phone, usersupplied (SMS authentication cannot use a user supplied number). Parenthesis and dashes can be used in the telephone number.  If `usersupplied` is used, the signer supplies his or her own telephone number.

        :param phone_number: The phone_number of this BulkRecipient.
        :type: str
        """

        self._phone_number = phone_number

    @property
    def recipient_signature_provider_info(self):
        """
        Gets the recipient_signature_provider_info of this BulkRecipient.
        

        :return: The recipient_signature_provider_info of this BulkRecipient.
        :rtype: list[BulkRecipientSignatureProvider]
        """
        return self._recipient_signature_provider_info

    @recipient_signature_provider_info.setter
    def recipient_signature_provider_info(self, recipient_signature_provider_info):
        """
        Sets the recipient_signature_provider_info of this BulkRecipient.
        

        :param recipient_signature_provider_info: The recipient_signature_provider_info of this BulkRecipient.
        :type: list[BulkRecipientSignatureProvider]
        """

        self._recipient_signature_provider_info = recipient_signature_provider_info

    @property
    def row_number(self):
        """
        Gets the row_number of this BulkRecipient.
        

        :return: The row_number of this BulkRecipient.
        :rtype: str
        """
        return self._row_number

    @row_number.setter
    def row_number(self, row_number):
        """
        Sets the row_number of this BulkRecipient.
        

        :param row_number: The row_number of this BulkRecipient.
        :type: str
        """

        self._row_number = row_number

    @property
    def tab_labels(self):
        """
        Gets the tab_labels of this BulkRecipient.
        Specifies values used to populate recipient tabs with information. This allows each bulk recipient signer to have different values for their associated tabs. Any number of `tabLabel` columns can be added to the bulk recipient file.  The information used in the bulk recipient file header must be the same as the `tabLabel` for the tab.  The values entered in this column are automatically inserted into the corresponding tab for the recipient in the same row.  Note that this option cannot be used for tabs that do not have data or that are automatically populated data such as Signature, Full Name, Email Address, Company, Title, and Date Signed tabs.

        :return: The tab_labels of this BulkRecipient.
        :rtype: list[BulkRecipientTabLabel]
        """
        return self._tab_labels

    @tab_labels.setter
    def tab_labels(self, tab_labels):
        """
        Sets the tab_labels of this BulkRecipient.
        Specifies values used to populate recipient tabs with information. This allows each bulk recipient signer to have different values for their associated tabs. Any number of `tabLabel` columns can be added to the bulk recipient file.  The information used in the bulk recipient file header must be the same as the `tabLabel` for the tab.  The values entered in this column are automatically inserted into the corresponding tab for the recipient in the same row.  Note that this option cannot be used for tabs that do not have data or that are automatically populated data such as Signature, Full Name, Email Address, Company, Title, and Date Signed tabs.

        :param tab_labels: The tab_labels of this BulkRecipient.
        :type: list[BulkRecipientTabLabel]
        """

        self._tab_labels = tab_labels

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
