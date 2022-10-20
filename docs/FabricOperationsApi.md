# swagger_client.FabricOperationsApi

All URIs are relative to *https://{{dcnm}}*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_config_fabric_backup_post**](FabricOperationsApi.md#rest_config_fabric_backup_post) | **POST** /rest/config/{fabric}/backup | fabric backup
[**rest_control_fabrics_fabric_delete**](FabricOperationsApi.md#rest_control_fabrics_fabric_delete) | **DELETE** /rest/control/fabrics/{fabric} | delete fabric
[**rest_control_fabrics_fabric_get**](FabricOperationsApi.md#rest_control_fabrics_fabric_get) | **GET** /rest/control/fabrics/{fabric} | get single fabric
[**rest_control_fabrics_fabric_id_number_inventory_discover_post**](FabricOperationsApi.md#rest_control_fabrics_fabric_id_number_inventory_discover_post) | **POST** /rest/control/fabrics/{fabric_id_number}/inventory/discover | register switch
[**rest_control_fabrics_fabric_id_number_inventory_test_reachability_post**](FabricOperationsApi.md#rest_control_fabrics_fabric_id_number_inventory_test_reachability_post) | **POST** /rest/control/fabrics/{fabric_id_number}/inventory/test-reachability | discover switches
[**rest_control_fabrics_fabric_inventory_get**](FabricOperationsApi.md#rest_control_fabrics_fabric_inventory_get) | **GET** /rest/control/fabrics/{fabric}/inventory | get fabric inventory
[**rest_control_fabrics_fabric_put**](FabricOperationsApi.md#rest_control_fabrics_fabric_put) | **PUT** /rest/control/fabrics/{fabric} | modify fabric
[**rest_control_fabrics_fabric_switches9_uncwexete8_delete**](FabricOperationsApi.md#rest_control_fabrics_fabric_switches9_uncwexete8_delete) | **DELETE** /rest/control/fabrics/{fabric}/switches/9UNCWEXETE8 | delete switch
[**rest_control_fabrics_get**](FabricOperationsApi.md#rest_control_fabrics_get) | **GET** /rest/control/fabrics | get all fabrics
[**rest_control_fabrics_post**](FabricOperationsApi.md#rest_control_fabrics_post) | **POST** /rest/control/fabrics | create fabric

# **rest_config_fabric_backup_post**
> rest_config_fabric_backup_post(fabric, body=body, dcnm_token=dcnm_token, content_type=content_type, tag=tag)

fabric backup

Creates a snapshot backup of the fabric named within the URI with a given user-defined tag

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FabricOperationsApi()
fabric = 'fabric_example' # str | 
body = 'body_example' # str |  (optional)
dcnm_token = 'dcnm_token_example' # str |  (optional)
content_type = 'content_type_example' # str |  (optional)
tag = 'tag_example' # str |  (optional)

try:
    # fabric backup
    api_instance.rest_config_fabric_backup_post(fabric, body=body, dcnm_token=dcnm_token, content_type=content_type, tag=tag)
except ApiException as e:
    print("Exception when calling FabricOperationsApi->rest_config_fabric_backup_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fabric** | **str**|  | 
 **body** | [**str**](str.md)|  | [optional] 
 **dcnm_token** | **str**|  | [optional] 
 **content_type** | **str**|  | [optional] 
 **tag** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_control_fabrics_fabric_delete**
> rest_control_fabrics_fabric_delete(fabric, accept=accept, dcnm_token=dcnm_token)

delete fabric

Removes fabric named in the URI from DCNM

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FabricOperationsApi()
fabric = 'fabric_example' # str | 
accept = 'accept_example' # str |  (optional)
dcnm_token = 'dcnm_token_example' # str |  (optional)

try:
    # delete fabric
    api_instance.rest_control_fabrics_fabric_delete(fabric, accept=accept, dcnm_token=dcnm_token)
except ApiException as e:
    print("Exception when calling FabricOperationsApi->rest_control_fabrics_fabric_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fabric** | **str**|  | 
 **accept** | **str**|  | [optional] 
 **dcnm_token** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_control_fabrics_fabric_get**
> rest_control_fabrics_fabric_get(fabric, accept=accept, dcnm_token=dcnm_token)

get single fabric

Lists the fabric details for the queried fabric.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FabricOperationsApi()
fabric = 'fabric_example' # str | 
accept = 'accept_example' # str |  (optional)
dcnm_token = 'dcnm_token_example' # str |  (optional)

try:
    # get single fabric
    api_instance.rest_control_fabrics_fabric_get(fabric, accept=accept, dcnm_token=dcnm_token)
except ApiException as e:
    print("Exception when calling FabricOperationsApi->rest_control_fabrics_fabric_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fabric** | **str**|  | 
 **accept** | **str**|  | [optional] 
 **dcnm_token** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_control_fabrics_fabric_id_number_inventory_discover_post**
> rest_control_fabrics_fabric_id_number_inventory_discover_post(fabric_id_number, body=body, dcnm_token=dcnm_token, accept=accept)

register switch

Uses the reachability information as a payload to register switches as members of the fabric named within the URI.  All switches will be added as `leaf` nodes, which may require some reassignment using another API endpoint.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FabricOperationsApi()
fabric_id_number = 'fabric_id_number_example' # str | 
body = NULL # object |  (optional)
dcnm_token = 'dcnm_token_example' # str |  (optional)
accept = 'accept_example' # str |  (optional)

try:
    # register switch
    api_instance.rest_control_fabrics_fabric_id_number_inventory_discover_post(fabric_id_number, body=body, dcnm_token=dcnm_token, accept=accept)
except ApiException as e:
    print("Exception when calling FabricOperationsApi->rest_control_fabrics_fabric_id_number_inventory_discover_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fabric_id_number** | **str**|  | 
 **body** | [**object**](object.md)|  | [optional] 
 **dcnm_token** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_control_fabrics_fabric_id_number_inventory_test_reachability_post**
> rest_control_fabrics_fabric_id_number_inventory_test_reachability_post(fabric_id_number, body=body, content_type=content_type, dcnm_token=dcnm_token)

discover switches

Used to find switches within a given network to be added into DCNM inventory for a specific fabric. Options in payload are similar to Fabric Builder UI, in which a `seed IP`, `number of hops`, and device credentials are given for DCNM to \"walk\" through.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FabricOperationsApi()
fabric_id_number = 'fabric_id_number_example' # str | 
body = 'body_example' # str |  (optional)
content_type = 'content_type_example' # str |  (optional)
dcnm_token = 'dcnm_token_example' # str |  (optional)

try:
    # discover switches
    api_instance.rest_control_fabrics_fabric_id_number_inventory_test_reachability_post(fabric_id_number, body=body, content_type=content_type, dcnm_token=dcnm_token)
except ApiException as e:
    print("Exception when calling FabricOperationsApi->rest_control_fabrics_fabric_id_number_inventory_test_reachability_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fabric_id_number** | **str**|  | 
 **body** | [**str**](str.md)|  | [optional] 
 **content_type** | **str**|  | [optional] 
 **dcnm_token** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_control_fabrics_fabric_inventory_get**
> rest_control_fabrics_fabric_inventory_get(fabric, accept=accept, dcnm_token=dcnm_token)

get fabric inventory

Gets all information for all devices that are part of the fabric named in the URI, including both DCNM as well as hardware specific facts.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FabricOperationsApi()
fabric = 'fabric_example' # str | 
accept = 'accept_example' # str |  (optional)
dcnm_token = 'dcnm_token_example' # str |  (optional)

try:
    # get fabric inventory
    api_instance.rest_control_fabrics_fabric_inventory_get(fabric, accept=accept, dcnm_token=dcnm_token)
except ApiException as e:
    print("Exception when calling FabricOperationsApi->rest_control_fabrics_fabric_inventory_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fabric** | **str**|  | 
 **accept** | **str**|  | [optional] 
 **dcnm_token** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_control_fabrics_fabric_put**
> rest_control_fabrics_fabric_put(fabric, body=body, accept=accept, dcnm_token=dcnm_token)

modify fabric

Used to modify an existing fabric with the desired nv pairs in the payload.  Can use similar payload to that used for creating a fabric.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FabricOperationsApi()
fabric = 'fabric_example' # str | 
body = NULL # object |  (optional)
accept = 'accept_example' # str |  (optional)
dcnm_token = 'dcnm_token_example' # str |  (optional)

try:
    # modify fabric
    api_instance.rest_control_fabrics_fabric_put(fabric, body=body, accept=accept, dcnm_token=dcnm_token)
except ApiException as e:
    print("Exception when calling FabricOperationsApi->rest_control_fabrics_fabric_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fabric** | **str**|  | 
 **body** | [**object**](object.md)|  | [optional] 
 **accept** | **str**|  | [optional] 
 **dcnm_token** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_control_fabrics_fabric_switches9_uncwexete8_delete**
> rest_control_fabrics_fabric_switches9_uncwexete8_delete(fabric, dcnm_token=dcnm_token)

delete switch

Removes switch (named by serial) in the URI from the fabric

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FabricOperationsApi()
fabric = 'fabric_example' # str | 
dcnm_token = 'dcnm_token_example' # str |  (optional)

try:
    # delete switch
    api_instance.rest_control_fabrics_fabric_switches9_uncwexete8_delete(fabric, dcnm_token=dcnm_token)
except ApiException as e:
    print("Exception when calling FabricOperationsApi->rest_control_fabrics_fabric_switches9_uncwexete8_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fabric** | **str**|  | 
 **dcnm_token** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_control_fabrics_get**
> rest_control_fabrics_get(accept=accept, dcnm_token=dcnm_token)

get all fabrics

Queries DCNM for all facts and information about all configured fabrics within the inventory

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FabricOperationsApi()
accept = 'accept_example' # str |  (optional)
dcnm_token = 'dcnm_token_example' # str |  (optional)

try:
    # get all fabrics
    api_instance.rest_control_fabrics_get(accept=accept, dcnm_token=dcnm_token)
except ApiException as e:
    print("Exception when calling FabricOperationsApi->rest_control_fabrics_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept** | **str**|  | [optional] 
 **dcnm_token** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_control_fabrics_post**
> rest_control_fabrics_post(body=body, accept=accept, dcnm_token=dcnm_token)

create fabric

Creates a new fabric with the specific nv pairs defined within the payload.  These values mimic the names/values that would be applied through the DCNM Fabric Builder UI.  To obtain a payload for this deployment, the API-Tool within DCNM can watch the request through the UI and give the applicable call and payload for reuse/modification later.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FabricOperationsApi()
body = NULL # object |  (optional)
accept = 'accept_example' # str |  (optional)
dcnm_token = 'dcnm_token_example' # str |  (optional)

try:
    # create fabric
    api_instance.rest_control_fabrics_post(body=body, accept=accept, dcnm_token=dcnm_token)
except ApiException as e:
    print("Exception when calling FabricOperationsApi->rest_control_fabrics_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**object**](object.md)|  | [optional] 
 **accept** | **str**|  | [optional] 
 **dcnm_token** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

