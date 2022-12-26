# coding: utf-8

"""
    Ledger API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1.9.0-beta.5
    Contact: support@numary.com
    Generated by: https://openapi-generator.tech
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from ledgerclient import schemas  # noqa: F401


class ErrorCode(
    schemas.EnumBase,
    schemas.StrSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        enum_value_to_name = {
            "INTERNAL": "INTERNAL",
            "INSUFFICIENT_FUND": "INSUFFICIENT_FUND",
            "VALIDATION": "VALIDATION",
            "CONFLICT": "CONFLICT",
        }
    
    @schemas.classproperty
    def INTERNAL(cls):
        return cls("INTERNAL")
    
    @schemas.classproperty
    def INSUFFICIENT_FUND(cls):
        return cls("INSUFFICIENT_FUND")
    
    @schemas.classproperty
    def VALIDATION(cls):
        return cls("VALIDATION")
    
    @schemas.classproperty
    def CONFLICT(cls):
        return cls("CONFLICT")
