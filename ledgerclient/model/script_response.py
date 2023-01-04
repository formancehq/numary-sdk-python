# coding: utf-8

"""
    Ledger API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1.9.0-rc.1
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


class ScriptResponse(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def errorCode() -> typing.Type['ErrorsEnum']:
                return ErrorsEnum
            errorMessage = schemas.StrSchema
            details = schemas.StrSchema
            
            
            class error_code(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "INTERNAL": "INTERNAL",
                        "INSUFFICIENT_FUND": "INSUFFICIENT_FUND",
                        "VALIDATION": "VALIDATION",
                        "CONFLICT": "CONFLICT",
                        "NO_SCRIPT": "NO_SCRIPT",
                        "COMPILATION_FAILED": "COMPILATION_FAILED",
                        "METADATA_OVERRIDE": "METADATA_OVERRIDE",
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
                
                @schemas.classproperty
                def NO_SCRIPT(cls):
                    return cls("NO_SCRIPT")
                
                @schemas.classproperty
                def COMPILATION_FAILED(cls):
                    return cls("COMPILATION_FAILED")
                
                @schemas.classproperty
                def METADATA_OVERRIDE(cls):
                    return cls("METADATA_OVERRIDE")
            error_message = schemas.StrSchema
        
            @staticmethod
            def transaction() -> typing.Type['Transaction']:
                return Transaction
            __annotations__ = {
                "errorCode": errorCode,
                "errorMessage": errorMessage,
                "details": details,
                "error_code": error_code,
                "error_message": error_message,
                "transaction": transaction,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["errorCode"]) -> 'ErrorsEnum': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["errorMessage"]) -> MetaOapg.properties.errorMessage: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["details"]) -> MetaOapg.properties.details: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["error_code"]) -> MetaOapg.properties.error_code: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["error_message"]) -> MetaOapg.properties.error_message: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["transaction"]) -> 'Transaction': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["errorCode", "errorMessage", "details", "error_code", "error_message", "transaction", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["errorCode"]) -> typing.Union['ErrorsEnum', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["errorMessage"]) -> typing.Union[MetaOapg.properties.errorMessage, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["details"]) -> typing.Union[MetaOapg.properties.details, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["error_code"]) -> typing.Union[MetaOapg.properties.error_code, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["error_message"]) -> typing.Union[MetaOapg.properties.error_message, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["transaction"]) -> typing.Union['Transaction', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["errorCode", "errorMessage", "details", "error_code", "error_message", "transaction", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        errorCode: typing.Union['ErrorsEnum', schemas.Unset] = schemas.unset,
        errorMessage: typing.Union[MetaOapg.properties.errorMessage, str, schemas.Unset] = schemas.unset,
        details: typing.Union[MetaOapg.properties.details, str, schemas.Unset] = schemas.unset,
        error_code: typing.Union[MetaOapg.properties.error_code, str, schemas.Unset] = schemas.unset,
        error_message: typing.Union[MetaOapg.properties.error_message, str, schemas.Unset] = schemas.unset,
        transaction: typing.Union['Transaction', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ScriptResponse':
        return super().__new__(
            cls,
            *_args,
            errorCode=errorCode,
            errorMessage=errorMessage,
            details=details,
            error_code=error_code,
            error_message=error_message,
            transaction=transaction,
            _configuration=_configuration,
            **kwargs,
        )

from ledgerclient.model.errors_enum import ErrorsEnum
from ledgerclient.model.transaction import Transaction
