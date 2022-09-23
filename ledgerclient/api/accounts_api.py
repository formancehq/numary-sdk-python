"""
    Ledger API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1.8.0-rc.1
    Contact: support@numary.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from ledgerclient.api_client import ApiClient, Endpoint as _Endpoint
from ledgerclient.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from ledgerclient.model.get_account200_response import GetAccount200Response
from ledgerclient.model.get_account400_response import GetAccount400Response
from ledgerclient.model.list_accounts200_response import ListAccounts200Response
from ledgerclient.model.list_accounts400_response import ListAccounts400Response
from ledgerclient.model.metadata import Metadata


class AccountsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.add_metadata_to_account_endpoint = _Endpoint(
            settings={
                'response_type': None,
                'auth': [
                    'basicAuth'
                ],
                'endpoint_path': '/{ledger}/accounts/{address}/metadata',
                'operation_id': 'add_metadata_to_account',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'ledger',
                    'address',
                    'metadata',
                ],
                'required': [
                    'ledger',
                    'address',
                    'metadata',
                ],
                'nullable': [
                    'metadata',
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'ledger':
                        (str,),
                    'address':
                        (str,),
                    'metadata':
                        (Metadata,),
                },
                'attribute_map': {
                    'ledger': 'ledger',
                    'address': 'address',
                },
                'location_map': {
                    'ledger': 'path',
                    'address': 'path',
                    'metadata': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self.count_accounts_endpoint = _Endpoint(
            settings={
                'response_type': None,
                'auth': [
                    'basicAuth'
                ],
                'endpoint_path': '/{ledger}/accounts',
                'operation_id': 'count_accounts',
                'http_method': 'HEAD',
                'servers': None,
            },
            params_map={
                'all': [
                    'ledger',
                    'address',
                    'metadata',
                ],
                'required': [
                    'ledger',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'ledger':
                        (str,),
                    'address':
                        (str,),
                    'metadata':
                        ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},),
                },
                'attribute_map': {
                    'ledger': 'ledger',
                    'address': 'address',
                    'metadata': 'metadata',
                },
                'location_map': {
                    'ledger': 'path',
                    'address': 'query',
                    'metadata': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [],
                'content_type': [],
            },
            api_client=api_client
        )
        self.get_account_endpoint = _Endpoint(
            settings={
                'response_type': (GetAccount200Response,),
                'auth': [
                    'basicAuth'
                ],
                'endpoint_path': '/{ledger}/accounts/{address}',
                'operation_id': 'get_account',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'ledger',
                    'address',
                ],
                'required': [
                    'ledger',
                    'address',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'ledger':
                        (str,),
                    'address':
                        (str,),
                },
                'attribute_map': {
                    'ledger': 'ledger',
                    'address': 'address',
                },
                'location_map': {
                    'ledger': 'path',
                    'address': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.list_accounts_endpoint = _Endpoint(
            settings={
                'response_type': (ListAccounts200Response,),
                'auth': [
                    'basicAuth'
                ],
                'endpoint_path': '/{ledger}/accounts',
                'operation_id': 'list_accounts',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'ledger',
                    'page_size',
                    'after',
                    'address',
                    'metadata',
                    'balance',
                    'balance_operator',
                    'pagination_token',
                ],
                'required': [
                    'ledger',
                ],
                'nullable': [
                ],
                'enum': [
                    'balance_operator',
                ],
                'validation': [
                    'page_size',
                ]
            },
            root_map={
                'validations': {
                    ('page_size',): {

                        'inclusive_maximum': 1000,
                        'inclusive_minimum': 1,
                    },
                },
                'allowed_values': {
                    ('balance_operator',): {

                        "GTE": "gte",
                        "LTE": "lte",
                        "GT": "gt",
                        "LT": "lt",
                        "E": "e"
                    },
                },
                'openapi_types': {
                    'ledger':
                        (str,),
                    'page_size':
                        (int,),
                    'after':
                        (str,),
                    'address':
                        (str,),
                    'metadata':
                        ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},),
                    'balance':
                        (int,),
                    'balance_operator':
                        (str,),
                    'pagination_token':
                        (str,),
                },
                'attribute_map': {
                    'ledger': 'ledger',
                    'page_size': 'page_size',
                    'after': 'after',
                    'address': 'address',
                    'metadata': 'metadata',
                    'balance': 'balance',
                    'balance_operator': 'balance_operator',
                    'pagination_token': 'pagination_token',
                },
                'location_map': {
                    'ledger': 'path',
                    'page_size': 'query',
                    'after': 'query',
                    'address': 'query',
                    'metadata': 'query',
                    'balance': 'query',
                    'balance_operator': 'query',
                    'pagination_token': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )

    def add_metadata_to_account(
        self,
        ledger,
        address,
        metadata,
        **kwargs
    ):
        """Add metadata to an account.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.add_metadata_to_account(ledger, address, metadata, async_req=True)
        >>> result = thread.get()

        Args:
            ledger (str): Name of the ledger.
            address (str): Exact address of the account. It must match the following regular expressions pattern: ``` ^\\w+(:\\w+)*$ ``` 
            metadata (Metadata): metadata

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            None
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['ledger'] = \
            ledger
        kwargs['address'] = \
            address
        kwargs['metadata'] = \
            metadata
        return self.add_metadata_to_account_endpoint.call_with_http_info(**kwargs)

    def count_accounts(
        self,
        ledger,
        **kwargs
    ):
        """Count the accounts from a ledger.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.count_accounts(ledger, async_req=True)
        >>> result = thread.get()

        Args:
            ledger (str): Name of the ledger.

        Keyword Args:
            address (str): Filter accounts by address pattern (regular expression placed between ^ and $).. [optional]
            metadata ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}): Filter accounts by metadata key value pairs. Nested objects can be used as seen in the example below.. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            None
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['ledger'] = \
            ledger
        return self.count_accounts_endpoint.call_with_http_info(**kwargs)

    def get_account(
        self,
        ledger,
        address,
        **kwargs
    ):
        """Get account by its address.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_account(ledger, address, async_req=True)
        >>> result = thread.get()

        Args:
            ledger (str): Name of the ledger.
            address (str): Exact address of the account. It must match the following regular expressions pattern: ``` ^\\w+(:\\w+)*$ ``` 

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            GetAccount200Response
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['ledger'] = \
            ledger
        kwargs['address'] = \
            address
        return self.get_account_endpoint.call_with_http_info(**kwargs)

    def list_accounts(
        self,
        ledger,
        **kwargs
    ):
        """List accounts from a ledger.  # noqa: E501

        List accounts from a ledger, sorted by address in descending order.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_accounts(ledger, async_req=True)
        >>> result = thread.get()

        Args:
            ledger (str): Name of the ledger.

        Keyword Args:
            page_size (int): The maximum number of results to return per page. [optional] if omitted the server will use the default value of 15
            after (str): Pagination cursor, will return accounts after given address, in descending order.. [optional]
            address (str): Filter accounts by address pattern (regular expression placed between ^ and $).. [optional]
            metadata ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}): Filter accounts by metadata key value pairs. Nested objects can be used as seen in the example below.. [optional]
            balance (int): Filter accounts by their balance (default operator is gte). [optional]
            balance_operator (str): Operator used for the filtering of balances can be greater than/equal, less than/equal, greater than, less than, or equal. [optional]
            pagination_token (str): Parameter used in pagination requests. Maximum page size is set to 15. Set to the value of next for the next page of results.  Set to the value of previous for the previous page of results. No other parameters can be set when the pagination token is set. . [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            ListAccounts200Response
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['ledger'] = \
            ledger
        return self.list_accounts_endpoint.call_with_http_info(**kwargs)

