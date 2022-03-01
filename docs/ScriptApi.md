# ledgerclient.ScriptApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**run_script**](ScriptApi.md#run_script) | **POST** /{ledger}/script | Execute Numscript


# **run_script**
> ScriptResult run_script(ledger, script)

Execute Numscript

Execute a Numscript and create the transaction if any

### Example

* Basic Authentication (basicAuth):
* Bearer Authentication (cloudToken):

```python
import time
import ledgerclient
from ledgerclient.api import script_api
from ledgerclient.model.script_result import ScriptResult
from ledgerclient.model.script import Script
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

# Configure Bearer authorization: cloudToken
configuration = ledgerclient.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with ledgerclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = script_api.ScriptApi(api_client)
    ledger = "ledger_example" # str | ledger
    script = Script(
        plain="plain_example",
        vars={},
    ) # Script | script
    preview = True # bool | Preview mode (optional)

    # example passing only required values which don't have defaults set
    try:
        # Execute Numscript
        api_response = api_instance.run_script(ledger, script)
        pprint(api_response)
    except ledgerclient.ApiException as e:
        print("Exception when calling ScriptApi->run_script: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Execute Numscript
        api_response = api_instance.run_script(ledger, script, preview=preview)
        pprint(api_response)
    except ledgerclient.ApiException as e:
        print("Exception when calling ScriptApi->run_script: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ledger** | **str**| ledger |
 **script** | [**Script**](Script.md)| script |
 **preview** | **bool**| Preview mode | [optional]

### Return type

[**ScriptResult**](ScriptResult.md)

### Authorization

[basicAuth](../README.md#basicAuth), [cloudToken](../README.md#cloudToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

