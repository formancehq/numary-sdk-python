# coding: utf-8

"""
    Ledger API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1.9.4
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


class PostTransaction(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            timestamp = schemas.DateTimeSchema
            
            
            class postings(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['Posting']:
                        return Posting
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['Posting'], typing.List['Posting']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'postings':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'Posting':
                    return super().__getitem__(i)
            
            
            class script(
                schemas.DictSchema
            ):
            
            
                class MetaOapg:
                    required = {
                        "plain",
                    }
                    
                    class properties:
                        plain = schemas.StrSchema
                        vars = schemas.DictSchema
                        __annotations__ = {
                            "plain": plain,
                            "vars": vars,
                        }
                
                plain: MetaOapg.properties.plain
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["plain"]) -> MetaOapg.properties.plain: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["vars"]) -> MetaOapg.properties.vars: ...
                
                @typing.overload
                def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                
                def __getitem__(self, name: typing.Union[typing_extensions.Literal["plain", "vars", ], str]):
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["plain"]) -> MetaOapg.properties.plain: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["vars"]) -> typing.Union[MetaOapg.properties.vars, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                
                def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["plain", "vars", ], str]):
                    return super().get_item_oapg(name)
                
            
                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, ],
                    plain: typing.Union[MetaOapg.properties.plain, str, ],
                    vars: typing.Union[MetaOapg.properties.vars, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'script':
                    return super().__new__(
                        cls,
                        *_args,
                        plain=plain,
                        vars=vars,
                        _configuration=_configuration,
                        **kwargs,
                    )
            reference = schemas.StrSchema
        
            @staticmethod
            def metadata() -> typing.Type['Metadata']:
                return Metadata
            __annotations__ = {
                "timestamp": timestamp,
                "postings": postings,
                "script": script,
                "reference": reference,
                "metadata": metadata,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["timestamp"]) -> MetaOapg.properties.timestamp: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["postings"]) -> MetaOapg.properties.postings: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["script"]) -> MetaOapg.properties.script: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["reference"]) -> MetaOapg.properties.reference: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["metadata"]) -> 'Metadata': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["timestamp", "postings", "script", "reference", "metadata", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["timestamp"]) -> typing.Union[MetaOapg.properties.timestamp, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["postings"]) -> typing.Union[MetaOapg.properties.postings, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["script"]) -> typing.Union[MetaOapg.properties.script, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["reference"]) -> typing.Union[MetaOapg.properties.reference, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["metadata"]) -> typing.Union['Metadata', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["timestamp", "postings", "script", "reference", "metadata", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        timestamp: typing.Union[MetaOapg.properties.timestamp, str, datetime, schemas.Unset] = schemas.unset,
        postings: typing.Union[MetaOapg.properties.postings, list, tuple, schemas.Unset] = schemas.unset,
        script: typing.Union[MetaOapg.properties.script, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        reference: typing.Union[MetaOapg.properties.reference, str, schemas.Unset] = schemas.unset,
        metadata: typing.Union['Metadata', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'PostTransaction':
        return super().__new__(
            cls,
            *_args,
            timestamp=timestamp,
            postings=postings,
            script=script,
            reference=reference,
            metadata=metadata,
            _configuration=_configuration,
            **kwargs,
        )

from ledgerclient.model.metadata import Metadata
from ledgerclient.model.posting import Posting
