# ledgerclient.ServerApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_info**](ServerApi.md#get_info) | **GET** /_info | Show server information


# **get_info**
> ConfigInfoResponse get_info()

Show server information

### Example


```python
import time
import ledgerclient
from ledgerclient.api import server_api
from ledgerclient.model.error_response import ErrorResponse
from ledgerclient.model.config_info_response import ConfigInfoResponse
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ledgerclient.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with ledgerclient.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = server_api.ServerApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Show server information
        api_response = api_instance.get_info()
        pprint(api_response)
    except ledgerclient.ApiException as e:
        print("Exception when calling ServerApi->get_info: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**ConfigInfoResponse**](ConfigInfoResponse.md)

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

