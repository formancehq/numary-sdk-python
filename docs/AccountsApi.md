# ledgerclient.AccountsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_metadata_to_account**](AccountsApi.md#add_metadata_to_account) | **POST** /{ledger}/accounts/{address}/metadata | Add metadata to an account.
[**count_accounts**](AccountsApi.md#count_accounts) | **HEAD** /{ledger}/accounts | Count the accounts from a ledger.
[**get_account**](AccountsApi.md#get_account) | **GET** /{ledger}/accounts/{address} | Get account by its address.
[**list_accounts**](AccountsApi.md#list_accounts) | **GET** /{ledger}/accounts | List accounts from a ledger.


# **add_metadata_to_account**
> add_metadata_to_account(ledger, address, metadata)

Add metadata to an account.

### Example

* Basic Authentication (basicAuth):

```python
import time
import ledgerclient
from ledgerclient.api import accounts_api
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

# Enter a context with an instance of the API client
with ledgerclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = accounts_api.AccountsApi(api_client)
    ledger = "ledger001" # str | Name of the ledger.
    address = "users:001" # str | Exact address of the account.
    metadata = Metadata(
        key=None,
    ) # Metadata | metadata

    # example passing only required values which don't have defaults set
    try:
        # Add metadata to an account.
        api_instance.add_metadata_to_account(ledger, address, metadata)
    except ledgerclient.ApiException as e:
        print("Exception when calling AccountsApi->add_metadata_to_account: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ledger** | **str**| Name of the ledger. |
 **address** | **str**| Exact address of the account. |
 **metadata** | [**Metadata**](Metadata.md)| metadata |

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Empty response |  -  |
**400** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **count_accounts**
> count_accounts(ledger)

Count the accounts from a ledger.

### Example

* Basic Authentication (basicAuth):

```python
import time
import ledgerclient
from ledgerclient.api import accounts_api
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

# Enter a context with an instance of the API client
with ledgerclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = accounts_api.AccountsApi(api_client)
    ledger = "ledger001" # str | Name of the ledger.
    address = "users:.+" # str | Filter accounts by address pattern (regular expression placed between ^ and $). (optional)
    metadata = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Filter accounts by metadata key value pairs. Nested objects can be used as seen in the example below. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Count the accounts from a ledger.
        api_instance.count_accounts(ledger)
    except ledgerclient.ApiException as e:
        print("Exception when calling AccountsApi->count_accounts: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Count the accounts from a ledger.
        api_instance.count_accounts(ledger, address=address, metadata=metadata)
    except ledgerclient.ApiException as e:
        print("Exception when calling AccountsApi->count_accounts: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ledger** | **str**| Name of the ledger. |
 **address** | **str**| Filter accounts by address pattern (regular expression placed between ^ and $). | [optional]
 **metadata** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Filter accounts by metadata key value pairs. Nested objects can be used as seen in the example below. | [optional]

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * Count -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_account**
> GetAccount200Response get_account(ledger, address)

Get account by its address.

### Example

* Basic Authentication (basicAuth):

```python
import time
import ledgerclient
from ledgerclient.api import accounts_api
from ledgerclient.model.get_account200_response import GetAccount200Response
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

# Enter a context with an instance of the API client
with ledgerclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = accounts_api.AccountsApi(api_client)
    ledger = "ledger001" # str | Name of the ledger.
    address = "users:001" # str | Exact address of the account.

    # example passing only required values which don't have defaults set
    try:
        # Get account by its address.
        api_response = api_instance.get_account(ledger, address)
        pprint(api_response)
    except ledgerclient.ApiException as e:
        print("Exception when calling AccountsApi->get_account: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ledger** | **str**| Name of the ledger. |
 **address** | **str**| Exact address of the account. |

### Return type

[**GetAccount200Response**](GetAccount200Response.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_accounts**
> ListAccounts200Response list_accounts(ledger)

List accounts from a ledger.

List accounts from a ledger, sorted by address in descending order.

### Example

* Basic Authentication (basicAuth):

```python
import time
import ledgerclient
from ledgerclient.api import accounts_api
from ledgerclient.model.list_accounts200_response import ListAccounts200Response
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

# Enter a context with an instance of the API client
with ledgerclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = accounts_api.AccountsApi(api_client)
    ledger = "ledger001" # str | Name of the ledger.
    after = "users:003" # str | Pagination cursor, will return accounts after given address, in descending order. (optional)
    address = "users:.+" # str | Filter accounts by address pattern (regular expression placed between ^ and $). (optional)
    metadata = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Filter accounts by metadata key value pairs. Nested objects can be used as seen in the example below. (optional)

    # example passing only required values which don't have defaults set
    try:
        # List accounts from a ledger.
        api_response = api_instance.list_accounts(ledger)
        pprint(api_response)
    except ledgerclient.ApiException as e:
        print("Exception when calling AccountsApi->list_accounts: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List accounts from a ledger.
        api_response = api_instance.list_accounts(ledger, after=after, address=address, metadata=metadata)
        pprint(api_response)
    except ledgerclient.ApiException as e:
        print("Exception when calling AccountsApi->list_accounts: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ledger** | **str**| Name of the ledger. |
 **after** | **str**| Pagination cursor, will return accounts after given address, in descending order. | [optional]
 **address** | **str**| Filter accounts by address pattern (regular expression placed between ^ and $). | [optional]
 **metadata** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Filter accounts by metadata key value pairs. Nested objects can be used as seen in the example below. | [optional]

### Return type

[**ListAccounts200Response**](ListAccounts200Response.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

