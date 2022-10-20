# swagger_client.NetworkOperationsApi

All URIs are relative to *https://{{dcnm}}*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_managed_pool_fabrics_fabric_segments_ids_post**](NetworkOperationsApi.md#rest_managed_pool_fabrics_fabric_segments_ids_post) | **POST** /rest/managed-pool/fabrics/{fabric}/segments/ids | get network id
[**rest_top_down_fabrics_fabric_networks_attachments_get**](NetworkOperationsApi.md#rest_top_down_fabrics_fabric_networks_attachments_get) | **GET** /rest/top-down/fabrics/{fabric}/networks/attachments | query network attachments
[**rest_top_down_fabrics_fabric_networks_attachments_post**](NetworkOperationsApi.md#rest_top_down_fabrics_fabric_networks_attachments_post) | **POST** /rest/top-down/fabrics/{fabric}/networks/attachments | attach network to switches
[**rest_top_down_fabrics_fabric_networks_get**](NetworkOperationsApi.md#rest_top_down_fabrics_fabric_networks_get) | **GET** /rest/top-down/fabrics/{fabric}/networks/ | get network details
[**rest_top_down_fabrics_fabric_networks_network_delete**](NetworkOperationsApi.md#rest_top_down_fabrics_fabric_networks_network_delete) | **DELETE** /rest/top-down/fabrics/{fabric}/networks/{network} | delete network
[**rest_top_down_fabrics_fabric_networks_network_deploy_post**](NetworkOperationsApi.md#rest_top_down_fabrics_fabric_networks_network_deploy_post) | **POST** /rest/top-down/fabrics/{fabric}/networks/{network}/deploy | deploy network
[**rest_top_down_fabrics_fabric_networks_post**](NetworkOperationsApi.md#rest_top_down_fabrics_fabric_networks_post) | **POST** /rest/top-down/fabrics/{fabric}/networks | create network

# **rest_managed_pool_fabrics_fabric_segments_ids_post**
> rest_managed_pool_fabrics_fabric_segments_ids_post(fabric, dcnm_token=dcnm_token, content_type=content_type)

get network id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NetworkOperationsApi()
fabric = 'fabric_example' # str | 
dcnm_token = 'dcnm_token_example' # str |  (optional)
content_type = 'content_type_example' # str |  (optional)

try:
    # get network id
    api_instance.rest_managed_pool_fabrics_fabric_segments_ids_post(fabric, dcnm_token=dcnm_token, content_type=content_type)
except ApiException as e:
    print("Exception when calling NetworkOperationsApi->rest_managed_pool_fabrics_fabric_segments_ids_post: %s\n" % e)
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

# **rest_top_down_fabrics_fabric_networks_attachments_get**
> rest_top_down_fabrics_fabric_networks_attachments_get(fabric, content_type=content_type, dcnm_token=dcnm_token, network_names=network_names)

query network attachments

Used to list all the attached switches and ports and deployment status in the given networks, filtered by the network names defined in the URI.  _Must have at least one network defined within the URI, but can be comma-separated list_

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NetworkOperationsApi()
fabric = 'fabric_example' # str | 
content_type = 'content_type_example' # str |  (optional)
dcnm_token = 'dcnm_token_example' # str |  (optional)
network_names = 'network_names_example' # str |  (optional)

try:
    # query network attachments
    api_instance.rest_top_down_fabrics_fabric_networks_attachments_get(fabric, content_type=content_type, dcnm_token=dcnm_token, network_names=network_names)
except ApiException as e:
    print("Exception when calling NetworkOperationsApi->rest_top_down_fabrics_fabric_networks_attachments_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fabric** | **str**|  | 
 **content_type** | **str**|  | [optional] 
 **dcnm_token** | **str**|  | [optional] 
 **network_names** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_top_down_fabrics_fabric_networks_attachments_post**
> rest_top_down_fabrics_fabric_networks_attachments_post(fabric, body=body, content_type=content_type, dcnm_token=dcnm_token)

attach network to switches

Attaches the created network to the leaf switches defined within the payload of the request.    _Please ensure proper serial numbers and \"edge-facing\" ports are referenced in the payload_

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NetworkOperationsApi()
fabric = 'fabric_example' # str | 
body = 'body_example' # str |  (optional)
content_type = 'content_type_example' # str |  (optional)
dcnm_token = 'dcnm_token_example' # str |  (optional)

try:
    # attach network to switches
    api_instance.rest_top_down_fabrics_fabric_networks_attachments_post(fabric, body=body, content_type=content_type, dcnm_token=dcnm_token)
except ApiException as e:
    print("Exception when calling NetworkOperationsApi->rest_top_down_fabrics_fabric_networks_attachments_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fabric** | **str**|  | 
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

# **rest_top_down_fabrics_fabric_networks_get**
> rest_top_down_fabrics_fabric_networks_get(fabric, content_type=content_type, dcnm_token=dcnm_token)

get network details

Used to list all the Networks under the selected fabric

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NetworkOperationsApi()
fabric = 'fabric_example' # str | 
content_type = 'content_type_example' # str |  (optional)
dcnm_token = 'dcnm_token_example' # str |  (optional)

try:
    # get network details
    api_instance.rest_top_down_fabrics_fabric_networks_get(fabric, content_type=content_type, dcnm_token=dcnm_token)
except ApiException as e:
    print("Exception when calling NetworkOperationsApi->rest_top_down_fabrics_fabric_networks_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fabric** | **str**|  | 
 **content_type** | **str**|  | [optional] 
 **dcnm_token** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_top_down_fabrics_fabric_networks_network_delete**
> rest_top_down_fabrics_fabric_networks_network_delete(fabric, network, content_type=content_type, dcnm_token=dcnm_token)

delete network

Deletes the network named within the URI path

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NetworkOperationsApi()
fabric = 'fabric_example' # str | 
network = 'network_example' # str | 
content_type = 'content_type_example' # str |  (optional)
dcnm_token = 'dcnm_token_example' # str |  (optional)

try:
    # delete network
    api_instance.rest_top_down_fabrics_fabric_networks_network_delete(fabric, network, content_type=content_type, dcnm_token=dcnm_token)
except ApiException as e:
    print("Exception when calling NetworkOperationsApi->rest_top_down_fabrics_fabric_networks_network_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fabric** | **str**|  | 
 **network** | **str**|  | 
 **content_type** | **str**|  | [optional] 
 **dcnm_token** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_top_down_fabrics_fabric_networks_network_deploy_post**
> rest_top_down_fabrics_fabric_networks_network_deploy_post(fabric, network, content_type=content_type, dcnm_token=dcnm_token)

deploy network

Used to deploy the pending config a Network under the selected fabric.  Requires network to be created and attached for successful deployment to fabric

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NetworkOperationsApi()
fabric = 'fabric_example' # str | 
network = 'network_example' # str | 
content_type = 'content_type_example' # str |  (optional)
dcnm_token = 'dcnm_token_example' # str |  (optional)

try:
    # deploy network
    api_instance.rest_top_down_fabrics_fabric_networks_network_deploy_post(fabric, network, content_type=content_type, dcnm_token=dcnm_token)
except ApiException as e:
    print("Exception when calling NetworkOperationsApi->rest_top_down_fabrics_fabric_networks_network_deploy_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fabric** | **str**|  | 
 **network** | **str**|  | 
 **content_type** | **str**|  | [optional] 
 **dcnm_token** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_top_down_fabrics_fabric_networks_post**
> rest_top_down_fabrics_fabric_networks_post(fabric, body=body, content_type=content_type, dcnm_token=dcnm_token)

create network

Creates a new network with the unused VLAN ID in the fabric named within the URI path.    _Note: `{{ network_id_number }}` is defined as an ENV var, but will need to be changed if more than one network is created on DCNM._

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NetworkOperationsApi()
fabric = 'fabric_example' # str | 
body = 'body_example' # str |  (optional)
content_type = 'content_type_example' # str |  (optional)
dcnm_token = 'dcnm_token_example' # str |  (optional)

try:
    # create network
    api_instance.rest_top_down_fabrics_fabric_networks_post(fabric, body=body, content_type=content_type, dcnm_token=dcnm_token)
except ApiException as e:
    print("Exception when calling NetworkOperationsApi->rest_top_down_fabrics_fabric_networks_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fabric** | **str**|  | 
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

