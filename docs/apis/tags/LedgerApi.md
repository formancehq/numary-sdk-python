<a name="__pageTop"></a>
# ledgerclient.apis.tags.ledger_api.LedgerApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_metadata_on_transaction**](#add_metadata_on_transaction) | **post** /{ledger}/transactions/{txid}/metadata | Set the metadata of a transaction by its ID
[**add_metadata_to_account**](#add_metadata_to_account) | **post** /{ledger}/accounts/{address}/metadata | Add metadata to an account
[**count_accounts**](#count_accounts) | **head** /{ledger}/accounts | Count the accounts from a ledger
[**count_transactions**](#count_transactions) | **head** /{ledger}/transactions | Count the transactions from a ledger
[**create_transaction**](#create_transaction) | **post** /{ledger}/transactions | Create a new transaction to a ledger
[**create_transactions**](#create_transactions) | **post** /{ledger}/transactions/batch | Create a new batch of transactions to a ledger
[**get_account**](#get_account) | **get** /{ledger}/accounts/{address} | Get account by its address
[**get_balances**](#get_balances) | **get** /{ledger}/balances | Get the balances from a ledger&#x27;s account
[**get_balances_aggregated**](#get_balances_aggregated) | **get** /{ledger}/aggregate/balances | Get the aggregated balances from selected accounts
[**get_info**](#get_info) | **get** /_info | Show server information
[**get_ledger_info**](#get_ledger_info) | **get** /{ledger}/_info | Get information about a ledger
[**get_mapping**](#get_mapping) | **get** /{ledger}/mapping | Get the mapping of a ledger
[**get_transaction**](#get_transaction) | **get** /{ledger}/transactions/{txid} | Get transaction from a ledger by its ID
[**list_accounts**](#list_accounts) | **get** /{ledger}/accounts | List accounts from a ledger
[**list_logs**](#list_logs) | **get** /{ledger}/logs | List the logs from a ledger
[**list_transactions**](#list_transactions) | **get** /{ledger}/transactions | List transactions from a ledger
[**read_stats**](#read_stats) | **get** /{ledger}/stats | Get statistics from a ledger
[**revert_transaction**](#revert_transaction) | **post** /{ledger}/transactions/{txid}/revert | Revert a ledger transaction by its ID
[**run_script**](#run_script) | **post** /{ledger}/script | Execute a Numscript
[**update_mapping**](#update_mapping) | **put** /{ledger}/mapping | Update the mapping of a ledger

# **add_metadata_on_transaction**
<a name="add_metadata_on_transaction"></a>
> add_metadata_on_transaction(ledgertxid)

Set the metadata of a transaction by its ID

### Example

```python
import ledgerclient
from ledgerclient.apis.tags import ledger_api
from ledgerclient.model.error_response import ErrorResponse
from ledgerclient.model.metadata import Metadata
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ledgerclient.Configuration(
    host = "http://localhost"
)

# Enter a context with an instance of the API client
with ledgerclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ledger_api.LedgerApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'ledger': "ledger001",
        'txid': 1234,
    }
    try:
        # Set the metadata of a transaction by its ID
        api_response = api_instance.add_metadata_on_transaction(
            path_params=path_params,
        )
    except ledgerclient.ApiException as e:
        print("Exception when calling LedgerApi->add_metadata_on_transaction: %s\n" % e)

    # example passing only optional values
    path_params = {
        'ledger': "ledger001",
        'txid': 1234,
    }
    body = Metadata(
        key=None,
    )
    try:
        # Set the metadata of a transaction by its ID
        api_response = api_instance.add_metadata_on_transaction(
            path_params=path_params,
            body=body,
        )
    except ledgerclient.ApiException as e:
        print("Exception when calling LedgerApi->add_metadata_on_transaction: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Metadata**](../../models/Metadata.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
ledger | LedgerSchema | | 
txid | TxidSchema | | 

# LedgerSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# TxidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#add_metadata_on_transaction.ApiResponseFor204) | No Content
default | [ApiResponseForDefault](#add_metadata_on_transaction.ApiResponseForDefault) | Error

#### add_metadata_on_transaction.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### add_metadata_on_transaction.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **add_metadata_to_account**
<a name="add_metadata_to_account"></a>
> add_metadata_to_account(ledgeraddressmetadata)

Add metadata to an account

### Example

```python
import ledgerclient
from ledgerclient.apis.tags import ledger_api
from ledgerclient.model.error_response import ErrorResponse
from ledgerclient.model.metadata import Metadata
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ledgerclient.Configuration(
    host = "http://localhost"
)

# Enter a context with an instance of the API client
with ledgerclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ledger_api.LedgerApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'ledger': "ledger001",
        'address': "users:001",
    }
    body = Metadata(
        key=None,
    )
    try:
        # Add metadata to an account
        api_response = api_instance.add_metadata_to_account(
            path_params=path_params,
            body=body,
        )
    except ledgerclient.ApiException as e:
        print("Exception when calling LedgerApi->add_metadata_to_account: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Metadata**](../../models/Metadata.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
ledger | LedgerSchema | | 
address | AddressSchema | | 

# LedgerSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# AddressSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#add_metadata_to_account.ApiResponseFor204) | No Content
default | [ApiResponseForDefault](#add_metadata_to_account.ApiResponseForDefault) | Error

#### add_metadata_to_account.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### add_metadata_to_account.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **count_accounts**
<a name="count_accounts"></a>
> count_accounts(ledger)

Count the accounts from a ledger

### Example

```python
import ledgerclient
from ledgerclient.apis.tags import ledger_api
from ledgerclient.model.error_response import ErrorResponse
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ledgerclient.Configuration(
    host = "http://localhost"
)

# Enter a context with an instance of the API client
with ledgerclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ledger_api.LedgerApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'ledger': "ledger001",
    }
    query_params = {
    }
    try:
        # Count the accounts from a ledger
        api_response = api_instance.count_accounts(
            path_params=path_params,
            query_params=query_params,
        )
    except ledgerclient.ApiException as e:
        print("Exception when calling LedgerApi->count_accounts: %s\n" % e)

    # example passing only optional values
    path_params = {
        'ledger': "ledger001",
    }
    query_params = {
        'address': "users:.+",
        'metadata': dict(),
    }
    try:
        # Count the accounts from a ledger
        api_response = api_instance.count_accounts(
            path_params=path_params,
            query_params=query_params,
        )
    except ledgerclient.ApiException as e:
        print("Exception when calling LedgerApi->count_accounts: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
address | AddressSchema | | optional
metadata | MetadataSchema | | optional


# AddressSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# MetadataSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
ledger | LedgerSchema | | 

# LedgerSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#count_accounts.ApiResponseFor200) | OK
default | [ApiResponseForDefault](#count_accounts.ApiResponseForDefault) | Error

#### count_accounts.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | ResponseHeadersFor200 |  |
#### ResponseHeadersFor200

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
Count | CountSchema | | optional

# CountSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer


#### count_accounts.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **count_transactions**
<a name="count_transactions"></a>
> count_transactions(ledger)

Count the transactions from a ledger

### Example

```python
import ledgerclient
from ledgerclient.apis.tags import ledger_api
from ledgerclient.model.error_response import ErrorResponse
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ledgerclient.Configuration(
    host = "http://localhost"
)

# Enter a context with an instance of the API client
with ledgerclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ledger_api.LedgerApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'ledger': "ledger001",
    }
    query_params = {
    }
    try:
        # Count the transactions from a ledger
        api_response = api_instance.count_transactions(
            path_params=path_params,
            query_params=query_params,
        )
    except ledgerclient.ApiException as e:
        print("Exception when calling LedgerApi->count_transactions: %s\n" % e)

    # example passing only optional values
    path_params = {
        'ledger': "ledger001",
    }
    query_params = {
        'reference': "ref:001",
        'account': "users:001",
        'source': "users:001",
        'destination': "users:001",
        'startTime': "1970-01-01T00:00:00.00Z",
        'start_time': "1970-01-01T00:00:00.00Z",
        'endTime': "1970-01-01T00:00:00.00Z",
        'end_time': "1970-01-01T00:00:00.00Z",
        'metadata': dict(),
    }
    try:
        # Count the transactions from a ledger
        api_response = api_instance.count_transactions(
            path_params=path_params,
            query_params=query_params,
        )
    except ledgerclient.ApiException as e:
        print("Exception when calling LedgerApi->count_transactions: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
reference | ReferenceSchema | | optional
account | AccountSchema | | optional
source | SourceSchema | | optional
destination | DestinationSchema | | optional
startTime | StartTimeSchema | | optional
start_time | StartTimeSchema | | optional
endTime | EndTimeSchema | | optional
end_time | EndTimeSchema | | optional
metadata | MetadataSchema | | optional


# ReferenceSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# AccountSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# SourceSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# DestinationSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# StartTimeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, datetime,  | str,  |  | value must conform to RFC-3339 date-time

# StartTimeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, datetime,  | str,  |  | value must conform to RFC-3339 date-time

# EndTimeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, datetime,  | str,  |  | value must conform to RFC-3339 date-time

# EndTimeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, datetime,  | str,  |  | value must conform to RFC-3339 date-time

# MetadataSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
ledger | LedgerSchema | | 

# LedgerSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#count_transactions.ApiResponseFor200) | OK
default | [ApiResponseForDefault](#count_transactions.ApiResponseForDefault) | Error

#### count_transactions.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | ResponseHeadersFor200 |  |
#### ResponseHeadersFor200

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
Count | CountSchema | | optional

# CountSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer


#### count_transactions.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **create_transaction**
<a name="create_transaction"></a>
> TransactionsResponse create_transaction(ledgerpost_transaction)

Create a new transaction to a ledger

### Example

```python
import ledgerclient
from ledgerclient.apis.tags import ledger_api
from ledgerclient.model.error_response import ErrorResponse
from ledgerclient.model.post_transaction import PostTransaction
from ledgerclient.model.transactions_response import TransactionsResponse
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ledgerclient.Configuration(
    host = "http://localhost"
)

# Enter a context with an instance of the API client
with ledgerclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ledger_api.LedgerApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'ledger': "ledger001",
    }
    query_params = {
    }
    body = PostTransaction(
        timestamp="1970-01-01T00:00:00.00Z",
        postings=[
            Posting(
                amount=100,
                asset="COIN",
                destination="users:002",
                source="users:001",
            )
        ],
        script=dict(
            plain="vars {\naccount $user\n}\nsend [COIN 10] (\n\tsource = @world\n\tdestination = $user\n)\n",
            vars=dict(),
        ),
        reference="ref:001",
        metadata=Metadata(
            key=None,
        ),
    )
    try:
        # Create a new transaction to a ledger
        api_response = api_instance.create_transaction(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except ledgerclient.ApiException as e:
        print("Exception when calling LedgerApi->create_transaction: %s\n" % e)

    # example passing only optional values
    path_params = {
        'ledger': "ledger001",
    }
    query_params = {
        'preview': True,
    }
    body = PostTransaction(
        timestamp="1970-01-01T00:00:00.00Z",
        postings=[
            Posting(
                amount=100,
                asset="COIN",
                destination="users:002",
                source="users:001",
            )
        ],
        script=dict(
            plain="vars {\naccount $user\n}\nsend [COIN 10] (\n\tsource = @world\n\tdestination = $user\n)\n",
            vars=dict(),
        ),
        reference="ref:001",
        metadata=Metadata(
            key=None,
        ),
    )
    try:
        # Create a new transaction to a ledger
        api_response = api_instance.create_transaction(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except ledgerclient.ApiException as e:
        print("Exception when calling LedgerApi->create_transaction: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**PostTransaction**](../../models/PostTransaction.md) |  | 


### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
preview | PreviewSchema | | optional


# PreviewSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
ledger | LedgerSchema | | 

# LedgerSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#create_transaction.ApiResponseFor200) | OK
default | [ApiResponseForDefault](#create_transaction.ApiResponseForDefault) | Error

#### create_transaction.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**TransactionsResponse**](../../models/TransactionsResponse.md) |  | 


#### create_transaction.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **create_transactions**
<a name="create_transactions"></a>
> TransactionsResponse create_transactions(ledgertransactions)

Create a new batch of transactions to a ledger

### Example

```python
import ledgerclient
from ledgerclient.apis.tags import ledger_api
from ledgerclient.model.error_response import ErrorResponse
from ledgerclient.model.transactions import Transactions
from ledgerclient.model.transactions_response import TransactionsResponse
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ledgerclient.Configuration(
    host = "http://localhost"
)

# Enter a context with an instance of the API client
with ledgerclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ledger_api.LedgerApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'ledger': "ledger001",
    }
    body = Transactions(
        transactions=[
            TransactionData(
                postings=[
                    Posting(
                        amount=100,
                        asset="COIN",
                        destination="users:002",
                        source="users:001",
                    )
                ],
                reference="ref:001",
                metadata=Metadata(
                    key=None,
                ),
                timestamp="1970-01-01T00:00:00.00Z",
            )
        ],
    )
    try:
        # Create a new batch of transactions to a ledger
        api_response = api_instance.create_transactions(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except ledgerclient.ApiException as e:
        print("Exception when calling LedgerApi->create_transactions: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Transactions**](../../models/Transactions.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
ledger | LedgerSchema | | 

# LedgerSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#create_transactions.ApiResponseFor200) | OK
default | [ApiResponseForDefault](#create_transactions.ApiResponseForDefault) | Error

#### create_transactions.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**TransactionsResponse**](../../models/TransactionsResponse.md) |  | 


#### create_transactions.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_account**
<a name="get_account"></a>
> AccountResponse get_account(ledgeraddress)

Get account by its address

### Example

```python
import ledgerclient
from ledgerclient.apis.tags import ledger_api
from ledgerclient.model.error_response import ErrorResponse
from ledgerclient.model.account_response import AccountResponse
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ledgerclient.Configuration(
    host = "http://localhost"
)

# Enter a context with an instance of the API client
with ledgerclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ledger_api.LedgerApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'ledger': "ledger001",
        'address': "users:001",
    }
    try:
        # Get account by its address
        api_response = api_instance.get_account(
            path_params=path_params,
        )
        pprint(api_response)
    except ledgerclient.ApiException as e:
        print("Exception when calling LedgerApi->get_account: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
ledger | LedgerSchema | | 
address | AddressSchema | | 

# LedgerSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# AddressSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_account.ApiResponseFor200) | OK
default | [ApiResponseForDefault](#get_account.ApiResponseForDefault) | Error

#### get_account.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AccountResponse**](../../models/AccountResponse.md) |  | 


#### get_account.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_balances**
<a name="get_balances"></a>
> BalancesCursorResponse get_balances(ledger)

Get the balances from a ledger's account

### Example

```python
import ledgerclient
from ledgerclient.apis.tags import ledger_api
from ledgerclient.model.error_response import ErrorResponse
from ledgerclient.model.balances_cursor_response import BalancesCursorResponse
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ledgerclient.Configuration(
    host = "http://localhost"
)

# Enter a context with an instance of the API client
with ledgerclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ledger_api.LedgerApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'ledger': "ledger001",
    }
    query_params = {
    }
    try:
        # Get the balances from a ledger's account
        api_response = api_instance.get_balances(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except ledgerclient.ApiException as e:
        print("Exception when calling LedgerApi->get_balances: %s\n" % e)

    # example passing only optional values
    path_params = {
        'ledger': "ledger001",
    }
    query_params = {
        'address': "users:001",
        'after': "users:003",
        'cursor': "aHR0cHM6Ly9nLnBhZ2UvTmVrby1SYW1lbj9zaGFyZQ==",
        'pagination_token': "aHR0cHM6Ly9nLnBhZ2UvTmVrby1SYW1lbj9zaGFyZQ==",
    }
    try:
        # Get the balances from a ledger's account
        api_response = api_instance.get_balances(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except ledgerclient.ApiException as e:
        print("Exception when calling LedgerApi->get_balances: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
address | AddressSchema | | optional
after | AfterSchema | | optional
cursor | CursorSchema | | optional
pagination_token | PaginationTokenSchema | | optional


# AddressSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# AfterSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# CursorSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# PaginationTokenSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
ledger | LedgerSchema | | 

# LedgerSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_balances.ApiResponseFor200) | OK
default | [ApiResponseForDefault](#get_balances.ApiResponseForDefault) | Error

#### get_balances.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BalancesCursorResponse**](../../models/BalancesCursorResponse.md) |  | 


#### get_balances.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_balances_aggregated**
<a name="get_balances_aggregated"></a>
> AggregateBalancesResponse get_balances_aggregated(ledger)

Get the aggregated balances from selected accounts

### Example

```python
import ledgerclient
from ledgerclient.apis.tags import ledger_api
from ledgerclient.model.error_response import ErrorResponse
from ledgerclient.model.aggregate_balances_response import AggregateBalancesResponse
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ledgerclient.Configuration(
    host = "http://localhost"
)

# Enter a context with an instance of the API client
with ledgerclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ledger_api.LedgerApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'ledger': "ledger001",
    }
    query_params = {
    }
    try:
        # Get the aggregated balances from selected accounts
        api_response = api_instance.get_balances_aggregated(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except ledgerclient.ApiException as e:
        print("Exception when calling LedgerApi->get_balances_aggregated: %s\n" % e)

    # example passing only optional values
    path_params = {
        'ledger': "ledger001",
    }
    query_params = {
        'address': "users:001",
    }
    try:
        # Get the aggregated balances from selected accounts
        api_response = api_instance.get_balances_aggregated(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except ledgerclient.ApiException as e:
        print("Exception when calling LedgerApi->get_balances_aggregated: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
address | AddressSchema | | optional


# AddressSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
ledger | LedgerSchema | | 

# LedgerSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_balances_aggregated.ApiResponseFor200) | OK
default | [ApiResponseForDefault](#get_balances_aggregated.ApiResponseForDefault) | Error

#### get_balances_aggregated.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AggregateBalancesResponse**](../../models/AggregateBalancesResponse.md) |  | 


#### get_balances_aggregated.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_info**
<a name="get_info"></a>
> ConfigInfoResponse get_info()

Show server information

### Example

```python
import ledgerclient
from ledgerclient.apis.tags import ledger_api
from ledgerclient.model.error_response import ErrorResponse
from ledgerclient.model.config_info_response import ConfigInfoResponse
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ledgerclient.Configuration(
    host = "http://localhost"
)

# Enter a context with an instance of the API client
with ledgerclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ledger_api.LedgerApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Show server information
        api_response = api_instance.get_info()
        pprint(api_response)
    except ledgerclient.ApiException as e:
        print("Exception when calling LedgerApi->get_info: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_info.ApiResponseFor200) | OK
default | [ApiResponseForDefault](#get_info.ApiResponseForDefault) | Error

#### get_info.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ConfigInfoResponse**](../../models/ConfigInfoResponse.md) |  | 


#### get_info.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_ledger_info**
<a name="get_ledger_info"></a>
> LedgerInfoResponse get_ledger_info(ledger)

Get information about a ledger

### Example

```python
import ledgerclient
from ledgerclient.apis.tags import ledger_api
from ledgerclient.model.error_response import ErrorResponse
from ledgerclient.model.ledger_info_response import LedgerInfoResponse
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ledgerclient.Configuration(
    host = "http://localhost"
)

# Enter a context with an instance of the API client
with ledgerclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ledger_api.LedgerApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'ledger': "ledger001",
    }
    try:
        # Get information about a ledger
        api_response = api_instance.get_ledger_info(
            path_params=path_params,
        )
        pprint(api_response)
    except ledgerclient.ApiException as e:
        print("Exception when calling LedgerApi->get_ledger_info: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
ledger | LedgerSchema | | 

# LedgerSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_ledger_info.ApiResponseFor200) | OK
default | [ApiResponseForDefault](#get_ledger_info.ApiResponseForDefault) | Error

#### get_ledger_info.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**LedgerInfoResponse**](../../models/LedgerInfoResponse.md) |  | 


#### get_ledger_info.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_mapping**
<a name="get_mapping"></a>
> MappingResponse get_mapping(ledger)

Get the mapping of a ledger

### Example

```python
import ledgerclient
from ledgerclient.apis.tags import ledger_api
from ledgerclient.model.error_response import ErrorResponse
from ledgerclient.model.mapping_response import MappingResponse
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ledgerclient.Configuration(
    host = "http://localhost"
)

# Enter a context with an instance of the API client
with ledgerclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ledger_api.LedgerApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'ledger': "ledger001",
    }
    try:
        # Get the mapping of a ledger
        api_response = api_instance.get_mapping(
            path_params=path_params,
        )
        pprint(api_response)
    except ledgerclient.ApiException as e:
        print("Exception when calling LedgerApi->get_mapping: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
ledger | LedgerSchema | | 

# LedgerSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_mapping.ApiResponseFor200) | OK
default | [ApiResponseForDefault](#get_mapping.ApiResponseForDefault) | Error

#### get_mapping.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**MappingResponse**](../../models/MappingResponse.md) |  | 


#### get_mapping.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_transaction**
<a name="get_transaction"></a>
> TransactionResponse get_transaction(ledgertxid)

Get transaction from a ledger by its ID

### Example

```python
import ledgerclient
from ledgerclient.apis.tags import ledger_api
from ledgerclient.model.error_response import ErrorResponse
from ledgerclient.model.transaction_response import TransactionResponse
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ledgerclient.Configuration(
    host = "http://localhost"
)

# Enter a context with an instance of the API client
with ledgerclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ledger_api.LedgerApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'ledger': "ledger001",
        'txid': 1234,
    }
    try:
        # Get transaction from a ledger by its ID
        api_response = api_instance.get_transaction(
            path_params=path_params,
        )
        pprint(api_response)
    except ledgerclient.ApiException as e:
        print("Exception when calling LedgerApi->get_transaction: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
ledger | LedgerSchema | | 
txid | TxidSchema | | 

# LedgerSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# TxidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_transaction.ApiResponseFor200) | OK
default | [ApiResponseForDefault](#get_transaction.ApiResponseForDefault) | Error

#### get_transaction.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**TransactionResponse**](../../models/TransactionResponse.md) |  | 


#### get_transaction.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **list_accounts**
<a name="list_accounts"></a>
> AccountsCursorResponse list_accounts(ledger)

List accounts from a ledger

List accounts from a ledger, sorted by address in descending order.

### Example

```python
import ledgerclient
from ledgerclient.apis.tags import ledger_api
from ledgerclient.model.error_response import ErrorResponse
from ledgerclient.model.accounts_cursor_response import AccountsCursorResponse
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ledgerclient.Configuration(
    host = "http://localhost"
)

# Enter a context with an instance of the API client
with ledgerclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ledger_api.LedgerApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'ledger': "ledger001",
    }
    query_params = {
    }
    try:
        # List accounts from a ledger
        api_response = api_instance.list_accounts(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except ledgerclient.ApiException as e:
        print("Exception when calling LedgerApi->list_accounts: %s\n" % e)

    # example passing only optional values
    path_params = {
        'ledger': "ledger001",
    }
    query_params = {
        'pageSize': 100,
        'page_size': 100,
        'after': "users:003",
        'address': "users:.+",
        'metadata': dict(),
        'balance': 2400,
        'balanceOperator': "gte",
        'balance_operator': "gte",
        'cursor': "aHR0cHM6Ly9nLnBhZ2UvTmVrby1SYW1lbj9zaGFyZQ==",
        'pagination_token': "aHR0cHM6Ly9nLnBhZ2UvTmVrby1SYW1lbj9zaGFyZQ==",
    }
    try:
        # List accounts from a ledger
        api_response = api_instance.list_accounts(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except ledgerclient.ApiException as e:
        print("Exception when calling LedgerApi->list_accounts: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
pageSize | PageSizeSchema | | optional
page_size | PageSizeSchema | | optional
after | AfterSchema | | optional
address | AddressSchema | | optional
metadata | MetadataSchema | | optional
balance | BalanceSchema | | optional
balanceOperator | BalanceOperatorSchema | | optional
balance_operator | BalanceOperatorSchema | | optional
cursor | CursorSchema | | optional
pagination_token | PaginationTokenSchema | | optional


# PageSizeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | if omitted the server will use the default value of 15value must be a 64 bit integer

# PageSizeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | if omitted the server will use the default value of 15value must be a 64 bit integer

# AfterSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# AddressSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# MetadataSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# BalanceSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer

# BalanceOperatorSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | must be one of ["gte", "lte", "gt", "lt", "e", "ne", ] 

# BalanceOperatorSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | must be one of ["gte", "lte", "gt", "lt", "e", "ne", ] 

# CursorSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# PaginationTokenSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
ledger | LedgerSchema | | 

# LedgerSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#list_accounts.ApiResponseFor200) | OK
default | [ApiResponseForDefault](#list_accounts.ApiResponseForDefault) | Error

#### list_accounts.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AccountsCursorResponse**](../../models/AccountsCursorResponse.md) |  | 


#### list_accounts.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **list_logs**
<a name="list_logs"></a>
> LogsCursorResponse list_logs(ledger)

List the logs from a ledger

List the logs from a ledger, sorted by ID in descending order.

### Example

```python
import ledgerclient
from ledgerclient.apis.tags import ledger_api
from ledgerclient.model.error_response import ErrorResponse
from ledgerclient.model.logs_cursor_response import LogsCursorResponse
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ledgerclient.Configuration(
    host = "http://localhost"
)

# Enter a context with an instance of the API client
with ledgerclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ledger_api.LedgerApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'ledger': "ledger001",
    }
    query_params = {
    }
    try:
        # List the logs from a ledger
        api_response = api_instance.list_logs(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except ledgerclient.ApiException as e:
        print("Exception when calling LedgerApi->list_logs: %s\n" % e)

    # example passing only optional values
    path_params = {
        'ledger': "ledger001",
    }
    query_params = {
        'pageSize': 100,
        'page_size': 100,
        'after': "1234",
        'startTime': "1970-01-01T00:00:00.00Z",
        'start_time': "1970-01-01T00:00:00.00Z",
        'endTime': "1970-01-01T00:00:00.00Z",
        'end_time': "1970-01-01T00:00:00.00Z",
        'cursor': "aHR0cHM6Ly9nLnBhZ2UvTmVrby1SYW1lbj9zaGFyZQ==",
        'pagination_token': "aHR0cHM6Ly9nLnBhZ2UvTmVrby1SYW1lbj9zaGFyZQ==",
    }
    try:
        # List the logs from a ledger
        api_response = api_instance.list_logs(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except ledgerclient.ApiException as e:
        print("Exception when calling LedgerApi->list_logs: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
pageSize | PageSizeSchema | | optional
page_size | PageSizeSchema | | optional
after | AfterSchema | | optional
startTime | StartTimeSchema | | optional
start_time | StartTimeSchema | | optional
endTime | EndTimeSchema | | optional
end_time | EndTimeSchema | | optional
cursor | CursorSchema | | optional
pagination_token | PaginationTokenSchema | | optional


# PageSizeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | if omitted the server will use the default value of 15value must be a 64 bit integer

# PageSizeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | if omitted the server will use the default value of 15value must be a 64 bit integer

# AfterSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# StartTimeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, datetime,  | str,  |  | value must conform to RFC-3339 date-time

# StartTimeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, datetime,  | str,  |  | value must conform to RFC-3339 date-time

# EndTimeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, datetime,  | str,  |  | value must conform to RFC-3339 date-time

# EndTimeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, datetime,  | str,  |  | value must conform to RFC-3339 date-time

# CursorSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# PaginationTokenSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
ledger | LedgerSchema | | 

# LedgerSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#list_logs.ApiResponseFor200) | OK
default | [ApiResponseForDefault](#list_logs.ApiResponseForDefault) | Error

#### list_logs.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**LogsCursorResponse**](../../models/LogsCursorResponse.md) |  | 


#### list_logs.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **list_transactions**
<a name="list_transactions"></a>
> TransactionsCursorResponse list_transactions(ledger)

List transactions from a ledger

List transactions from a ledger, sorted by txid in descending order.

### Example

```python
import ledgerclient
from ledgerclient.apis.tags import ledger_api
from ledgerclient.model.error_response import ErrorResponse
from ledgerclient.model.transactions_cursor_response import TransactionsCursorResponse
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ledgerclient.Configuration(
    host = "http://localhost"
)

# Enter a context with an instance of the API client
with ledgerclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ledger_api.LedgerApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'ledger': "ledger001",
    }
    query_params = {
    }
    try:
        # List transactions from a ledger
        api_response = api_instance.list_transactions(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except ledgerclient.ApiException as e:
        print("Exception when calling LedgerApi->list_transactions: %s\n" % e)

    # example passing only optional values
    path_params = {
        'ledger': "ledger001",
    }
    query_params = {
        'pageSize': 100,
        'page_size': 100,
        'after': "1234",
        'reference': "ref:001",
        'account': "users:001",
        'source': "users:001",
        'destination': "users:001",
        'startTime': "1970-01-01T00:00:00.00Z",
        'start_time': "1970-01-01T00:00:00.00Z",
        'endTime': "1970-01-01T00:00:00.00Z",
        'end_time': "1970-01-01T00:00:00.00Z",
        'cursor': "aHR0cHM6Ly9nLnBhZ2UvTmVrby1SYW1lbj9zaGFyZQ==",
        'pagination_token': "aHR0cHM6Ly9nLnBhZ2UvTmVrby1SYW1lbj9zaGFyZQ==",
        'metadata': dict(),
    }
    try:
        # List transactions from a ledger
        api_response = api_instance.list_transactions(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except ledgerclient.ApiException as e:
        print("Exception when calling LedgerApi->list_transactions: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
pageSize | PageSizeSchema | | optional
page_size | PageSizeSchema | | optional
after | AfterSchema | | optional
reference | ReferenceSchema | | optional
account | AccountSchema | | optional
source | SourceSchema | | optional
destination | DestinationSchema | | optional
startTime | StartTimeSchema | | optional
start_time | StartTimeSchema | | optional
endTime | EndTimeSchema | | optional
end_time | EndTimeSchema | | optional
cursor | CursorSchema | | optional
pagination_token | PaginationTokenSchema | | optional
metadata | MetadataSchema | | optional


# PageSizeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | if omitted the server will use the default value of 15value must be a 64 bit integer

# PageSizeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | if omitted the server will use the default value of 15value must be a 64 bit integer

# AfterSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ReferenceSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# AccountSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# SourceSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# DestinationSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# StartTimeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, datetime,  | str,  |  | value must conform to RFC-3339 date-time

# StartTimeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, datetime,  | str,  |  | value must conform to RFC-3339 date-time

# EndTimeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, datetime,  | str,  |  | value must conform to RFC-3339 date-time

# EndTimeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, datetime,  | str,  |  | value must conform to RFC-3339 date-time

# CursorSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# PaginationTokenSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# MetadataSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
ledger | LedgerSchema | | 

# LedgerSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#list_transactions.ApiResponseFor200) | OK
default | [ApiResponseForDefault](#list_transactions.ApiResponseForDefault) | Error

#### list_transactions.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**TransactionsCursorResponse**](../../models/TransactionsCursorResponse.md) |  | 


#### list_transactions.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **read_stats**
<a name="read_stats"></a>
> StatsResponse read_stats(ledger)

Get statistics from a ledger

Get statistics from a ledger. (aggregate metrics on accounts and transactions) 

### Example

```python
import ledgerclient
from ledgerclient.apis.tags import ledger_api
from ledgerclient.model.error_response import ErrorResponse
from ledgerclient.model.stats_response import StatsResponse
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ledgerclient.Configuration(
    host = "http://localhost"
)

# Enter a context with an instance of the API client
with ledgerclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ledger_api.LedgerApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'ledger': "ledger001",
    }
    try:
        # Get statistics from a ledger
        api_response = api_instance.read_stats(
            path_params=path_params,
        )
        pprint(api_response)
    except ledgerclient.ApiException as e:
        print("Exception when calling LedgerApi->read_stats: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
ledger | LedgerSchema | | 

# LedgerSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#read_stats.ApiResponseFor200) | OK
default | [ApiResponseForDefault](#read_stats.ApiResponseForDefault) | Error

#### read_stats.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**StatsResponse**](../../models/StatsResponse.md) |  | 


#### read_stats.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **revert_transaction**
<a name="revert_transaction"></a>
> TransactionResponse revert_transaction(ledgertxid)

Revert a ledger transaction by its ID

### Example

```python
import ledgerclient
from ledgerclient.apis.tags import ledger_api
from ledgerclient.model.error_response import ErrorResponse
from ledgerclient.model.transaction_response import TransactionResponse
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ledgerclient.Configuration(
    host = "http://localhost"
)

# Enter a context with an instance of the API client
with ledgerclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ledger_api.LedgerApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'ledger': "ledger001",
        'txid': 1234,
    }
    query_params = {
    }
    try:
        # Revert a ledger transaction by its ID
        api_response = api_instance.revert_transaction(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except ledgerclient.ApiException as e:
        print("Exception when calling LedgerApi->revert_transaction: %s\n" % e)

    # example passing only optional values
    path_params = {
        'ledger': "ledger001",
        'txid': 1234,
    }
    query_params = {
        'disableChecks': True,
    }
    try:
        # Revert a ledger transaction by its ID
        api_response = api_instance.revert_transaction(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except ledgerclient.ApiException as e:
        print("Exception when calling LedgerApi->revert_transaction: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
disableChecks | DisableChecksSchema | | optional


# DisableChecksSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
ledger | LedgerSchema | | 
txid | TxidSchema | | 

# LedgerSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# TxidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#revert_transaction.ApiResponseFor200) | OK
default | [ApiResponseForDefault](#revert_transaction.ApiResponseForDefault) | Error

#### revert_transaction.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**TransactionResponse**](../../models/TransactionResponse.md) |  | 


#### revert_transaction.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **run_script**
<a name="run_script"></a>
> ScriptResponse run_script(ledgerscript)

Execute a Numscript

This route is deprecated, and has been merged into `POST /{ledger}/transactions`. 

### Example

```python
import ledgerclient
from ledgerclient.apis.tags import ledger_api
from ledgerclient.model.script_response import ScriptResponse
from ledgerclient.model.script import Script
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ledgerclient.Configuration(
    host = "http://localhost"
)

# Enter a context with an instance of the API client
with ledgerclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ledger_api.LedgerApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'ledger': "ledger001",
    }
    query_params = {
    }
    body = Script(
        plain="vars {\naccount $user\n}\nsend [COIN 10] (\n\tsource = @world\n\tdestination = $user\n)\n",
        vars=dict(),
        reference="order_1234",
        metadata=Metadata(
            key=None,
        ),
    )
    try:
        # Execute a Numscript
        api_response = api_instance.run_script(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except ledgerclient.ApiException as e:
        print("Exception when calling LedgerApi->run_script: %s\n" % e)

    # example passing only optional values
    path_params = {
        'ledger': "ledger001",
    }
    query_params = {
        'preview': True,
    }
    body = Script(
        plain="vars {\naccount $user\n}\nsend [COIN 10] (\n\tsource = @world\n\tdestination = $user\n)\n",
        vars=dict(),
        reference="order_1234",
        metadata=Metadata(
            key=None,
        ),
    )
    try:
        # Execute a Numscript
        api_response = api_instance.run_script(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except ledgerclient.ApiException as e:
        print("Exception when calling LedgerApi->run_script: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Script**](../../models/Script.md) |  | 


### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
preview | PreviewSchema | | optional


# PreviewSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
ledger | LedgerSchema | | 

# LedgerSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#run_script.ApiResponseFor200) | On success, it will return a 200 status code, and the resulting transaction under the &#x60;transaction&#x60; field.  On failure, it will also return a 200 status code, and the following fields:   - &#x60;details&#x60;: contains a URL. When there is an error parsing Numscript, the result can be difficult to read—the provided URL will render the error in an easy-to-read format.   - &#x60;errorCode&#x60; and &#x60;error_code&#x60; (deprecated): contains the string code of the error   - &#x60;errorMessage&#x60; and &#x60;error_message&#x60; (deprecated): contains a human-readable indication of what went wrong, for example that an account had insufficient funds, or that there was an error in the provided Numscript. 

#### run_script.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ScriptResponse**](../../models/ScriptResponse.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **update_mapping**
<a name="update_mapping"></a>
> MappingResponse update_mapping(ledgermapping)

Update the mapping of a ledger

### Example

```python
import ledgerclient
from ledgerclient.apis.tags import ledger_api
from ledgerclient.model.error_response import ErrorResponse
from ledgerclient.model.mapping import Mapping
from ledgerclient.model.mapping_response import MappingResponse
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ledgerclient.Configuration(
    host = "http://localhost"
)

# Enter a context with an instance of the API client
with ledgerclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ledger_api.LedgerApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'ledger': "ledger001",
    }
    body = Mapping(
        contracts=[
            Contract(
                account="users:001",
                expr=dict(),
            )
        ],
    )
    try:
        # Update the mapping of a ledger
        api_response = api_instance.update_mapping(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except ledgerclient.ApiException as e:
        print("Exception when calling LedgerApi->update_mapping: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Mapping**](../../models/Mapping.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
ledger | LedgerSchema | | 

# LedgerSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#update_mapping.ApiResponseFor200) | OK
default | [ApiResponseForDefault](#update_mapping.ApiResponseForDefault) | Error

#### update_mapping.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**MappingResponse**](../../models/MappingResponse.md) |  | 


#### update_mapping.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

