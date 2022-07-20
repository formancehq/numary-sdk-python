# ledgerclient.StatsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**read_stats**](StatsApi.md#read_stats) | **GET** /{ledger}/stats | Get Stats


# **read_stats**
> StatsResponse read_stats(ledger)

Get Stats

Get ledger stats (aggregate metrics on accounts and transactions) The stats for account

### Example

* Basic Authentication (basicAuth):

```python
import time
import ledgerclient
from ledgerclient.api import stats_api
from ledgerclient.model.stats_response import StatsResponse
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
    api_instance = stats_api.StatsApi(api_client)
    ledger = "ledger001" # str | name of the ledger

    # example passing only required values which don't have defaults set
    try:
        # Get Stats
        api_response = api_instance.read_stats(ledger)
        pprint(api_response)
    except ledgerclient.ApiException as e:
        print("Exception when calling StatsApi->read_stats: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ledger** | **str**| name of the ledger |

### Return type

[**StatsResponse**](StatsResponse.md)

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

