# ledgerclient.BalancesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_balances**](BalancesApi.md#get_balances) | **GET** /{ledger}/balances | Get the balances from a ledger&#39;s account
[**get_balances_aggregated**](BalancesApi.md#get_balances_aggregated) | **GET** /{ledger}/aggregate/balances | Get the aggregated balances from selected accounts


# **get_balances**
> BalancesCursorResponse get_balances(ledger)

Get the balances from a ledger's account

### Example


```python
import time
import ledgerclient
from ledgerclient.api import balances_api
from ledgerclient.model.error_response import ErrorResponse
from ledgerclient.model.balances_cursor_response import BalancesCursorResponse
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ledgerclient.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with ledgerclient.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = balances_api.BalancesApi(api_client)
    ledger = "ledger001" # str | Name of the ledger.
    address = "users:001" # str | Filter balances involving given account, either as source or destination. (optional)
    after = "users:003" # str | Pagination cursor, will return accounts after given address, in descending order. (optional)
    cursor = "aHR0cHM6Ly9nLnBhZ2UvTmVrby1SYW1lbj9zaGFyZQ==" # str | Parameter used in pagination requests. Maximum page size is set to 15. Set to the value of next for the next page of results. Set to the value of previous for the previous page of results. No other parameters can be set when this parameter is set.  (optional)
    pagination_token = "aHR0cHM6Ly9nLnBhZ2UvTmVrby1SYW1lbj9zaGFyZQ==" # str | Parameter used in pagination requests. Set to the value of next for the next page of results. Set to the value of previous for the previous page of results. Deprecated, please use `cursor` instead. (optional)

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
        api_response = api_instance.get_balances(ledger, address=address, after=after, cursor=cursor, pagination_token=pagination_token)
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
 **cursor** | **str**| Parameter used in pagination requests. Maximum page size is set to 15. Set to the value of next for the next page of results. Set to the value of previous for the previous page of results. No other parameters can be set when this parameter is set.  | [optional]
 **pagination_token** | **str**| Parameter used in pagination requests. Set to the value of next for the next page of results. Set to the value of previous for the previous page of results. Deprecated, please use &#x60;cursor&#x60; instead. | [optional]

### Return type

[**BalancesCursorResponse**](BalancesCursorResponse.md)

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

# **get_balances_aggregated**
> AggregateBalancesResponse get_balances_aggregated(ledger)

Get the aggregated balances from selected accounts

### Example


```python
import time
import ledgerclient
from ledgerclient.api import balances_api
from ledgerclient.model.error_response import ErrorResponse
from ledgerclient.model.aggregate_balances_response import AggregateBalancesResponse
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ledgerclient.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with ledgerclient.ApiClient() as api_client:
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

[**AggregateBalancesResponse**](AggregateBalancesResponse.md)

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

