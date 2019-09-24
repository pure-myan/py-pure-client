# coding: utf-8

"""
    Pure1 Public REST API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from ...properties import Property
import pprint
import re

import six


class Alert(object):


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'as_of': 'int',
        'id': 'str',
        'name': 'str',
        'arrays': 'list[FixedReference]',
        'actual': 'str',
        'category': 'str',
        'closed': 'int',
        'code': 'int',
        'component_name': 'str',
        'component_type': 'str',
        'created': 'int',
        'description': 'str',
        'expected': 'str',
        'knowledge_base_url': 'str',
        'notified': 'int',
        'origin': 'str',
        'severity': 'str',
        'state': 'str',
        'summary': 'str',
        'updated': 'int'
    }

    attribute_map = {
        'as_of': '_as_of',
        'id': 'id',
        'name': 'name',
        'arrays': 'arrays',
        'actual': 'actual',
        'category': 'category',
        'closed': 'closed',
        'code': 'code',
        'component_name': 'component_name',
        'component_type': 'component_type',
        'created': 'created',
        'description': 'description',
        'expected': 'expected',
        'knowledge_base_url': 'knowledge_base_url',
        'notified': 'notified',
        'origin': 'origin',
        'severity': 'severity',
        'state': 'state',
        'summary': 'summary',
        'updated': 'updated'
    }

    required_args = {
        'as_of',
    }

    def __init__(self, **kwargs):
        """
        Keyword args:
            as_of (int, required): The freshness of the data (timestamp in millis since epoch).
            id (str): A non-modifiable, globally unique ID chosen by the system.
            name (str): A modifiable, locally unique name chosen by the user.
            arrays (list[FixedReference]): The list of arrays where this resource exists. Many resources are on a single array, but some resources, such as pods, can be shared across multiple arrays.
            actual (str): Actual condition at the time of the alert.
            category (str): Category of the alert. Valid values are `array`, `hardware`, and `software`.
            closed (int): Time when the alert was closed, in milliseconds since UNIX epoch.
            code (int): Code associated with the alert.
            component_name (str): Name of the component alerted about.
            component_type (str): Type of the component alerted about.
            created (int): Time when the alert was created, in milliseconds since UNIX epoch.
            description (str): Short description of the alert.
            expected (str): Expected state/threshold under normal conditions.
            knowledge_base_url (str): URL of the relevant Knowledge Base page.
            notified (int): Time when the user was notified of the alert, in milliseconds since UNIX epoch.
            origin (str): Origin of the alert. Valid values are `array` and `Pure1`.
            severity (str): Current severity level. Valid values are `info`, `warning`, `critical`, and `hidden`.
            state (str): Current state of the alert. Valid values are `open`, `closing`, and `closed`.
            summary (str): Summary of the alert.
            updated (int): Time when the alert was last updated, in milliseconds since UNIX epoch.
        """
        for arg in kwargs:
            setattr(self, arg, kwargs[arg])
        for arg in self.required_args:
            if arg not in kwargs:
                raise Exception("Required argument {} is missing".format(arg))

    def __setattr__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `Alert`".format(key))
        if key == "as_of" and value is None:
            raise ValueError("Invalid value for `as_of`, must not be `None`")
        self.__dict__[key] = value

    def __getattribute__(self, item):
        value = object.__getattribute__(self, item)
        if isinstance(value, Property):
            raise AttributeError
        else:
            return value

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            if hasattr(self, attr):
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
        if issubclass(Alert, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Alert):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
