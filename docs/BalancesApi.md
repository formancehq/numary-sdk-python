# ledgerclient.BalancesApi

All URIs are relative to *https://.o.numary.cloud/ledger*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_balances**](BalancesApi.md#get_balances) | **GET** /{ledger}/balances | Get the balances from a ledger&#39;s account
[**get_balances_aggregated**](BalancesApi.md#get_balances_aggregated) | **GET** /{ledger}/aggregate/balances | Get the aggregated balances from selected accounts


# **get_balances**
> GetBalances200Response get_balances(ledger)

Get the balances from a ledger's account

### Example

* Basic Authentication (basicAuth):

```python
import time
import ledgerclient
from ledgerclient.api import balances_api
from ledgerclient.model.list_accounts400_response import ListAccounts400Response
from ledgerclient.model.get_balances200_response import GetBalances200Response
from pprint import pprint
# Defining the host is optional and defaults to https://.o.numary.cloud/ledger
# See configuration.py for a list of all supported configuration parameters.
configuration = ledgerclient.Configuration(
    host = "https://.o.numary.cloud/ledger"
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
    api_instance = balances_api.BalancesApi(api_client)
    ledger = "ledger001" # str | Name of the ledger.
    address = "users:001" # str | Filter balances involving given account, either as source or destination. (optional)
    after = "users:003" # str | Pagination cursor, will return accounts after given address, in descending order. (optional)
    pagination_token = "aHR0cHM6Ly9nLnBhZ2UvTmVrby1SYW1lbj9zaGFyZQ==" # str | Parameter used in pagination requests.  Set to the value of next for the next page of results.  Set to the value of previous for the previous page of results. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get the balances from a ledger's account
        api_response = api_instance.get_balances(ledger)
        pprint(api_response)
    except ledgerclient.ApiException as e:
        print("Exception when calling BalancesApi->get_balances: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get the balances from a ledger's account
        api_response = api_instance.get_balances(ledger, address=address, after=after, pagination_token=pagination_token)
        pprint(api_response)
    except ledgerclient.ApiException as e:
        print("Exception when calling BalancesApi->get_balances: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ledger** | **str**| Name of the ledger. |
 **address** | **str**| Filter balances involving given account, either as source or destination. | [optional]
 **after** | **str**| Pagination cursor, will return accounts after given address, in descending order. | [optional]
 **pagination_token** | **str**| Parameter used in pagination requests.  Set to the value of next for the next page of results.  Set to the value of previous for the previous page of results. | [optional]

### Return type

[**GetBalances200Response**](GetBalances200Response.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_balances_aggregated**
> GetBalancesAggregated200Response get_balances_aggregated(ledger)

Get the aggregated balances from selected accounts

### Example

* Basic Authentication (basicAuth):

```python
import time
import ledgerclient
from ledgerclient.api import balances_api
from ledgerclient.model.get_balances_aggregated200_response import GetBalancesAggregated200Response
from ledgerclient.model.get_balances_aggregated400_response import GetBalancesAggregated400Response
from pprint import pprint
# Defining the host is optional and defaults to https://.o.numary.cloud/ledger
# See configuration.py for a list of all supported configuration parameters.
configuration = ledgerclient.Configuration(
    host = "https://.o.numary.cloud/ledger"
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
    api_instance = balances_api.BalancesApi(api_client)
    ledger = "ledger001" # str | Name of the ledger.
    address = "users:001" # str | Filter balances involving given account, either as source or destination. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get the aggregated balances from selected accounts
        api_response = api_instance.get_balances_aggregated(ledger)
        pprint(api_response)
    except ledgerclient.ApiException as e:
        print("Exception when calling BalancesApi->get_balances_aggregated: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get the aggregated balances from selected accounts
        api_response = api_instance.get_balances_aggregated(ledger, address=address)
        pprint(api_response)
    except ledgerclient.ApiException as e:
        print("Exception when calling BalancesApi->get_balances_aggregated: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ledger** | **str**| Name of the ledger. |
 **address** | **str**| Filter balances involving given account, either as source or destination. | [optional]

### Return type

[**GetBalancesAggregated200Response**](GetBalancesAggregated200Response.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

