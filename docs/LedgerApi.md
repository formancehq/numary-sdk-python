# ledgerclient.LedgerApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_ledger_info**](LedgerApi.md#get_ledger_info) | **GET** /{ledger}/_info | Get information about a ledger


# **get_ledger_info**
> LedgerInfoResponse get_ledger_info(ledger)

Get information about a ledger

### Example


```python
import time
import ledgerclient
from ledgerclient.api import ledger_api
from ledgerclient.model.error_response import ErrorResponse
from ledgerclient.model.ledger_info_response import LedgerInfoResponse
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ledgerclient.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with ledgerclient.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = ledger_api.LedgerApi(api_client)
    ledger = "ledger001" # str | Name of the ledger.

    # example passing only required values which don't have defaults set
    try:
        # Get information about a ledger
        api_response = api_instance.get_ledger_info(ledger)
        pprint(api_response)
    except ledgerclient.ApiException as e:
        print("Exception when calling LedgerApi->get_ledger_info: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ledger** | **str**| Name of the ledger. |

### Return type

[**LedgerInfoResponse**](LedgerInfoResponse.md)

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

