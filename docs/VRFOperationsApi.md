# swagger_client.VRFOperationsApi

All URIs are relative to *https://{{dcnm}}*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_managed_pool_fabrics_fabric_partitions_ids_post**](VRFOperationsApi.md#rest_managed_pool_fabrics_fabric_partitions_ids_post) | **POST** /rest/managed-pool/fabrics/{fabric}/partitions/ids | get vrf segment id
[**rest_resource_manager_reserve_id_post**](VRFOperationsApi.md#rest_resource_manager_reserve_id_post) | **POST** /rest/resource-manager/reserve-id | get vrf lite dot1q id
[**rest_resource_manager_vlan_fabric_get**](VRFOperationsApi.md#rest_resource_manager_vlan_fabric_get) | **GET** /rest/resource-manager/vlan/{fabric} | get proposed vrf vlan
[**rest_top_down_fabrics_fabric_vrfs_attachments_get**](VRFOperationsApi.md#rest_top_down_fabrics_fabric_vrfs_attachments_get) | **GET** /rest/top-down/fabrics/{fabric}/vrfs/attachments | query vrf attachments
[**rest_top_down_fabrics_fabric_vrfs_attachments_post**](VRFOperationsApi.md#rest_top_down_fabrics_fabric_vrfs_attachments_post) | **POST** /rest/top-down/fabrics/{fabric}/vrfs/attachments | create multi-site extension attachment
[**rest_top_down_fabrics_fabric_vrfs_deployments_post**](VRFOperationsApi.md#rest_top_down_fabrics_fabric_vrfs_deployments_post) | **POST** /rest/top-down/fabrics/{fabric}/vrfs/deployments | deploy vrf
[**rest_top_down_fabrics_fabric_vrfs_get**](VRFOperationsApi.md#rest_top_down_fabrics_fabric_vrfs_get) | **GET** /rest/top-down/fabrics/{fabric}/vrfs | query vrf
[**rest_top_down_fabrics_fabric_vrfs_post**](VRFOperationsApi.md#rest_top_down_fabrics_fabric_vrfs_post) | **POST** /rest/top-down/fabrics/{fabric}/vrfs | create vrf
[**rest_top_down_fabrics_fabric_vrfs_switches_get**](VRFOperationsApi.md#rest_top_down_fabrics_fabric_vrfs_switches_get) | **GET** /rest/top-down/fabrics/{fabric}/vrfs/switches | get switch details by vrf
[**rest_top_down_fabrics_fabric_vrfs_vrf_delete**](VRFOperationsApi.md#rest_top_down_fabrics_fabric_vrfs_vrf_delete) | **DELETE** /rest/top-down/fabrics/{fabric}/vrfs/{vrf} | delete vrf
[**rest_top_down_fabrics_fabric_vrfs_vrf_put**](VRFOperationsApi.md#rest_top_down_fabrics_fabric_vrfs_vrf_put) | **PUT** /rest/top-down/fabrics/{fabric}/vrfs/{vrf} | update vrf

# **rest_managed_pool_fabrics_fabric_partitions_ids_post**
> rest_managed_pool_fabrics_fabric_partitions_ids_post(fabric, dcnm_token=dcnm_token, content_type=content_type)

get vrf segment id

Uses DCNM resource manager to obtain a VRF segment ID value for tracking.  JS tests insert this into the `{{ vrf_id_number }}` ENV var

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.VRFOperationsApi()
fabric = 'fabric_example' # str | 
dcnm_token = 'dcnm_token_example' # str |  (optional)
content_type = 'content_type_example' # str |  (optional)

try:
    # get vrf segment id
    api_instance.rest_managed_pool_fabrics_fabric_partitions_ids_post(fabric, dcnm_token=dcnm_token, content_type=content_type)
except ApiException as e:
    print("Exception when calling VRFOperationsApi->rest_managed_pool_fabrics_fabric_partitions_ids_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fabric** | **str**|  | 
 **dcnm_token** | **str**|  | [optional] 
 **content_type** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_resource_manager_reserve_id_post**
> rest_resource_manager_reserve_id_post(body=body, dcnm_token=dcnm_token, content_type=content_type)

get vrf lite dot1q id

Uses the DCNM resource manager to gather an unused 802.1q VLAN ID for use in the VRF for peering purposes.  JS test inserts this value after completion into the `{{ vrf_dot1q_vlan }}` ENV var

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.VRFOperationsApi()
body = NULL # object |  (optional)
dcnm_token = 'dcnm_token_example' # str |  (optional)
content_type = 'content_type_example' # str |  (optional)

try:
    # get vrf lite dot1q id
    api_instance.rest_resource_manager_reserve_id_post(body=body, dcnm_token=dcnm_token, content_type=content_type)
except ApiException as e:
    print("Exception when calling VRFOperationsApi->rest_resource_manager_reserve_id_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**object**](object.md)|  | [optional] 
 **dcnm_token** | **str**|  | [optional] 
 **content_type** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_resource_manager_vlan_fabric_get**
> rest_resource_manager_vlan_fabric_get(fabric, dcnm_token=dcnm_token, vlan_usage_type=vlan_usage_type)

get proposed vrf vlan

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.VRFOperationsApi()
fabric = 'fabric_example' # str | 
dcnm_token = 'dcnm_token_example' # str |  (optional)
vlan_usage_type = 'vlan_usage_type_example' # str |  (optional)

try:
    # get proposed vrf vlan
    api_instance.rest_resource_manager_vlan_fabric_get(fabric, dcnm_token=dcnm_token, vlan_usage_type=vlan_usage_type)
except ApiException as e:
    print("Exception when calling VRFOperationsApi->rest_resource_manager_vlan_fabric_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fabric** | **str**|  | 
 **dcnm_token** | **str**|  | [optional] 
 **vlan_usage_type** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_top_down_fabrics_fabric_vrfs_attachments_get**
> rest_top_down_fabrics_fabric_vrfs_attachments_get(fabric, dcnm_token=dcnm_token, content_type=content_type, vrf_names=vrf_names)

query vrf attachments

Used to list all the attached switches and deployment status in the given VRFs

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.VRFOperationsApi()
fabric = 'fabric_example' # str | 
dcnm_token = 'dcnm_token_example' # str |  (optional)
content_type = 'content_type_example' # str |  (optional)
vrf_names = 'vrf_names_example' # str |  (optional)

try:
    # query vrf attachments
    api_instance.rest_top_down_fabrics_fabric_vrfs_attachments_get(fabric, dcnm_token=dcnm_token, content_type=content_type, vrf_names=vrf_names)
except ApiException as e:
    print("Exception when calling VRFOperationsApi->rest_top_down_fabrics_fabric_vrfs_attachments_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fabric** | **str**|  | 
 **dcnm_token** | **str**|  | [optional] 
 **content_type** | **str**|  | [optional] 
 **vrf_names** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_top_down_fabrics_fabric_vrfs_attachments_post**
> rest_top_down_fabrics_fabric_vrfs_attachments_post(fabric, body=body, dcnm_token=dcnm_token, content_type=content_type)

create multi-site extension attachment

This specific payload creates a multi-site extension VRF switch attachment within DCNM

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.VRFOperationsApi()
fabric = 'fabric_example' # str | 
body = 'body_example' # str |  (optional)
dcnm_token = 'dcnm_token_example' # str |  (optional)
content_type = 'content_type_example' # str |  (optional)

try:
    # create multi-site extension attachment
    api_instance.rest_top_down_fabrics_fabric_vrfs_attachments_post(fabric, body=body, dcnm_token=dcnm_token, content_type=content_type)
except ApiException as e:
    print("Exception when calling VRFOperationsApi->rest_top_down_fabrics_fabric_vrfs_attachments_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fabric** | **str**|  | 
 **body** | [**str**](str.md)|  | [optional] 
 **dcnm_token** | **str**|  | [optional] 
 **content_type** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_top_down_fabrics_fabric_vrfs_deployments_post**
> rest_top_down_fabrics_fabric_vrfs_deployments_post(fabric, body=body, dcnm_token=dcnm_token, content_type=content_type)

deploy vrf

Deploys the previously created VRF to the fabric defined in the URI

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.VRFOperationsApi()
fabric = 'fabric_example' # str | 
body = NULL # object |  (optional)
dcnm_token = 'dcnm_token_example' # str |  (optional)
content_type = 'content_type_example' # str |  (optional)

try:
    # deploy vrf
    api_instance.rest_top_down_fabrics_fabric_vrfs_deployments_post(fabric, body=body, dcnm_token=dcnm_token, content_type=content_type)
except ApiException as e:
    print("Exception when calling VRFOperationsApi->rest_top_down_fabrics_fabric_vrfs_deployments_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fabric** | **str**|  | 
 **body** | [**object**](object.md)|  | [optional] 
 **dcnm_token** | **str**|  | [optional] 
 **content_type** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_top_down_fabrics_fabric_vrfs_get**
> rest_top_down_fabrics_fabric_vrfs_get(fabric, dcnm_token=dcnm_token, content_type=content_type)

query vrf

Lists all VRFs in the fabric defined within the URI

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.VRFOperationsApi()
fabric = 'fabric_example' # str | 
dcnm_token = 'dcnm_token_example' # str |  (optional)
content_type = 'content_type_example' # str |  (optional)

try:
    # query vrf
    api_instance.rest_top_down_fabrics_fabric_vrfs_get(fabric, dcnm_token=dcnm_token, content_type=content_type)
except ApiException as e:
    print("Exception when calling VRFOperationsApi->rest_top_down_fabrics_fabric_vrfs_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fabric** | **str**|  | 
 **dcnm_token** | **str**|  | [optional] 
 **content_type** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_top_down_fabrics_fabric_vrfs_post**
> rest_top_down_fabrics_fabric_vrfs_post(fabric, body=body, dcnm_token=dcnm_token, content_type=content_type)

create vrf

Creates a VRF within the fabric defined in the URI.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.VRFOperationsApi()
fabric = 'fabric_example' # str | 
body = 'body_example' # str |  (optional)
dcnm_token = 'dcnm_token_example' # str |  (optional)
content_type = 'content_type_example' # str |  (optional)

try:
    # create vrf
    api_instance.rest_top_down_fabrics_fabric_vrfs_post(fabric, body=body, dcnm_token=dcnm_token, content_type=content_type)
except ApiException as e:
    print("Exception when calling VRFOperationsApi->rest_top_down_fabrics_fabric_vrfs_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fabric** | **str**|  | 
 **body** | [**str**](str.md)|  | [optional] 
 **dcnm_token** | **str**|  | [optional] 
 **content_type** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_top_down_fabrics_fabric_vrfs_switches_get**
> rest_top_down_fabrics_fabric_vrfs_switches_get(fabric, dcnm_token=dcnm_token, content_type=content_type, vrf_names=vrf_names, serial_numbers=serial_numbers)

get switch details by vrf

Used to obtain the switch details per VRF using a comma-separated list of VRF names and switch serial numbers defined within the URI

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.VRFOperationsApi()
fabric = 'fabric_example' # str | 
dcnm_token = 'dcnm_token_example' # str |  (optional)
content_type = 'content_type_example' # str |  (optional)
vrf_names = 'vrf_names_example' # str |  (optional)
serial_numbers = 'serial_numbers_example' # str |  (optional)

try:
    # get switch details by vrf
    api_instance.rest_top_down_fabrics_fabric_vrfs_switches_get(fabric, dcnm_token=dcnm_token, content_type=content_type, vrf_names=vrf_names, serial_numbers=serial_numbers)
except ApiException as e:
    print("Exception when calling VRFOperationsApi->rest_top_down_fabrics_fabric_vrfs_switches_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fabric** | **str**|  | 
 **dcnm_token** | **str**|  | [optional] 
 **content_type** | **str**|  | [optional] 
 **vrf_names** | **str**|  | [optional] 
 **serial_numbers** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_top_down_fabrics_fabric_vrfs_vrf_delete**
> rest_top_down_fabrics_fabric_vrfs_vrf_delete(fabric, vrf, dcnm_token=dcnm_token, content_type=content_type)

delete vrf

Deletes the defined VRF within the fabric defined inside of the URI

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.VRFOperationsApi()
fabric = 'fabric_example' # str | 
vrf = 'vrf_example' # str | 
dcnm_token = 'dcnm_token_example' # str |  (optional)
content_type = 'content_type_example' # str |  (optional)

try:
    # delete vrf
    api_instance.rest_top_down_fabrics_fabric_vrfs_vrf_delete(fabric, vrf, dcnm_token=dcnm_token, content_type=content_type)
except ApiException as e:
    print("Exception when calling VRFOperationsApi->rest_top_down_fabrics_fabric_vrfs_vrf_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fabric** | **str**|  | 
 **vrf** | **str**|  | 
 **dcnm_token** | **str**|  | [optional] 
 **content_type** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_top_down_fabrics_fabric_vrfs_vrf_put**
> rest_top_down_fabrics_fabric_vrfs_vrf_put(fabric, vrf, body=body, dcnm_token=dcnm_token, content_type=content_type)

update vrf

Updates the template configuration applied to a VRF after deployment

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.VRFOperationsApi()
fabric = 'fabric_example' # str | 
vrf = 'vrf_example' # str | 
body = 'body_example' # str |  (optional)
dcnm_token = 'dcnm_token_example' # str |  (optional)
content_type = 'content_type_example' # str |  (optional)

try:
    # update vrf
    api_instance.rest_top_down_fabrics_fabric_vrfs_vrf_put(fabric, vrf, body=body, dcnm_token=dcnm_token, content_type=content_type)
except ApiException as e:
    print("Exception when calling VRFOperationsApi->rest_top_down_fabrics_fabric_vrfs_vrf_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fabric** | **str**|  | 
 **vrf** | **str**|  | 
 **body** | [**str**](str.md)|  | [optional] 
 **dcnm_token** | **str**|  | [optional] 
 **content_type** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

