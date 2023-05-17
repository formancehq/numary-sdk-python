# ledgerclient.MappingApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_mapping**](MappingApi.md#get_mapping) | **GET** /{ledger}/mapping | Get the mapping of a ledger
[**update_mapping**](MappingApi.md#update_mapping) | **PUT** /{ledger}/mapping | Update the mapping of a ledger


# **get_mapping**
> MappingResponse get_mapping(ledger)

Get the mapping of a ledger

### Example


```python
import time
import ledgerclient
from ledgerclient.api import mapping_api
from ledgerclient.model.error_response import ErrorResponse
from ledgerclient.model.mapping_response import MappingResponse
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ledgerclient.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with ledgerclient.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = mapping_api.MappingApi(api_client)
    ledger = "ledger001" # str | Name of the ledger.

    # example passing only required values which don't have defaults set
    try:
        # Get the mapping of a ledger
        api_response = api_instance.get_mapping(ledger)
        pprint(api_response)
    except ledgerclient.ApiException as e:
        print("Exception when calling MappingApi->get_mapping: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ledger** | **str**| Name of the ledger. |

### Return type

[**MappingResponse**](MappingResponse.md)

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

# **update_mapping**
> MappingResponse update_mapping(ledger, mapping)

Update the mapping of a ledger

### Example


```python
import time
import ledgerclient
from ledgerclient.api import mapping_api
from ledgerclient.model.error_response import ErrorResponse
from ledgerclient.model.mapping import Mapping
from ledgerclient.model.mapping_response import MappingResponse
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ledgerclient.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with ledgerclient.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = mapping_api.MappingApi(api_client)
    ledger = "ledger001" # str | Name of the ledger.
    mapping = Mapping(
        contracts=[
            Contract(
                account="users:001",
                expr={},
            ),
        ],
    ) # Mapping | 

    # example passing only required values which don't have defaults set
    try:
        # Update the mapping of a ledger
        api_response = api_instance.update_mapping(ledger, mapping)
        pprint(api_response)
    except ledgerclient.ApiException as e:
        print("Exception when calling MappingApi->update_mapping: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ledger** | **str**| Name of the ledger. |
 **mapping** | [**Mapping**](Mapping.md)|  |

### Return type

[**MappingResponse**](MappingResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

