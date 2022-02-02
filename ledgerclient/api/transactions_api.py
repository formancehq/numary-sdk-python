"""
    Ledger API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0
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
from ledgerclient.model.create_transaction_response import CreateTransactionResponse
from ledgerclient.model.error_response import ErrorResponse
from ledgerclient.model.metadata import Metadata
from ledgerclient.model.transaction_commit_error_response import TransactionCommitErrorResponse
from ledgerclient.model.transaction_cursor_response import TransactionCursorResponse
from ledgerclient.model.transaction_data import TransactionData
from ledgerclient.model.transaction_list_response import TransactionListResponse
from ledgerclient.model.transaction_response import TransactionResponse
from ledgerclient.model.transactions import Transactions


class TransactionsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.add_metadata_on_transaction_endpoint = _Endpoint(
            settings={
                'response_type': None,
                'auth': [
                    'basicAuth',
                    'cloudToken'
                ],
                'endpoint_path': '/{ledger}/transactions/{txid}/metadata',
                'operation_id': 'add_metadata_on_transaction',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'ledger',
                    'txid',
                    'metadata',
                ],
                'required': [
                    'ledger',
                    'txid',
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
                    'txid':
                        (int,),
                    'metadata':
                        (Metadata,),
                },
                'attribute_map': {
                    'ledger': 'ledger',
                    'txid': 'txid',
                },
                'location_map': {
                    'ledger': 'path',
                    'txid': 'path',
                    'metadata': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self.create_transaction_endpoint = _Endpoint(
            settings={
                'response_type': (CreateTransactionResponse,),
                'auth': [
                    'basicAuth',
                    'cloudToken'
                ],
                'endpoint_path': '/{ledger}/transactions',
                'operation_id': 'create_transaction',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'ledger',
                    'transaction_data',
                ],
                'required': [
                    'ledger',
                    'transaction_data',
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
                    'transaction_data':
                        (TransactionData,),
                },
                'attribute_map': {
                    'ledger': 'ledger',
                },
                'location_map': {
                    'ledger': 'path',
                    'transaction_data': 'body',
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
        self.create_transactions_endpoint = _Endpoint(
            settings={
                'response_type': (TransactionListResponse,),
                'auth': [
                    'basicAuth',
                    'cloudToken'
                ],
                'endpoint_path': '/{ledger}/transactions/batch',
                'operation_id': 'create_transactions',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'ledger',
                    'transactions',
                ],
                'required': [
                    'ledger',
                    'transactions',
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
                    'transactions':
                        (Transactions,),
                },
                'attribute_map': {
                    'ledger': 'ledger',
                },
                'location_map': {
                    'ledger': 'path',
                    'transactions': 'body',
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
        self.get_transaction_endpoint = _Endpoint(
            settings={
                'response_type': (TransactionResponse,),
                'auth': [
                    'basicAuth',
                    'cloudToken'
                ],
                'endpoint_path': '/{ledger}/transactions/{txid}',
                'operation_id': 'get_transaction',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'ledger',
                    'txid',
                ],
                'required': [
                    'ledger',
                    'txid',
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
                    'txid':
                        (int,),
                },
                'attribute_map': {
                    'ledger': 'ledger',
                    'txid': 'txid',
                },
                'location_map': {
                    'ledger': 'path',
                    'txid': 'path',
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
        self.list_transactions_endpoint = _Endpoint(
            settings={
                'response_type': (TransactionCursorResponse,),
                'auth': [
                    'basicAuth',
                    'cloudToken'
                ],
                'endpoint_path': '/{ledger}/transactions',
                'operation_id': 'list_transactions',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'ledger',
                    'after',
                    'reference',
                    'account',
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
                    'after':
                        (str,),
                    'reference':
                        (str,),
                    'account':
                        (str,),
                },
                'attribute_map': {
                    'ledger': 'ledger',
                    'after': 'after',
                    'reference': 'reference',
                    'account': 'account',
                },
                'location_map': {
                    'ledger': 'path',
                    'after': 'query',
                    'reference': 'query',
                    'account': 'query',
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
        self.revert_transaction_endpoint = _Endpoint(
            settings={
                'response_type': None,
                'auth': [
                    'basicAuth',
                    'cloudToken'
                ],
                'endpoint_path': '/{ledger}/transactions/{txid}/revert',
                'operation_id': 'revert_transaction',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'ledger',
                    'txid',
                ],
                'required': [
                    'ledger',
                    'txid',
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
                    'txid':
                        (int,),
                },
                'attribute_map': {
                    'ledger': 'ledger',
                    'txid': 'txid',
                },
                'location_map': {
                    'ledger': 'path',
                    'txid': 'path',
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

    def add_metadata_on_transaction(
        self,
        ledger,
        txid,
        **kwargs
    ):
        """Set Transaction Metadata  # noqa: E501

        Set a new metadata to a ledger transaction by transaction id  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.add_metadata_on_transaction(ledger, txid, async_req=True)
        >>> result = thread.get()

        Args:
            ledger (str): ledger
            txid (int): txid

        Keyword Args:
            metadata (Metadata): metadata. [optional]
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
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
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
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['ledger'] = \
            ledger
        kwargs['txid'] = \
            txid
        return self.add_metadata_on_transaction_endpoint.call_with_http_info(**kwargs)

    def create_transaction(
        self,
        ledger,
        transaction_data,
        **kwargs
    ):
        """Create Transaction  # noqa: E501

        Create a new ledger transaction Commit a new transaction to the ledger  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_transaction(ledger, transaction_data, async_req=True)
        >>> result = thread.get()

        Args:
            ledger (str): ledger
            transaction_data (TransactionData): transaction

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
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            CreateTransactionResponse
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
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['ledger'] = \
            ledger
        kwargs['transaction_data'] = \
            transaction_data
        return self.create_transaction_endpoint.call_with_http_info(**kwargs)

    def create_transactions(
        self,
        ledger,
        transactions,
        **kwargs
    ):
        """Create Transactions Batch  # noqa: E501

        Create a new ledger transactions batch Commit a batch of new transactions to the ledger  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_transactions(ledger, transactions, async_req=True)
        >>> result = thread.get()

        Args:
            ledger (str): ledger
            transactions (Transactions): transactions

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
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            TransactionListResponse
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
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['ledger'] = \
            ledger
        kwargs['transactions'] = \
            transactions
        return self.create_transactions_endpoint.call_with_http_info(**kwargs)

    def get_transaction(
        self,
        ledger,
        txid,
        **kwargs
    ):
        """Get Transaction  # noqa: E501

        Get transaction by transaction id  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_transaction(ledger, txid, async_req=True)
        >>> result = thread.get()

        Args:
            ledger (str): ledger
            txid (int): txid

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
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            TransactionResponse
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
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['ledger'] = \
            ledger
        kwargs['txid'] = \
            txid
        return self.get_transaction_endpoint.call_with_http_info(**kwargs)

    def list_transactions(
        self,
        ledger,
        **kwargs
    ):
        """Get all Transactions  # noqa: E501

        Get all ledger transactions  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_transactions(ledger, async_req=True)
        >>> result = thread.get()

        Args:
            ledger (str): ledger

        Keyword Args:
            after (str): pagination cursor, will return transactions after given txid (in descending order). [optional]
            reference (str): find transactions by reference field. [optional]
            account (str): find transactions with postings involving given account, either as source or destination. [optional]
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
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            TransactionCursorResponse
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
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['ledger'] = \
            ledger
        return self.list_transactions_endpoint.call_with_http_info(**kwargs)

    def revert_transaction(
        self,
        ledger,
        txid,
        **kwargs
    ):
        """Revert Transaction  # noqa: E501

        Revert a ledger transaction by transaction id  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.revert_transaction(ledger, txid, async_req=True)
        >>> result = thread.get()

        Args:
            ledger (str): ledger
            txid (int): txid

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
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
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
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['ledger'] = \
            ledger
        kwargs['txid'] = \
            txid
        return self.revert_transaction_endpoint.call_with_http_info(**kwargs)
