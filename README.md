# ledgerclient
No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: v1.9.0-rc.10
- Package version: v1.9.0-rc.10
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python &gt;&#x3D;3.7

## Migration from other generators like python and python-legacy

### Changes
1. This generator uses spec case for all (object) property names and parameter names.
    - So if the spec has a property name like camelCase, it will use camelCase rather than camel_case
    - So you will need to update how you input and read properties to use spec case
2. Endpoint parameters are stored in dictionaries to prevent collisions (explanation below)
    - So you will need to update how you pass data in to endpoints
3. Endpoint responses now include the original response, the deserialized response body, and (todo)the deserialized headers
    - So you will need to update your code to use response.body to access deserialized data
4. All validated data is instantiated in an instance that subclasses all validated Schema classes and Decimal/str/list/tuple/frozendict/NoneClass/BoolClass/bytes/io.FileIO
    - This means that you can use isinstance to check if a payload validated against a schema class
    - This means that no data will be of type None/True/False
        - ingested None will subclass NoneClass
        - ingested True will subclass BoolClass
        - ingested False will subclass BoolClass
        - So if you need to check is True/False/None, instead use instance.is_true_oapg()/.is_false_oapg()/.is_none_oapg()
5. All validated class instances are immutable except for ones based on io.File
    - This is because if properties were changed after validation, that validation would no longer apply
    - So no changing values or property values after a class has been instantiated
6. String + Number types with formats
    - String type data is stored as a string and if you need to access types based on its format like date,
    date-time, uuid, number etc then you will need to use accessor functions on the instance
    - type string + format: See .as_date_oapg, .as_datetime_oapg, .as_decimal_oapg, .as_uuid_oapg
    - type number + format: See .as_float_oapg, .as_int_oapg
    - this was done because openapi/json-schema defines constraints. string data may be type string with no format
    keyword in one schema, and include a format constraint in another schema
    - So if you need to access a string format based type, use as_date_oapg/as_datetime_oapg/as_decimal_oapg/as_uuid_oapg
    - So if you need to access a number format based type, use as_int_oapg/as_float_oapg
7. Property access on AnyType(type unset) or object(dict) schemas
    - Only required keys with valid python names are properties like .someProp and have type hints
    - All optional keys may not exist, so properties are not defined for them
    - One can access optional values with dict_instance['optionalProp'] and KeyError will be raised if it does not exist
    - Use get_item_oapg if you need a way to always get a value whether or not the key exists
        - If the key does not exist, schemas.unset is returned from calling dict_instance.get_item_oapg('optionalProp')
        - All required and optional keys have type hints for this method, and @typing.overload is used
        - A type hint is also generated for additionalProperties accessed using this method
    - So you will need to update you code to use some_instance['optionalProp'] to access optional property
    and additionalProperty values
8. The location of the api classes has changed
    - Api classes are located in your_package.apis.tags.some_api
    - This change was made to eliminate redundant code generation
    - Legacy generators generated the same endpoint twice if it had > 1 tag on it
    - This generator defines an endpoint in one class, then inherits that class to generate
      apis by tags and by paths
    - This change reduces code and allows quicker run time if you use the path apis
        - path apis are at your_package.apis.paths.some_path
    - Those apis will only load their needed models, which is less to load than all of the resources needed in a tag api
    - So you will need to update your import paths to the api classes

### Why are Oapg and _oapg used in class and method names?
Classes can have arbitrarily named properties set on them
Endpoints can have arbitrary operationId method names set
For those reasons, I use the prefix Oapg and _oapg to greatly reduce the likelihood of collisions
on protected + public classes/methods.
oapg stands for OpenApi Python Generator.

### Object property spec case
This was done because when payloads are ingested, they can be validated against N number of schemas.
If the input signature used a different property name then that has mutated the payload.
So SchemaA and SchemaB must both see the camelCase spec named variable.
Also it is possible to send in two properties, named camelCase and camel_case in the same payload.
That use case should be support so spec case is used.

### Parameter spec case
Parameters can be included in different locations including:
- query
- path
- header
- cookie

Any of those parameters could use the same parameter names, so if every parameter
was included as an endpoint parameter in a function signature, they would collide.
For that reason, each of those inputs have been separated out into separate typed dictionaries:
- query_params
- path_params
- header_params
- cookie_params

