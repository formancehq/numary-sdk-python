# ledgerclient.AccountsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_metadata_to_account**](AccountsApi.md#add_metadata_to_account) | **POST** /{ledger}/accounts/{address}/metadata | Add metadata to an account
[**count_accounts**](AccountsApi.md#count_accounts) | **HEAD** /{ledger}/accounts | Count the accounts from a ledger
[**get_account**](AccountsApi.md#get_account) | **GET** /{ledger}/accounts/{address} | Get account by its address
[**list_accounts**](AccountsApi.md#list_accounts) | **GET** /{ledger}/accounts | List accounts from a ledger


# **add_metadata_to_account**
> add_metadata_to_account(ledger, address, metadata)

Add metadata to an account

### Example


```python
import time
import ledgerclient
from ledgerclient.api import accounts_api
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
    api_instance = accounts_api.AccountsApi(api_client)
    ledger = "ledger001" # str | Name of the ledger.
    address = "users:001" # str | Exact address of the account. It must match the following regular expressions pattern: ``` ^\\w+(:\\w+)*$ ``` 
    metadata = Metadata(
        key=None,
    ) # Metadata | metadata

    # example passing only required values which don't have defaults set
    try:
        # Add metadata to an account
        api_instance.add_metadata_to_account(ledger, address, metadata)
    except ledgerclient.ApiException as e:
        print("Exception when calling AccountsApi->add_metadata_to_account: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ledger** | **str**| Name of the ledger. |
 **address** | **str**| Exact address of the account. It must match the following regular expressions pattern: &#x60;&#x60;&#x60; ^\\w+(:\\w+)*$ &#x60;&#x60;&#x60;  |
 **metadata** | [**Metadata**](Metadata.md)| metadata |

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

# **count_accounts**
> count_accounts(ledger)

Count the accounts from a ledger

### Example


```python
import time
import ledgerclient
from ledgerclient.api import accounts_api
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
    api_instance = accounts_api.AccountsApi(api_client)
    ledger = "ledger001" # str | Name of the ledger.
    address = "users:.+" # str | Filter accounts by address pattern (regular expression placed between ^ and $). (optional)
    metadata = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Filter accounts by metadata key value pairs. The filter can be used like this metadata[key]=value1&metadata[a.nested.key]=value2 (optional)

    # example passing only required values which don't have defaults set
    try:
        # Count the accounts from a ledger
        api_instance.count_accounts(ledger)
    except ledgerclient.ApiException as e:
        print("Exception when calling AccountsApi->count_accounts: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Count the accounts from a ledger
        api_instance.count_accounts(ledger, address=address, metadata=metadata)
    except ledgerclient.ApiException as e:
        print("Exception when calling AccountsApi->count_accounts: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ledger** | **str**| Name of the ledger. |
 **address** | **str**| Filter accounts by address pattern (regular expression placed between ^ and $). | [optional]
 **metadata** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Filter accounts by metadata key value pairs. The filter can be used like this metadata[key]&#x3D;value1&amp;metadata[a.nested.key]&#x3D;value2 | [optional]

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

# **get_account**
> AccountResponse get_account(ledger, address)

Get account by its address

### Example


```python
import time
import ledgerclient
from ledgerclient.api import accounts_api
from ledgerclient.model.error_response import ErrorResponse
from ledgerclient.model.account_response import AccountResponse
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ledgerclient.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with ledgerclient.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = accounts_api.AccountsApi(api_client)
    ledger = "ledger001" # str | Name of the ledger.
    address = "users:001" # str | Exact address of the account. It must match the following regular expressions pattern: ``` ^\\w+(:\\w+)*$ ``` 

    # example passing only required values which don't have defaults set
    try:
        # Get account by its address
        api_response = api_instance.get_account(ledger, address)
        pprint(api_response)
    except ledgerclient.ApiException as e:
        print("Exception when calling AccountsApi->get_account: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ledger** | **str**| Name of the ledger. |
 **address** | **str**| Exact address of the account. It must match the following regular expressions pattern: &#x60;&#x60;&#x60; ^\\w+(:\\w+)*$ &#x60;&#x60;&#x60;  |

### Return type

[**AccountResponse**](AccountResponse.md)

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

# **list_accounts**
> AccountsCursorResponse list_accounts(ledger)

List accounts from a ledger

List accounts from a ledger, sorted by address in descending order.

### Example


```python
import time
import ledgerclient
from ledgerclient.api import accounts_api
from ledgerclient.model.error_response import ErrorResponse
from ledgerclient.model.accounts_cursor_response import AccountsCursorResponse
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ledgerclient.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with ledgerclient.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = accounts_api.AccountsApi(api_client)
    ledger = "ledger001" # str | Name of the ledger.
    page_size = 100 # int | The maximum number of results to return per page.  (optional) if omitted the server will use the default value of 15
    page_size2 = 100 # int | The maximum number of results to return per page. Deprecated, please use `pageSize` instead.  (optional) if omitted the server will use the default value of 15
    after = "users:003" # str | Pagination cursor, will return accounts after given address, in descending order. (optional)
    address = "users:.+" # str | Filter accounts by address pattern (regular expression placed between ^ and $). (optional)
    metadata = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Filter accounts by metadata key value pairs. Nested objects can be used as seen in the example below. (optional)
    balance = 2400 # int | Filter accounts by their balance (default operator is gte) (optional)
    balance_operator = "gte" # str | Operator used for the filtering of balances can be greater than/equal, less than/equal, greater than, less than, equal or not.  (optional)
    balance_operator2 = "gte" # str | Operator used for the filtering of balances can be greater than/equal, less than/equal, greater than, less than, equal or not. Deprecated, please use `balanceOperator` instead.  (optional)
    cursor = "aHR0cHM6Ly9nLnBhZ2UvTmVrby1SYW1lbj9zaGFyZQ==" # str | Parameter used in pagination requests. Maximum page size is set to 15. Set to the value of next for the next page of results. Set to the value of previous for the previous page of results. No other parameters can be set when this parameter is set.  (optional)
    pagination_token = "aHR0cHM6Ly9nLnBhZ2UvTmVrby1SYW1lbj9zaGFyZQ==" # str | Parameter used in pagination requests. Maximum page size is set to 15. Set to the value of next for the next page of results. Set to the value of previous for the previous page of results. No other parameters can be set when this parameter is set. Deprecated, please use `cursor` instead.  (optional)

    # example passing only required values which don't have defaults set
    try:
        # List accounts from a ledger
        api_response = api_instance.list_accounts(ledger)
        pprint(api_response)
    except ledgerclient.ApiException as e:
        print("Exception when calling AccountsApi->list_accounts: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List accounts from a ledger
        api_response = api_instance.list_accounts(ledger, page_size=page_size, page_size2=page_size2, after=after, address=address, metadata=metadata, balance=balance, balance_operator=balance_operator, balance_operator2=balance_operator2, cursor=cursor, pagination_token=pagination_token)
        pprint(api_response)
    except ledgerclient.ApiException as e:
        print("Exception when calling AccountsApi->list_accounts: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ledger** | **str**| Name of the ledger. |
 **page_size** | **int**| The maximum number of results to return per page.  | [optional] if omitted the server will use the default value of 15
 **page_size2** | **int**| The maximum number of results to return per page. Deprecated, please use &#x60;pageSize&#x60; instead.  | [optional] if omitted the server will use the default value of 15
 **after** | **str**| Pagination cursor, will return accounts after given address, in descending order. | [optional]
 **address** | **str**| Filter accounts by address pattern (regular expression placed between ^ and $). | [optional]
 **metadata** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Filter accounts by metadata key value pairs. Nested objects can be used as seen in the example below. | [optional]
 **balance** | **int**| Filter accounts by their balance (default operator is gte) | [optional]
 **balance_operator** | **str**| Operator used for the filtering of balances can be greater than/equal, less than/equal, greater than, less than, equal or not.  | [optional]
 **balance_operator2** | **str**| Operator used for the filtering of balances can be greater than/equal, less than/equal, greater than, less than, equal or not. Deprecated, please use &#x60;balanceOperator&#x60; instead.  | [optional]
 **cursor** | **str**| Parameter used in pagination requests. Maximum page size is set to 15. Set to the value of next for the next page of results. Set to the value of previous for the previous page of results. No other parameters can be set when this parameter is set.  | [optional]
 **pagination_token** | **str**| Parameter used in pagination requests. Maximum page size is set to 15. Set to the value of next for the next page of results. Set to the value of previous for the previous page of results. No other parameters can be set when this parameter is set. Deprecated, please use &#x60;cursor&#x60; instead.  | [optional]

### Return type

[**AccountsCursorResponse**](AccountsCursorResponse.md)

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

