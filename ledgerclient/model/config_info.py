# coding: utf-8

"""
    Ledger API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1.10.13
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


class ConfigInfo(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "server",
            "config",
            "version",
        }
        
        class properties:
        
            @staticmethod
            def config() -> typing.Type['Config']:
                return Config
            server = schemas.StrSchema
            version = schemas.StrSchema
            __annotations__ = {
                "config": config,
                "server": server,
                "version": version,
            }
    
    server: MetaOapg.properties.server
    config: 'Config'
    version: MetaOapg.properties.version
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["config"]) -> 'Config': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["server"]) -> MetaOapg.properties.server: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["version"]) -> MetaOapg.properties.version: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["config", "server", "version", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["config"]) -> 'Config': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["server"]) -> MetaOapg.properties.server: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["version"]) -> MetaOapg.properties.version: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["config", "server", "version", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        server: typing.Union[MetaOapg.properties.server, str, ],
        config: 'Config',
        version: typing.Union[MetaOapg.properties.version, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ConfigInfo':
        return super().__new__(
            cls,
            *_args,
            server=server,
            config=config,
            version=version,
            _configuration=_configuration,
            **kwargs,
        )

from ledgerclient.model.config import Config
