# ledgerclient.MappingApi

All URIs are relative to *https://.o.numary.cloud/ledger*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_mapping**](MappingApi.md#get_mapping) | **GET** /{ledger}/mapping | Get the mapping of a ledger.
[**update_mapping**](MappingApi.md#update_mapping) | **PUT** /{ledger}/mapping | Update the mapping of a ledger.


# **get_mapping**
> MappingResponse get_mapping(ledger)

Get the mapping of a ledger.

### Example

* Basic Authentication (basicAuth):

```python
import time
import ledgerclient
from ledgerclient.api import mapping_api
from ledgerclient.model.mapping_response import MappingResponse
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
    api_instance = mapping_api.MappingApi(api_client)
    ledger = "ledger001" # str | Name of the ledger.

    # example passing only required values which don't have defaults set
    try:
        # Get the mapping of a ledger.
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

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_mapping**
> MappingResponse update_mapping(ledger, mapping)

Update the mapping of a ledger.

### Example

* Basic Authentication (basicAuth):

```python
import time
import ledgerclient
from ledgerclient.api import mapping_api
from ledgerclient.model.mapping import Mapping
from ledgerclient.model.mapping_response import MappingResponse
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
        # Update the mapping of a ledger.
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

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

