<a name="__pageTop"></a>
# ledgerclient.apis.tags.script_api.ScriptApi

All URIs are relative to *https://.o.numary.cloud/ledger*

Method | HTTP request | Description
------------- | ------------- | -------------
[**run_script**](#run_script) | **post** /{ledger}/script | Execute a Numscript.

# **run_script**
<a name="run_script"></a>
> ScriptResult run_script(ledgerscript)

Execute a Numscript.

### Example

* Basic Authentication (basicAuth):
```python
import ledgerclient
from ledgerclient.apis.tags import script_api
from ledgerclient.model.script_result import ScriptResult
from ledgerclient.model.script import Script
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
    api_instance = script_api.ScriptApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'ledger': "ledger001",
    }
    query_params = {
    }
    body = Script(
        reference="order_1234",
        metadata=Metadata(
            key=None,
        ),
        plain="vars {\naccount $user\n}\nsend [COIN 10] (\n\tsource = @world\n\tdestination = $user\n)\n",
        vars=dict(),
    )
    try:
        # Execute a Numscript.
        api_response = api_instance.run_script(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except ledgerclient.ApiException as e:
        print("Exception when calling ScriptApi->run_script: %s\n" % e)

    # example passing only optional values
    path_params = {
        'ledger': "ledger001",
    }
    query_params = {
        'preview': True,
    }
    body = Script(
        reference="order_1234",
        metadata=Metadata(
            key=None,
        ),
        plain="vars {\naccount $user\n}\nsend [COIN 10] (\n\tsource = @world\n\tdestination = $user\n)\n",
        vars=dict(),
    )
    try:
        # Execute a Numscript.
        api_response = api_instance.run_script(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except ledgerclient.ApiException as e:
        print("Exception when calling ScriptApi->run_script: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Script**](../../models/Script.md) |  | 


### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
preview | PreviewSchema | | optional


# PreviewSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
ledger | LedgerSchema | | 

# LedgerSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#run_script.ApiResponseFor200) | OK

#### run_script.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ScriptResult**](../../models/ScriptResult.md) |  | 


### Authorization

[basicAuth](../../../README.md#basicAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

