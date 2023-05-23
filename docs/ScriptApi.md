# ledgerclient.ScriptApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**run_script**](ScriptApi.md#run_script) | **POST** /{ledger}/script | Execute a Numscript


# **run_script**
> ScriptResponse run_script(ledger, script)

Execute a Numscript

This route is deprecated, and has been merged into `POST /{ledger}/transactions`. 

### Example


```python
import time
import ledgerclient
from ledgerclient.api import script_api
from ledgerclient.model.script_response import ScriptResponse
from ledgerclient.model.script import Script
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ledgerclient.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with ledgerclient.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = script_api.ScriptApi(api_client)
    ledger = "ledger001" # str | Name of the ledger.
    script = Script(
        plain='''vars {
account $user
}
send [COIN 10] (
	source = @world
	destination = $user
)
''',
        vars={},
        reference="order_1234",
        metadata=Metadata(
            key=None,
        ),
    ) # Script | 
    preview = True # bool | Set the preview mode. Preview mode doesn't add the logs to the database or publish a message to the message broker. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Execute a Numscript
        api_response = api_instance.run_script(ledger, script)
        pprint(api_response)
    except ledgerclient.ApiException as e:
        print("Exception when calling ScriptApi->run_script: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Execute a Numscript
        api_response = api_instance.run_script(ledger, script, preview=preview)
        pprint(api_response)
    except ledgerclient.ApiException as e:
        print("Exception when calling ScriptApi->run_script: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ledger** | **str**| Name of the ledger. |
 **script** | [**Script**](Script.md)|  |
 **preview** | **bool**| Set the preview mode. Preview mode doesn&#39;t add the logs to the database or publish a message to the message broker. | [optional]

### Return type

[**ScriptResponse**](ScriptResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | On success, it will return a 200 status code, and the resulting transaction under the &#x60;transaction&#x60; field.  On failure, it will also return a 200 status code, and the following fields:   - &#x60;details&#x60;: contains a URL. When there is an error parsing Numscript, the result can be difficult to read—the provided URL will render the error in an easy-to-read format.   - &#x60;errorCode&#x60; and &#x60;error_code&#x60; (deprecated): contains the string code of the error   - &#x60;errorMessage&#x60; and &#x60;error_message&#x60; (deprecated): contains a human-readable indication of what went wrong, for example that an account had insufficient funds, or that there was an error in the provided Numscript.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

