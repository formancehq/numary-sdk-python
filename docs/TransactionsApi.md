# ledgerclient.TransactionsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_metadata_on_transaction**](TransactionsApi.md#add_metadata_on_transaction) | **POST** /{ledger}/transactions/{txid}/metadata | Set the metadata of a transaction by its ID
[**count_transactions**](TransactionsApi.md#count_transactions) | **HEAD** /{ledger}/transactions | Count the transactions from a ledger
[**create_transaction**](TransactionsApi.md#create_transaction) | **POST** /{ledger}/transactions | Create a new transaction to a ledger
[**create_transactions**](TransactionsApi.md#create_transactions) | **POST** /{ledger}/transactions/batch | Create a new batch of transactions to a ledger
[**get_transaction**](TransactionsApi.md#get_transaction) | **GET** /{ledger}/transactions/{txid} | Get transaction from a ledger by its ID
[**list_transactions**](TransactionsApi.md#list_transactions) | **GET** /{ledger}/transactions | List transactions from a ledger
[**revert_transaction**](TransactionsApi.md#revert_transaction) | **POST** /{ledger}/transactions/{txid}/revert | Revert a ledger transaction by its ID


# **add_metadata_on_transaction**
> add_metadata_on_transaction(ledger, txid)

Set the metadata of a transaction by its ID

### Example


```python
import time
import ledgerclient
from ledgerclient.api import transactions_api
from ledgerclient.model.error_response import ErrorResponse
from ledgerclient.model.metadata import Metadata
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ledgerclient.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with ledgerclient.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = transactions_api.TransactionsApi(api_client)
    ledger = "ledger001" # str | Name of the ledger.
    txid = 1234 # int | Transaction ID.
    metadata = Metadata(
        key=None,
    ) # Metadata | metadata (optional)

    # example passing only required values which don't have defaults set
    try:
        # Set the metadata of a transaction by its ID
        api_instance.add_metadata_on_transaction(ledger, txid)
    except ledgerclient.ApiException as e:
        print("Exception when calling TransactionsApi->add_metadata_on_transaction: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Set the metadata of a transaction by its ID
        api_instance.add_metadata_on_transaction(ledger, txid, metadata=metadata)
    except ledgerclient.ApiException as e:
        print("Exception when calling TransactionsApi->add_metadata_on_transaction: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ledger** | **str**| Name of the ledger. |
 **txid** | **int**| Transaction ID. |
 **metadata** | [**Metadata**](Metadata.md)| metadata | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **count_transactions**
> count_transactions(ledger)

Count the transactions from a ledger

### Example


```python
import time
import ledgerclient
from ledgerclient.api import transactions_api
from ledgerclient.model.error_response import ErrorResponse
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ledgerclient.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with ledgerclient.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = transactions_api.TransactionsApi(api_client)
    ledger = "ledger001" # str | Name of the ledger.
    reference = "ref:001" # str | Filter transactions by reference field. (optional)
    account = "users:001" # str | Filter transactions with postings involving given account, either as source or destination (regular expression placed between ^ and $). (optional)
    source = "users:001" # str | Filter transactions with postings involving given account at source (regular expression placed between ^ and $). (optional)
    destination = "users:001" # str | Filter transactions with postings involving given account at destination (regular expression placed between ^ and $). (optional)
    start_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Filter transactions that occurred after this timestamp. The format is RFC3339 and is inclusive (for example, \"2023-01-02T15:04:01Z\" includes the first second of 4th minute).  (optional)
    start_time2 = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Filter transactions that occurred after this timestamp. The format is RFC3339 and is inclusive (for example, \"2023-01-02T15:04:01Z\" includes the first second of 4th minute). Deprecated, please use `startTime` instead.  (optional)
    end_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Filter transactions that occurred before this timestamp. The format is RFC3339 and is exclusive (for example, \"2023-01-02T15:04:01Z\" excludes the first second of 4th minute).  (optional)
    end_time2 = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Filter transactions that occurred before this timestamp. The format is RFC3339 and is exclusive (for example, \"2023-01-02T15:04:01Z\" excludes the first second of 4th minute). Deprecated, please use `endTime` instead.  (optional)
    metadata = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Filter transactions by metadata key value pairs. Nested objects can be used as seen in the example below. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Count the transactions from a ledger
        api_instance.count_transactions(ledger)
    except ledgerclient.ApiException as e:
        print("Exception when calling TransactionsApi->count_transactions: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Count the transactions from a ledger
        api_instance.count_transactions(ledger, reference=reference, account=account, source=source, destination=destination, start_time=start_time, start_time2=start_time2, end_time=end_time, end_time2=end_time2, metadata=metadata)
    except ledgerclient.ApiException as e:
        print("Exception when calling TransactionsApi->count_transactions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ledger** | **str**| Name of the ledger. |
 **reference** | **str**| Filter transactions by reference field. | [optional]
 **account** | **str**| Filter transactions with postings involving given account, either as source or destination (regular expression placed between ^ and $). | [optional]
 **source** | **str**| Filter transactions with postings involving given account at source (regular expression placed between ^ and $). | [optional]
 **destination** | **str**| Filter transactions with postings involving given account at destination (regular expression placed between ^ and $). | [optional]
 **start_time** | **datetime**| Filter transactions that occurred after this timestamp. The format is RFC3339 and is inclusive (for example, \&quot;2023-01-02T15:04:01Z\&quot; includes the first second of 4th minute).  | [optional]
 **start_time2** | **datetime**| Filter transactions that occurred after this timestamp. The format is RFC3339 and is inclusive (for example, \&quot;2023-01-02T15:04:01Z\&quot; includes the first second of 4th minute). Deprecated, please use &#x60;startTime&#x60; instead.  | [optional]
 **end_time** | **datetime**| Filter transactions that occurred before this timestamp. The format is RFC3339 and is exclusive (for example, \&quot;2023-01-02T15:04:01Z\&quot; excludes the first second of 4th minute).  | [optional]
 **end_time2** | **datetime**| Filter transactions that occurred before this timestamp. The format is RFC3339 and is exclusive (for example, \&quot;2023-01-02T15:04:01Z\&quot; excludes the first second of 4th minute). Deprecated, please use &#x60;endTime&#x60; instead.  | [optional]
 **metadata** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Filter transactions by metadata key value pairs. Nested objects can be used as seen in the example below. | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * Count -  <br>  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_transaction**
> TransactionsResponse create_transaction(ledger, post_transaction)

Create a new transaction to a ledger

### Example


```python
import time
import ledgerclient
from ledgerclient.api import transactions_api
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
with ledgerclient.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = transactions_api.TransactionsApi(api_client)
    ledger = "ledger001" # str | Name of the ledger.
    post_transaction = PostTransaction(
        timestamp=dateutil_parser('1970-01-01T00:00:00.00Z'),
        postings=[
            Posting(
                amount=100,
                asset="COIN",
                destination="users:002",
                source="users:001",
            ),
        ],
        script=PostTransactionScript(
            plain='''vars {
account $user
}
send [COIN 10] (
	source = @world
	destination = $user
)
''',
            vars={},
        ),
        reference="ref:001",
        metadata=Metadata(
            key=None,
        ),
    ) # PostTransaction | The request body must contain at least one of the following objects:   - `postings`: suitable for simple transactions   - `script`: enabling more complex transactions with Numscript 
    preview = True # bool | Set the preview mode. Preview mode doesn't add the logs to the database or publish a message to the message broker. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create a new transaction to a ledger
        api_response = api_instance.create_transaction(ledger, post_transaction)
        pprint(api_response)
    except ledgerclient.ApiException as e:
        print("Exception when calling TransactionsApi->create_transaction: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a new transaction to a ledger
        api_response = api_instance.create_transaction(ledger, post_transaction, preview=preview)
        pprint(api_response)
    except ledgerclient.ApiException as e:
        print("Exception when calling TransactionsApi->create_transaction: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ledger** | **str**| Name of the ledger. |
 **post_transaction** | [**PostTransaction**](PostTransaction.md)| The request body must contain at least one of the following objects:   - &#x60;postings&#x60;: suitable for simple transactions   - &#x60;script&#x60;: enabling more complex transactions with Numscript  |
 **preview** | **bool**| Set the preview mode. Preview mode doesn&#39;t add the logs to the database or publish a message to the message broker. | [optional]

### Return type

[**TransactionsResponse**](TransactionsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_transactions**
> TransactionsResponse create_transactions(ledger, transactions)

Create a new batch of transactions to a ledger

### Example


```python
import time
import ledgerclient
from ledgerclient.api import transactions_api
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
with ledgerclient.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = transactions_api.TransactionsApi(api_client)
    ledger = "ledger001" # str | Name of the ledger.
    transactions = Transactions(
        transactions=[
            TransactionData(
                postings=[
                    Posting(
                        amount=100,
                        asset="COIN",
                        destination="users:002",
                        source="users:001",
                    ),
                ],
                reference="ref:001",
                metadata=Metadata(
                    key=None,
                ),
                timestamp=dateutil_parser('1970-01-01T00:00:00.00Z'),
            ),
        ],
    ) # Transactions | 

    # example passing only required values which don't have defaults set
    try:
        # Create a new batch of transactions to a ledger
        api_response = api_instance.create_transactions(ledger, transactions)
        pprint(api_response)
    except ledgerclient.ApiException as e:
        print("Exception when calling TransactionsApi->create_transactions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ledger** | **str**| Name of the ledger. |
 **transactions** | [**Transactions**](Transactions.md)|  |

### Return type

[**TransactionsResponse**](TransactionsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_transaction**
> TransactionResponse get_transaction(ledger, txid)

Get transaction from a ledger by its ID

### Example


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


# Enter a context with an instance of the API client
with ledgerclient.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = transactions_api.TransactionsApi(api_client)
    ledger = "ledger001" # str | Name of the ledger.
    txid = 1234 # int | Transaction ID.

    # example passing only required values which don't have defaults set
    try:
        # Get transaction from a ledger by its ID
        api_response = api_instance.get_transaction(ledger, txid)
        pprint(api_response)
    except ledgerclient.ApiException as e:
        print("Exception when calling TransactionsApi->get_transaction: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ledger** | **str**| Name of the ledger. |
 **txid** | **int**| Transaction ID. |

### Return type

[**TransactionResponse**](TransactionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_transactions**
> TransactionsCursorResponse list_transactions(ledger)

List transactions from a ledger

List transactions from a ledger, sorted by txid in descending order.

### Example


```python
import time
import ledgerclient
from ledgerclient.api import transactions_api
from ledgerclient.model.error_response import ErrorResponse
from ledgerclient.model.transactions_cursor_response import TransactionsCursorResponse
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ledgerclient.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with ledgerclient.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = transactions_api.TransactionsApi(api_client)
    ledger = "ledger001" # str | Name of the ledger.
    page_size = 100 # int | The maximum number of results to return per page.  (optional) if omitted the server will use the default value of 15
    page_size2 = 100 # int | The maximum number of results to return per page. Deprecated, please use `pageSize` instead.  (optional) if omitted the server will use the default value of 15
    after = "1234" # str | Pagination cursor, will return transactions after given txid (in descending order). (optional)
    reference = "ref:001" # str | Find transactions by reference field. (optional)
    account = "users:001" # str | Filter transactions with postings involving given account, either as source or destination (regular expression placed between ^ and $). (optional)
    source = "users:001" # str | Filter transactions with postings involving given account at source (regular expression placed between ^ and $). (optional)
    destination = "users:001" # str | Filter transactions with postings involving given account at destination (regular expression placed between ^ and $). (optional)
    start_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Filter transactions that occurred after this timestamp. The format is RFC3339 and is inclusive (for example, \"2023-01-02T15:04:01Z\" includes the first second of 4th minute).  (optional)
    start_time2 = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Filter transactions that occurred after this timestamp. The format is RFC3339 and is inclusive (for example, \"2023-01-02T15:04:01Z\" includes the first second of 4th minute). Deprecated, please use `startTime` instead.  (optional)
    end_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Filter transactions that occurred before this timestamp. The format is RFC3339 and is exclusive (for example, \"2023-01-02T15:04:01Z\" excludes the first second of 4th minute).  (optional)
    end_time2 = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Filter transactions that occurred before this timestamp. The format is RFC3339 and is exclusive (for example, \"2023-01-02T15:04:01Z\" excludes the first second of 4th minute). Deprecated, please use `endTime` instead.  (optional)
    cursor = "aHR0cHM6Ly9nLnBhZ2UvTmVrby1SYW1lbj9zaGFyZQ==" # str | Parameter used in pagination requests. Maximum page size is set to 15. Set to the value of next for the next page of results. Set to the value of previous for the previous page of results. No other parameters can be set when this parameter is set.  (optional)
    pagination_token = "aHR0cHM6Ly9nLnBhZ2UvTmVrby1SYW1lbj9zaGFyZQ==" # str | Parameter used in pagination requests. Maximum page size is set to 15. Set to the value of next for the next page of results. Set to the value of previous for the previous page of results. No other parameters can be set when this parameter is set. Deprecated, please use `cursor` instead.  (optional)
    metadata = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Filter transactions by metadata key value pairs. Nested objects can be used as seen in the example below. (optional)

    # example passing only required values which don't have defaults set
    try:
        # List transactions from a ledger
        api_response = api_instance.list_transactions(ledger)
        pprint(api_response)
    except ledgerclient.ApiException as e:
        print("Exception when calling TransactionsApi->list_transactions: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List transactions from a ledger
        api_response = api_instance.list_transactions(ledger, page_size=page_size, page_size2=page_size2, after=after, reference=reference, account=account, source=source, destination=destination, start_time=start_time, start_time2=start_time2, end_time=end_time, end_time2=end_time2, cursor=cursor, pagination_token=pagination_token, metadata=metadata)
        pprint(api_response)
    except ledgerclient.ApiException as e:
        print("Exception when calling TransactionsApi->list_transactions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ledger** | **str**| Name of the ledger. |
 **page_size** | **int**| The maximum number of results to return per page.  | [optional] if omitted the server will use the default value of 15
 **page_size2** | **int**| The maximum number of results to return per page. Deprecated, please use &#x60;pageSize&#x60; instead.  | [optional] if omitted the server will use the default value of 15
 **after** | **str**| Pagination cursor, will return transactions after given txid (in descending order). | [optional]
 **reference** | **str**| Find transactions by reference field. | [optional]
 **account** | **str**| Filter transactions with postings involving given account, either as source or destination (regular expression placed between ^ and $). | [optional]
 **source** | **str**| Filter transactions with postings involving given account at source (regular expression placed between ^ and $). | [optional]
 **destination** | **str**| Filter transactions with postings involving given account at destination (regular expression placed between ^ and $). | [optional]
 **start_time** | **datetime**| Filter transactions that occurred after this timestamp. The format is RFC3339 and is inclusive (for example, \&quot;2023-01-02T15:04:01Z\&quot; includes the first second of 4th minute).  | [optional]
 **start_time2** | **datetime**| Filter transactions that occurred after this timestamp. The format is RFC3339 and is inclusive (for example, \&quot;2023-01-02T15:04:01Z\&quot; includes the first second of 4th minute). Deprecated, please use &#x60;startTime&#x60; instead.  | [optional]
 **end_time** | **datetime**| Filter transactions that occurred before this timestamp. The format is RFC3339 and is exclusive (for example, \&quot;2023-01-02T15:04:01Z\&quot; excludes the first second of 4th minute).  | [optional]
 **end_time2** | **datetime**| Filter transactions that occurred before this timestamp. The format is RFC3339 and is exclusive (for example, \&quot;2023-01-02T15:04:01Z\&quot; excludes the first second of 4th minute). Deprecated, please use &#x60;endTime&#x60; instead.  | [optional]
 **cursor** | **str**| Parameter used in pagination requests. Maximum page size is set to 15. Set to the value of next for the next page of results. Set to the value of previous for the previous page of results. No other parameters can be set when this parameter is set.  | [optional]
 **pagination_token** | **str**| Parameter used in pagination requests. Maximum page size is set to 15. Set to the value of next for the next page of results. Set to the value of previous for the previous page of results. No other parameters can be set when this parameter is set. Deprecated, please use &#x60;cursor&#x60; instead.  | [optional]
 **metadata** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Filter transactions by metadata key value pairs. Nested objects can be used as seen in the example below. | [optional]

### Return type

[**TransactionsCursorResponse**](TransactionsCursorResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **revert_transaction**
> TransactionResponse revert_transaction(ledger, txid)

Revert a ledger transaction by its ID

### Example


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


# Enter a context with an instance of the API client
with ledgerclient.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = transactions_api.TransactionsApi(api_client)
    ledger = "ledger001" # str | Name of the ledger.
    txid = 1234 # int | Transaction ID.

    # example passing only required values which don't have defaults set
    try:
        # Revert a ledger transaction by its ID
        api_response = api_instance.revert_transaction(ledger, txid)
        pprint(api_response)
    except ledgerclient.ApiException as e:
        print("Exception when calling TransactionsApi->revert_transaction: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ledger** | **str**| Name of the ledger. |
 **txid** | **int**| Transaction ID. |

### Return type

[**TransactionResponse**](TransactionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

