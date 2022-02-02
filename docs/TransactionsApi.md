# ledgerclient.TransactionsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_metadata_on_transaction**](TransactionsApi.md#add_metadata_on_transaction) | **POST** /{ledger}/transactions/{txid}/metadata | Set Transaction Metadata
[**create_transaction**](TransactionsApi.md#create_transaction) | **POST** /{ledger}/transactions | Create Transaction
[**create_transactions**](TransactionsApi.md#create_transactions) | **POST** /{ledger}/transactions/batch | Create Transactions Batch
[**get_transaction**](TransactionsApi.md#get_transaction) | **GET** /{ledger}/transactions/{txid} | Get Transaction
[**list_transactions**](TransactionsApi.md#list_transactions) | **GET** /{ledger}/transactions | Get all Transactions
[**revert_transaction**](TransactionsApi.md#revert_transaction) | **POST** /{ledger}/transactions/{txid}/revert | Revert Transaction


# **add_metadata_on_transaction**
> add_metadata_on_transaction(ledger, txid)

Set Transaction Metadata

Set a new metadata to a ledger transaction by transaction id

### Example

* Basic Authentication (basicAuth):
* Bearer Authentication (cloudToken):

```python
import time
import ledgerclient
from ledgerclient.api import transactions_api
from ledgerclient.model.metadata import Metadata
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ledgerclient.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = ledgerclient.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization: cloudToken
configuration = ledgerclient.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with ledgerclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = transactions_api.TransactionsApi(api_client)
    ledger = "ledger_example" # str | ledger
    txid = 1 # int | txid
    metadata = Metadata(
        key=None,
    ) # Metadata | metadata (optional)

    # example passing only required values which don't have defaults set
    try:
        # Set Transaction Metadata
        api_instance.add_metadata_on_transaction(ledger, txid)
    except ledgerclient.ApiException as e:
        print("Exception when calling TransactionsApi->add_metadata_on_transaction: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Set Transaction Metadata
        api_instance.add_metadata_on_transaction(ledger, txid, metadata=metadata)
    except ledgerclient.ApiException as e:
        print("Exception when calling TransactionsApi->add_metadata_on_transaction: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ledger** | **str**| ledger |
 **txid** | **int**| txid |
 **metadata** | [**Metadata**](Metadata.md)| metadata | [optional]

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth), [cloudToken](../README.md#cloudToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Empty response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_transaction**
> CreateTransactionResponse create_transaction(ledger, transaction_data)

Create Transaction

Create a new ledger transaction Commit a new transaction to the ledger

### Example

* Basic Authentication (basicAuth):
* Bearer Authentication (cloudToken):

```python
import time
import ledgerclient
from ledgerclient.api import transactions_api
from ledgerclient.model.error_response import ErrorResponse
from ledgerclient.model.transaction_data import TransactionData
from ledgerclient.model.create_transaction_response import CreateTransactionResponse
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ledgerclient.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = ledgerclient.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization: cloudToken
configuration = ledgerclient.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with ledgerclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = transactions_api.TransactionsApi(api_client)
    ledger = "ledger_example" # str | ledger
    transaction_data = TransactionData(
        metadata={},
        postings=[
            Posting(
                amount=1,
                asset="asset_example",
                destination="destination_example",
                source="source_example",
            ),
        ],
        reference="reference_example",
    ) # TransactionData | transaction

    # example passing only required values which don't have defaults set
    try:
        # Create Transaction
        api_response = api_instance.create_transaction(ledger, transaction_data)
        pprint(api_response)
    except ledgerclient.ApiException as e:
        print("Exception when calling TransactionsApi->create_transaction: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ledger** | **str**| ledger |
 **transaction_data** | [**TransactionData**](TransactionData.md)| transaction |

### Return type

[**CreateTransactionResponse**](CreateTransactionResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [cloudToken](../README.md#cloudToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Commit error |  -  |
**409** | Confict |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_transactions**
> TransactionListResponse create_transactions(ledger, transactions)

Create Transactions Batch

Create a new ledger transactions batch Commit a batch of new transactions to the ledger

### Example

* Basic Authentication (basicAuth):
* Bearer Authentication (cloudToken):

```python
import time
import ledgerclient
from ledgerclient.api import transactions_api
from ledgerclient.model.transactions import Transactions
from ledgerclient.model.transaction_list_response import TransactionListResponse
from ledgerclient.model.transaction_commit_error_response import TransactionCommitErrorResponse
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ledgerclient.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = ledgerclient.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization: cloudToken
configuration = ledgerclient.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with ledgerclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = transactions_api.TransactionsApi(api_client)
    ledger = "ledger_example" # str | ledger
    transactions = Transactions(
        transactions=[
            TransactionData(
                metadata={},
                postings=[
                    Posting(
                        amount=1,
                        asset="asset_example",
                        destination="destination_example",
                        source="source_example",
                    ),
                ],
                reference="reference_example",
            ),
        ],
    ) # Transactions | transactions

    # example passing only required values which don't have defaults set
    try:
        # Create Transactions Batch
        api_response = api_instance.create_transactions(ledger, transactions)
        pprint(api_response)
    except ledgerclient.ApiException as e:
        print("Exception when calling TransactionsApi->create_transactions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ledger** | **str**| ledger |
 **transactions** | [**Transactions**](Transactions.md)| transactions |

### Return type

[**TransactionListResponse**](TransactionListResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [cloudToken](../README.md#cloudToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_transaction**
> TransactionResponse get_transaction(ledger, txid)

Get Transaction

Get transaction by transaction id

### Example

* Basic Authentication (basicAuth):
* Bearer Authentication (cloudToken):

```python
import time
import ledgerclient
from ledgerclient.api import transactions_api
from ledgerclient.model.error_response import ErrorResponse
from ledgerclient.model.transaction_response import TransactionResponse
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ledgerclient.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = ledgerclient.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization: cloudToken
configuration = ledgerclient.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with ledgerclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = transactions_api.TransactionsApi(api_client)
    ledger = "ledger_example" # str | ledger
    txid = 1 # int | txid

    # example passing only required values which don't have defaults set
    try:
        # Get Transaction
        api_response = api_instance.get_transaction(ledger, txid)
        pprint(api_response)
    except ledgerclient.ApiException as e:
        print("Exception when calling TransactionsApi->get_transaction: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ledger** | **str**| ledger |
 **txid** | **int**| txid |

### Return type

[**TransactionResponse**](TransactionResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [cloudToken](../README.md#cloudToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_transactions**
> TransactionCursorResponse list_transactions(ledger)

Get all Transactions

Get all ledger transactions

### Example

* Basic Authentication (basicAuth):
* Bearer Authentication (cloudToken):

```python
import time
import ledgerclient
from ledgerclient.api import transactions_api
from ledgerclient.model.transaction_cursor_response import TransactionCursorResponse
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ledgerclient.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = ledgerclient.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization: cloudToken
configuration = ledgerclient.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with ledgerclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = transactions_api.TransactionsApi(api_client)
    ledger = "ledger_example" # str | ledger
    after = "after_example" # str | pagination cursor, will return transactions after given txid (in descending order) (optional)
    reference = "reference_example" # str | find transactions by reference field (optional)
    account = "account_example" # str | find transactions with postings involving given account, either as source or destination (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get all Transactions
        api_response = api_instance.list_transactions(ledger)
        pprint(api_response)
    except ledgerclient.ApiException as e:
        print("Exception when calling TransactionsApi->list_transactions: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get all Transactions
        api_response = api_instance.list_transactions(ledger, after=after, reference=reference, account=account)
        pprint(api_response)
    except ledgerclient.ApiException as e:
        print("Exception when calling TransactionsApi->list_transactions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ledger** | **str**| ledger |
 **after** | **str**| pagination cursor, will return transactions after given txid (in descending order) | [optional]
 **reference** | **str**| find transactions by reference field | [optional]
 **account** | **str**| find transactions with postings involving given account, either as source or destination | [optional]

### Return type

[**TransactionCursorResponse**](TransactionCursorResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [cloudToken](../README.md#cloudToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **revert_transaction**
> revert_transaction(ledger, txid)

Revert Transaction

Revert a ledger transaction by transaction id

### Example

* Basic Authentication (basicAuth):
* Bearer Authentication (cloudToken):

```python
import time
import ledgerclient
from ledgerclient.api import transactions_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ledgerclient.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = ledgerclient.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization: cloudToken
configuration = ledgerclient.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with ledgerclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = transactions_api.TransactionsApi(api_client)
    ledger = "ledger_example" # str | ledger
    txid = 1 # int | txid

    # example passing only required values which don't have defaults set
    try:
        # Revert Transaction
        api_instance.revert_transaction(ledger, txid)
    except ledgerclient.ApiException as e:
        print("Exception when calling TransactionsApi->revert_transaction: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ledger** | **str**| ledger |
 **txid** | **int**| txid |

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth), [cloudToken](../README.md#cloudToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Empty response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