So when updating your code, you will need to pass endpoint parameters in using those
dictionaries.

### Endpoint responses
Endpoint responses have been enriched to now include more information.
Any response reom an endpoint will now include the following properties:
response: urllib3.HTTPResponse
body: typing.Union[Unset, Schema]
headers: typing.Union[Unset, TODO]
Note: response header deserialization has not yet been added


## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/formancehq/numary-sdk-python.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/formancehq/numary-sdk-python.git`)

Then import the package:
```python
import ledgerclient
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import ledgerclient
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import time
import ledgerclient
from pprint import pprint
from ledgerclient.apis.tags import accounts_api
from ledgerclient.model.account_response import AccountResponse
from ledgerclient.model.accounts_cursor_response import AccountsCursorResponse
from ledgerclient.model.error_response import ErrorResponse
from ledgerclient.model.metadata import Metadata
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ledgerclient.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with ledgerclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = accounts_api.AccountsApi(api_client)
    ledger = "ledger001" # str | Name of the ledger.
address = "users:001" # str | Exact address of the account. It must match the following regular expressions pattern: ``` ^\\w+(:\\w+)*$ ``` 
metadata = Metadata(
        key=None,
    ) # Metadata | metadata

    try:
        # Add metadata to an account
        api_instance.add_metadata_to_account(ledgeraddressmetadata)
    except ledgerclient.ApiException as e:
        print("Exception when calling AccountsApi->add_metadata_to_account: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *http://localhost*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AccountsApi* | [**add_metadata_to_account**](docs/apis/tags/AccountsApi.md#add_metadata_to_account) | **post** /{ledger}/accounts/{address}/metadata | Add metadata to an account
*AccountsApi* | [**count_accounts**](docs/apis/tags/AccountsApi.md#count_accounts) | **head** /{ledger}/accounts | Count the accounts from a ledger
*AccountsApi* | [**get_account**](docs/apis/tags/AccountsApi.md#get_account) | **get** /{ledger}/accounts/{address} | Get account by its address
*AccountsApi* | [**list_accounts**](docs/apis/tags/AccountsApi.md#list_accounts) | **get** /{ledger}/accounts | List accounts from a ledger
*BalancesApi* | [**get_balances**](docs/apis/tags/BalancesApi.md#get_balances) | **get** /{ledger}/balances | Get the balances from a ledger&#x27;s account
*BalancesApi* | [**get_balances_aggregated**](docs/apis/tags/BalancesApi.md#get_balances_aggregated) | **get** /{ledger}/aggregate/balances | Get the aggregated balances from selected accounts
*LedgerApi* | [**get_ledger_info**](docs/apis/tags/LedgerApi.md#get_ledger_info) | **get** /{ledger}/_info | Get information about a ledger
*LogsApi* | [**list_logs**](docs/apis/tags/LogsApi.md#list_logs) | **get** /{ledger}/logs | List the logs from a ledger
*MappingApi* | [**get_mapping**](docs/apis/tags/MappingApi.md#get_mapping) | **get** /{ledger}/mapping | Get the mapping of a ledger
*MappingApi* | [**update_mapping**](docs/apis/tags/MappingApi.md#update_mapping) | **put** /{ledger}/mapping | Update the mapping of a ledger
*ScriptApi* | [**run_script**](docs/apis/tags/ScriptApi.md#run_script) | **post** /{ledger}/script | Execute a Numscript
*ServerApi* | [**get_info**](docs/apis/tags/ServerApi.md#get_info) | **get** /_info | Show server information
*StatsApi* | [**read_stats**](docs/apis/tags/StatsApi.md#read_stats) | **get** /{ledger}/stats | Get statistics from a ledger
*TransactionsApi* | [**add_metadata_on_transaction**](docs/apis/tags/TransactionsApi.md#add_metadata_on_transaction) | **post** /{ledger}/transactions/{txid}/metadata | Set the metadata of a transaction by its ID
*TransactionsApi* | [**count_transactions**](docs/apis/tags/TransactionsApi.md#count_transactions) | **head** /{ledger}/transactions | Count the transactions from a ledger
*TransactionsApi* | [**create_transaction**](docs/apis/tags/TransactionsApi.md#create_transaction) | **post** /{ledger}/transactions | Create a new transaction to a ledger
*TransactionsApi* | [**create_transactions**](docs/apis/tags/TransactionsApi.md#create_transactions) | **post** /{ledger}/transactions/batch | Create a new batch of transactions to a ledger
*TransactionsApi* | [**get_transaction**](docs/apis/tags/TransactionsApi.md#get_transaction) | **get** /{ledger}/transactions/{txid} | Get transaction from a ledger by its ID
*TransactionsApi* | [**list_transactions**](docs/apis/tags/TransactionsApi.md#list_transactions) | **get** /{ledger}/transactions | List transactions from a ledger
*TransactionsApi* | [**revert_transaction**](docs/apis/tags/TransactionsApi.md#revert_transaction) | **post** /{ledger}/transactions/{txid}/revert | Revert a ledger transaction by its ID

## Documentation For Models

 - [Account](docs/models/Account.md)
 - [AccountResponse](docs/models/AccountResponse.md)
 - [AccountWithVolumesAndBalances](docs/models/AccountWithVolumesAndBalances.md)
 - [AccountsBalances](docs/models/AccountsBalances.md)
 - [AccountsCursorResponse](docs/models/AccountsCursorResponse.md)
 - [AggregateBalancesResponse](docs/models/AggregateBalancesResponse.md)
 - [AggregatedVolumes](docs/models/AggregatedVolumes.md)
 - [AssetsBalances](docs/models/AssetsBalances.md)
 - [BalancesCursorResponse](docs/models/BalancesCursorResponse.md)
 - [Config](docs/models/Config.md)
 - [ConfigInfo](docs/models/ConfigInfo.md)
 - [ConfigInfoResponse](docs/models/ConfigInfoResponse.md)
 - [Contract](docs/models/Contract.md)
 - [ErrorResponse](docs/models/ErrorResponse.md)
 - [ErrorsEnum](docs/models/ErrorsEnum.md)
 - [LedgerInfo](docs/models/LedgerInfo.md)
 - [LedgerInfoResponse](docs/models/LedgerInfoResponse.md)
 - [LedgerStorage](docs/models/LedgerStorage.md)
 - [Log](docs/models/Log.md)
 - [LogsCursorResponse](docs/models/LogsCursorResponse.md)
 - [Mapping](docs/models/Mapping.md)
 - [MappingResponse](docs/models/MappingResponse.md)
 - [Metadata](docs/models/Metadata.md)
 - [MigrationInfo](docs/models/MigrationInfo.md)
 - [PostTransaction](docs/models/PostTransaction.md)
 - [Posting](docs/models/Posting.md)
 - [Script](docs/models/Script.md)
 - [ScriptResponse](docs/models/ScriptResponse.md)
 - [Stats](docs/models/Stats.md)
 - [StatsResponse](docs/models/StatsResponse.md)
 - [Transaction](docs/models/Transaction.md)
 - [TransactionData](docs/models/TransactionData.md)
 - [TransactionResponse](docs/models/TransactionResponse.md)
 - [Transactions](docs/models/Transactions.md)
 - [TransactionsCursorResponse](docs/models/TransactionsCursorResponse.md)
 - [TransactionsResponse](docs/models/TransactionsResponse.md)
 - [Volume](docs/models/Volume.md)
 - [Volumes](docs/models/Volumes.md)

## Documentation For Authorization

 All endpoints do not require authorization.

## Author

support@numary.com
support@numary.com
support@numary.com
support@numary.com
support@numary.com
support@numary.com
support@numary.com
support@numary.com
support@numary.com

## Notes for Large OpenAPI documents
If the OpenAPI document is large, imports in ledgerclient.apis and ledgerclient.models may fail with a
RecursionError indicating the maximum recursion limit has been exceeded. In that case, there are a couple of solutions:

Solution 1:
Use specific imports for apis and models like:
- `from ledgerclient.apis.default_api import DefaultApi`
- `from ledgerclient.model.pet import Pet`

Solution 1:
Before importing the package, adjust the maximum recursion limit as shown below:
```
import sys
sys.setrecursionlimit(1500)
import ledgerclient
from ledgerclient.apis import *
from ledgerclient.models import *
```
