# coding: utf-8

"""
    Ledger API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1.10.12
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


class Transaction(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "postings",
            "txid",
            "timestamp",
        }
        
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
            
            
            class txid(
                schemas.Int64Schema
            ):
                pass
            reference = schemas.StrSchema
        
            @staticmethod
            def metadata() -> typing.Type['Metadata']:
                return Metadata
        
            @staticmethod
            def preCommitVolumes() -> typing.Type['AggregatedVolumes']:
                return AggregatedVolumes
        
            @staticmethod
            def postCommitVolumes() -> typing.Type['AggregatedVolumes']:
                return AggregatedVolumes
            __annotations__ = {
                "timestamp": timestamp,
                "postings": postings,
                "txid": txid,
                "reference": reference,
                "metadata": metadata,
                "preCommitVolumes": preCommitVolumes,
                "postCommitVolumes": postCommitVolumes,
            }
    
    postings: MetaOapg.properties.postings
    txid: MetaOapg.properties.txid
    timestamp: MetaOapg.properties.timestamp
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["timestamp"]) -> MetaOapg.properties.timestamp: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["postings"]) -> MetaOapg.properties.postings: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["txid"]) -> MetaOapg.properties.txid: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["reference"]) -> MetaOapg.properties.reference: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["metadata"]) -> 'Metadata': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["preCommitVolumes"]) -> 'AggregatedVolumes': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["postCommitVolumes"]) -> 'AggregatedVolumes': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["timestamp", "postings", "txid", "reference", "metadata", "preCommitVolumes", "postCommitVolumes", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["timestamp"]) -> MetaOapg.properties.timestamp: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["postings"]) -> MetaOapg.properties.postings: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["txid"]) -> MetaOapg.properties.txid: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["reference"]) -> typing.Union[MetaOapg.properties.reference, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["metadata"]) -> typing.Union['Metadata', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["preCommitVolumes"]) -> typing.Union['AggregatedVolumes', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["postCommitVolumes"]) -> typing.Union['AggregatedVolumes', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["timestamp", "postings", "txid", "reference", "metadata", "preCommitVolumes", "postCommitVolumes", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        postings: typing.Union[MetaOapg.properties.postings, list, tuple, ],
        txid: typing.Union[MetaOapg.properties.txid, decimal.Decimal, int, ],
        timestamp: typing.Union[MetaOapg.properties.timestamp, str, datetime, ],
        reference: typing.Union[MetaOapg.properties.reference, str, schemas.Unset] = schemas.unset,
        metadata: typing.Union['Metadata', schemas.Unset] = schemas.unset,
        preCommitVolumes: typing.Union['AggregatedVolumes', schemas.Unset] = schemas.unset,
        postCommitVolumes: typing.Union['AggregatedVolumes', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Transaction':
        return super().__new__(
            cls,
            *_args,
            postings=postings,
            txid=txid,
            timestamp=timestamp,
            reference=reference,
            metadata=metadata,
            preCommitVolumes=preCommitVolumes,
            postCommitVolumes=postCommitVolumes,
            _configuration=_configuration,
            **kwargs,
        )

from ledgerclient.model.aggregated_volumes import AggregatedVolumes
from ledgerclient.model.metadata import Metadata
from ledgerclient.model.posting import Posting
