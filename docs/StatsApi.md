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


# Enter a context with an instance of the API client
with ledgerclient.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = stats_api.StatsApi(api_client)
    ledger = "ledger_example" # str | ledger

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
 **ledger** | **str**| ledger |

### Return type

[**StatsResponse**](StatsResponse.md)

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

