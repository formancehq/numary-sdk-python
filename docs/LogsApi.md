# ledgerclient.LogsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_logs**](LogsApi.md#list_logs) | **GET** /{ledger}/logs | List the logs from a ledger


# **list_logs**
> LogsCursorResponse list_logs(ledger)

List the logs from a ledger

List the logs from a ledger, sorted by ID in descending order.

### Example


```python
import time
import ledgerclient
from ledgerclient.api import logs_api
from ledgerclient.model.error_response import ErrorResponse
from ledgerclient.model.logs_cursor_response import LogsCursorResponse
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ledgerclient.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with ledgerclient.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = logs_api.LogsApi(api_client)
    ledger = "ledger001" # str | Name of the ledger.
    page_size = 100 # int | The maximum number of results to return per page.  (optional) if omitted the server will use the default value of 15
    page_size2 = 100 # int | The maximum number of results to return per page. Deprecated, please use `pageSize` instead.  (optional) if omitted the server will use the default value of 15
    after = "1234" # str | Pagination cursor, will return the logs after a given ID. (in descending order). (optional)
    start_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Filter transactions that occurred after this timestamp. The format is RFC3339 and is inclusive (for example, \"2023-01-02T15:04:01Z\" includes the first second of 4th minute).  (optional)
    start_time2 = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Filter transactions that occurred after this timestamp. The format is RFC3339 and is inclusive (for example, \"2023-01-02T15:04:01Z\" includes the first second of 4th minute). Deprecated, please use `startTime` instead.  (optional)
    end_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Filter transactions that occurred before this timestamp. The format is RFC3339 and is exclusive (for example, \"2023-01-02T15:04:01Z\" excludes the first second of 4th minute).  (optional)
    end_time2 = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Filter transactions that occurred before this timestamp. The format is RFC3339 and is exclusive (for example, \"2023-01-02T15:04:01Z\" excludes the first second of 4th minute). Deprecated, please use `endTime` instead.  (optional)
    cursor = "aHR0cHM6Ly9nLnBhZ2UvTmVrby1SYW1lbj9zaGFyZQ==" # str | Parameter used in pagination requests. Maximum page size is set to 15. Set to the value of next for the next page of results. Set to the value of previous for the previous page of results. No other parameters can be set when this parameter is set.  (optional)
    pagination_token = "aHR0cHM6Ly9nLnBhZ2UvTmVrby1SYW1lbj9zaGFyZQ==" # str | Parameter used in pagination requests. Maximum page size is set to 15. Set to the value of next for the next page of results. Set to the value of previous for the previous page of results. No other parameters can be set when this parameter is set. Deprecated, please use `cursor` instead.  (optional)

    # example passing only required values which don't have defaults set
    try:
        # List the logs from a ledger
        api_response = api_instance.list_logs(ledger)
        pprint(api_response)
    except ledgerclient.ApiException as e:
        print("Exception when calling LogsApi->list_logs: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List the logs from a ledger
        api_response = api_instance.list_logs(ledger, page_size=page_size, page_size2=page_size2, after=after, start_time=start_time, start_time2=start_time2, end_time=end_time, end_time2=end_time2, cursor=cursor, pagination_token=pagination_token)
        pprint(api_response)
    except ledgerclient.ApiException as e:
        print("Exception when calling LogsApi->list_logs: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ledger** | **str**| Name of the ledger. |
 **page_size** | **int**| The maximum number of results to return per page.  | [optional] if omitted the server will use the default value of 15
 **page_size2** | **int**| The maximum number of results to return per page. Deprecated, please use &#x60;pageSize&#x60; instead.  | [optional] if omitted the server will use the default value of 15
 **after** | **str**| Pagination cursor, will return the logs after a given ID. (in descending order). | [optional]
 **start_time** | **datetime**| Filter transactions that occurred after this timestamp. The format is RFC3339 and is inclusive (for example, \&quot;2023-01-02T15:04:01Z\&quot; includes the first second of 4th minute).  | [optional]
 **start_time2** | **datetime**| Filter transactions that occurred after this timestamp. The format is RFC3339 and is inclusive (for example, \&quot;2023-01-02T15:04:01Z\&quot; includes the first second of 4th minute). Deprecated, please use &#x60;startTime&#x60; instead.  | [optional]
 **end_time** | **datetime**| Filter transactions that occurred before this timestamp. The format is RFC3339 and is exclusive (for example, \&quot;2023-01-02T15:04:01Z\&quot; excludes the first second of 4th minute).  | [optional]
 **end_time2** | **datetime**| Filter transactions that occurred before this timestamp. The format is RFC3339 and is exclusive (for example, \&quot;2023-01-02T15:04:01Z\&quot; excludes the first second of 4th minute). Deprecated, please use &#x60;endTime&#x60; instead.  | [optional]
 **cursor** | **str**| Parameter used in pagination requests. Maximum page size is set to 15. Set to the value of next for the next page of results. Set to the value of previous for the previous page of results. No other parameters can be set when this parameter is set.  | [optional]
 **pagination_token** | **str**| Parameter used in pagination requests. Maximum page size is set to 15. Set to the value of next for the next page of results. Set to the value of previous for the previous page of results. No other parameters can be set when this parameter is set. Deprecated, please use &#x60;cursor&#x60; instead.  | [optional]

### Return type

[**LogsCursorResponse**](LogsCursorResponse.md)

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

