# ledgerclient.AccountsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_metadata_to_account**](AccountsApi.md#add_metadata_to_account) | **POST** /{ledger}/accounts/{accountId}/metadata | Add metadata to account
[**get_account**](AccountsApi.md#get_account) | **GET** /{ledger}/accounts/{accountId} | Get account by address
[**list_accounts**](AccountsApi.md#list_accounts) | **GET** /{ledger}/accounts | List all accounts


# **add_metadata_to_account**
> add_metadata_to_account(ledger, account_id, metadata)

Add metadata to account

### Example


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


# Enter a context with an instance of the API client
with ledgerclient.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = accounts_api.AccountsApi(api_client)
    ledger = "ledger_example" # str | ledger
    account_id = "accountId_example" # str | accountId
    metadata = Metadata(
        key=None,
    ) # Metadata | metadata

    # example passing only required values which don't have defaults set
    try:
        # Add metadata to account
        api_instance.add_metadata_to_account(ledger, account_id, metadata)
    except ledgerclient.ApiException as e:
        print("Exception when calling AccountsApi->add_metadata_to_account: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ledger** | **str**| ledger |
 **account_id** | **str**| accountId |
 **metadata** | [**Metadata**](Metadata.md)| metadata |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Empty response |  -  |
**400** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_account**
> AccountResponse get_account(ledger, account_id)

Get account by address

### Example


```python
import time
import ledgerclient
from ledgerclient.api import accounts_api
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
    ledger = "ledger_example" # str | ledger
    account_id = "accountId_example" # str | accountId

    # example passing only required values which don't have defaults set
    try:
        # Get account by address
        api_response = api_instance.get_account(ledger, account_id)
        pprint(api_response)
    except ledgerclient.ApiException as e:
        print("Exception when calling AccountsApi->get_account: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ledger** | **str**| ledger |
 **account_id** | **str**| accountId |

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_accounts**
> AccountCursorResponse list_accounts(ledger)

List all accounts

### Example


```python
import time
import ledgerclient
from ledgerclient.api import accounts_api
from ledgerclient.model.account_cursor_response import AccountCursorResponse
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
    ledger = "ledger_example" # str | ledger
    after = "after_example" # str | pagination cursor, will return accounts after given address (in descending order) (optional)

    # example passing only required values which don't have defaults set
    try:
        # List all accounts
        api_response = api_instance.list_accounts(ledger)
        pprint(api_response)
    except ledgerclient.ApiException as e:
        print("Exception when calling AccountsApi->list_accounts: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List all accounts
        api_response = api_instance.list_accounts(ledger, after=after)
        pprint(api_response)
    except ledgerclient.ApiException as e:
        print("Exception when calling AccountsApi->list_accounts: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ledger** | **str**| ledger |
 **after** | **str**| pagination cursor, will return accounts after given address (in descending order) | [optional]

### Return type

[**AccountCursorResponse**](AccountCursorResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

