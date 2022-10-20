# swagger_client.ServiceOperationsApi

All URIs are relative to *https://{{dcnm}}*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_fabrics_service_fabric_service_node_post**](ServiceOperationsApi.md#rest_fabrics_service_fabric_service_node_post) | **POST** /rest/fabrics/{service_fabric}/service-node | create service node
[**rest_fabrics_service_fabric_service_nodes_get**](ServiceOperationsApi.md#rest_fabrics_service_fabric_service_nodes_get) | **GET** /rest/fabrics/{service_fabric}/service-nodes | get service node 
[**rest_fabrics_service_fabric_service_nodes_service_node_peerings_fabric_attachments_delete**](ServiceOperationsApi.md#rest_fabrics_service_fabric_service_nodes_service_node_peerings_fabric_attachments_delete) | **DELETE** /rest/fabrics/{service_fabric}/service-nodes/{service_node}/peerings/{fabric}/attachments | detach route peering
[**rest_fabrics_service_fabric_service_nodes_service_node_peerings_fabric_attachments_post**](ServiceOperationsApi.md#rest_fabrics_service_fabric_service_nodes_service_node_peerings_fabric_attachments_post) | **POST** /rest/fabrics/{service_fabric}/service-nodes/{service_node}/peerings/{fabric}/attachments | attach route peering
[**rest_fabrics_service_fabric_service_nodes_service_node_peerings_fabric_delete**](ServiceOperationsApi.md#rest_fabrics_service_fabric_service_nodes_service_node_peerings_fabric_delete) | **DELETE** /rest/fabrics/{service_fabric}/service-nodes/{service_node}/peerings/{fabric} | delete route peering
[**rest_fabrics_service_fabric_service_nodes_service_node_peerings_fabric_depoloyments_post**](ServiceOperationsApi.md#rest_fabrics_service_fabric_service_nodes_service_node_peerings_fabric_depoloyments_post) | **POST** /rest/fabrics/{service_fabric}/service-nodes/{service_node}/peerings/{fabric}/depoloyments | deploy route peering
[**rest_fabrics_service_fabric_service_nodes_service_node_peerings_post**](ServiceOperationsApi.md#rest_fabrics_service_fabric_service_nodes_service_node_peerings_post) | **POST** /rest/fabrics/{service_fabric}/service-nodes/{service_node}/peerings | create route peering
[**rest_fabrics_service_fabric_service_nodes_service_node_policies_delete**](ServiceOperationsApi.md#rest_fabrics_service_fabric_service_nodes_service_node_policies_delete) | **DELETE** /rest/fabrics/{service_fabric}/service-nodes/{service_node}/policies | delete service policy
[**rest_fabrics_service_fabric_service_nodes_service_node_policies_fabric_attachments_delete**](ServiceOperationsApi.md#rest_fabrics_service_fabric_service_nodes_service_node_policies_fabric_attachments_delete) | **DELETE** /rest/fabrics/{service_fabric}/service-nodes/{service_node}/policies/{fabric}/attachments | detach service policy
[**rest_fabrics_service_fabric_service_nodes_service_node_policies_fabric_attachments_post**](ServiceOperationsApi.md#rest_fabrics_service_fabric_service_nodes_service_node_policies_fabric_attachments_post) | **POST** /rest/fabrics/{service_fabric}/service-nodes/{service_node}/policies/{fabric}/attachments | attach service policy
[**rest_fabrics_service_fabric_service_nodes_service_node_policies_fabric_deployments_post**](ServiceOperationsApi.md#rest_fabrics_service_fabric_service_nodes_service_node_policies_fabric_deployments_post) | **POST** /rest/fabrics/{service_fabric}/service-nodes/{service_node}/policies/{fabric}/deployments | deploy service policy
[**rest_fabrics_service_fabric_service_nodes_service_node_policies_post**](ServiceOperationsApi.md#rest_fabrics_service_fabric_service_nodes_service_node_policies_post) | **POST** /rest/fabrics/{service_fabric}/service-nodes/{service_node}/policies | create service policy
[**rest_fabricsservice_fabric_service_node_service_node_peerings_get**](ServiceOperationsApi.md#rest_fabricsservice_fabric_service_node_service_node_peerings_get) | **GET** /rest/fabrics{service_fabric}/service-node/{service_node}/peerings | get route peering of node
[**rest_service_fabric_service_nodes_service_node_delete**](ServiceOperationsApi.md#rest_service_fabric_service_nodes_service_node_delete) | **DELETE** /rest/{service_fabric}/service-nodes/{service_node} | delete service node
[**rest_service_fabric_service_nodes_service_node_policies_get**](ServiceOperationsApi.md#rest_service_fabric_service_nodes_service_node_policies_get) | **GET** /rest/{service_fabric}/service-nodes/{service_node}/policies | get service policy

# **rest_fabrics_service_fabric_service_node_post**
> rest_fabrics_service_fabric_service_node_post(service_fabric, body=body, dcnm_token=dcnm_token, content_type=content_type)

create service node

Creates a service node within the external service fabric.  The payload will include the fabric that the node is attached to (EasyFabric) as well as the device and port-level information

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ServiceOperationsApi()
service_fabric = 'service_fabric_example' # str | 
body = NULL # object |  (optional)
dcnm_token = 'dcnm_token_example' # str |  (optional)
content_type = 'content_type_example' # str |  (optional)

try:
    # create service node
    api_instance.rest_fabrics_service_fabric_service_node_post(service_fabric, body=body, dcnm_token=dcnm_token, content_type=content_type)
except ApiException as e:
    print("Exception when calling ServiceOperationsApi->rest_fabrics_service_fabric_service_node_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_fabric** | **str**|  | 
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

# **rest_fabrics_service_fabric_service_nodes_get**
> rest_fabrics_service_fabric_service_nodes_get(service_fabric, dcnm_token=dcnm_token, content_type=content_type)

get service node 

Used to retrieve the service nodes present under the fabric defined within the URI.  The fabric will be an external fabric to the EVPN-VXLAN EasyFabric

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ServiceOperationsApi()
service_fabric = 'service_fabric_example' # str | 
dcnm_token = 'dcnm_token_example' # str |  (optional)
content_type = 'content_type_example' # str |  (optional)

try:
    # get service node 
    api_instance.rest_fabrics_service_fabric_service_nodes_get(service_fabric, dcnm_token=dcnm_token, content_type=content_type)
except ApiException as e:
    print("Exception when calling ServiceOperationsApi->rest_fabrics_service_fabric_service_nodes_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_fabric** | **str**|  | 
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

# **rest_fabrics_service_fabric_service_nodes_service_node_peerings_fabric_attachments_delete**
> rest_fabrics_service_fabric_service_nodes_service_node_peerings_fabric_attachments_delete(service_fabric, service_node, fabric, dcnm_token=dcnm_token, content_type=content_type, peering_names=peering_names)

detach route peering

Used to detach the service networks and their VRF of the selected route peering to service leaf

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ServiceOperationsApi()
service_fabric = 'service_fabric_example' # str | 
service_node = 'service_node_example' # str | 
fabric = 'fabric_example' # str | 
dcnm_token = 'dcnm_token_example' # str |  (optional)
content_type = 'content_type_example' # str |  (optional)
peering_names = 'peering_names_example' # str |  (optional)

try:
    # detach route peering
    api_instance.rest_fabrics_service_fabric_service_nodes_service_node_peerings_fabric_attachments_delete(service_fabric, service_node, fabric, dcnm_token=dcnm_token, content_type=content_type, peering_names=peering_names)
except ApiException as e:
    print("Exception when calling ServiceOperationsApi->rest_fabrics_service_fabric_service_nodes_service_node_peerings_fabric_attachments_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_fabric** | **str**|  | 
 **service_node** | **str**|  | 
 **fabric** | **str**|  | 
 **dcnm_token** | **str**|  | [optional] 
 **content_type** | **str**|  | [optional] 
 **peering_names** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_fabrics_service_fabric_service_nodes_service_node_peerings_fabric_attachments_post**
> rest_fabrics_service_fabric_service_nodes_service_node_peerings_fabric_attachments_post(service_fabric, service_node, fabric, body=body, dcnm_token=dcnm_token, content_type=content_type)

attach route peering

Used to attach the service networks and their VRF of the selected route peerings to service leaf

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ServiceOperationsApi()
service_fabric = 'service_fabric_example' # str | 
service_node = 'service_node_example' # str | 
fabric = 'fabric_example' # str | 
body = 'body_example' # str |  (optional)
dcnm_token = 'dcnm_token_example' # str |  (optional)
content_type = 'content_type_example' # str |  (optional)

try:
    # attach route peering
    api_instance.rest_fabrics_service_fabric_service_nodes_service_node_peerings_fabric_attachments_post(service_fabric, service_node, fabric, body=body, dcnm_token=dcnm_token, content_type=content_type)
except ApiException as e:
    print("Exception when calling ServiceOperationsApi->rest_fabrics_service_fabric_service_nodes_service_node_peerings_fabric_attachments_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_fabric** | **str**|  | 
 **service_node** | **str**|  | 
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

# **rest_fabrics_service_fabric_service_nodes_service_node_peerings_fabric_delete**
> rest_fabrics_service_fabric_service_nodes_service_node_peerings_fabric_delete(service_fabric, service_node, fabric, dcnm_token=dcnm_token, content_type=content_type)

delete route peering

Used to delete a service route peering for the selected service node of the type under the selected fabric

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ServiceOperationsApi()
service_fabric = 'service_fabric_example' # str | 
service_node = 'service_node_example' # str | 
fabric = 'fabric_example' # str | 
dcnm_token = 'dcnm_token_example' # str |  (optional)
content_type = 'content_type_example' # str |  (optional)

try:
    # delete route peering
    api_instance.rest_fabrics_service_fabric_service_nodes_service_node_peerings_fabric_delete(service_fabric, service_node, fabric, dcnm_token=dcnm_token, content_type=content_type)
except ApiException as e:
    print("Exception when calling ServiceOperationsApi->rest_fabrics_service_fabric_service_nodes_service_node_peerings_fabric_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_fabric** | **str**|  | 
 **service_node** | **str**|  | 
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

# **rest_fabrics_service_fabric_service_nodes_service_node_peerings_fabric_depoloyments_post**
> rest_fabrics_service_fabric_service_nodes_service_node_peerings_fabric_depoloyments_post(service_fabric, service_node, fabric, body=body, dcnm_token=dcnm_token, content_type=content_type)

deploy route peering

Used to deploy the service network and its VRF of the selected route peerings to service leaf

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ServiceOperationsApi()
service_fabric = 'service_fabric_example' # str | 
service_node = 'service_node_example' # str | 
fabric = 'fabric_example' # str | 
body = 'body_example' # str |  (optional)
dcnm_token = 'dcnm_token_example' # str |  (optional)
content_type = 'content_type_example' # str |  (optional)

try:
    # deploy route peering
    api_instance.rest_fabrics_service_fabric_service_nodes_service_node_peerings_fabric_depoloyments_post(service_fabric, service_node, fabric, body=body, dcnm_token=dcnm_token, content_type=content_type)
except ApiException as e:
    print("Exception when calling ServiceOperationsApi->rest_fabrics_service_fabric_service_nodes_service_node_peerings_fabric_depoloyments_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_fabric** | **str**|  | 
 **service_node** | **str**|  | 
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

# **rest_fabrics_service_fabric_service_nodes_service_node_peerings_post**
> rest_fabrics_service_fabric_service_nodes_service_node_peerings_post(service_fabric, service_node, body=body, dcnm_token=dcnm_token, content_type=content_type)

create route peering

Used to create service route peering under the selected fabric, i.e. the logic attachment to the easy fabric

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ServiceOperationsApi()
service_fabric = 'service_fabric_example' # str | 
service_node = 'service_node_example' # str | 
body = 'body_example' # str |  (optional)
dcnm_token = 'dcnm_token_example' # str |  (optional)
content_type = 'content_type_example' # str |  (optional)

try:
    # create route peering
    api_instance.rest_fabrics_service_fabric_service_nodes_service_node_peerings_post(service_fabric, service_node, body=body, dcnm_token=dcnm_token, content_type=content_type)
except ApiException as e:
    print("Exception when calling ServiceOperationsApi->rest_fabrics_service_fabric_service_nodes_service_node_peerings_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_fabric** | **str**|  | 
 **service_node** | **str**|  | 
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

# **rest_fabrics_service_fabric_service_nodes_service_node_policies_delete**
> rest_fabrics_service_fabric_service_nodes_service_node_policies_delete(service_fabric, service_node, dcnm_token=dcnm_token, content_type=content_type)

delete service policy

Used to delete service policies for the selected service node under the selected fabric and attached fabric

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ServiceOperationsApi()
service_fabric = 'service_fabric_example' # str | 
service_node = 'service_node_example' # str | 
dcnm_token = 'dcnm_token_example' # str |  (optional)
content_type = 'content_type_example' # str |  (optional)

try:
    # delete service policy
    api_instance.rest_fabrics_service_fabric_service_nodes_service_node_policies_delete(service_fabric, service_node, dcnm_token=dcnm_token, content_type=content_type)
except ApiException as e:
    print("Exception when calling ServiceOperationsApi->rest_fabrics_service_fabric_service_nodes_service_node_policies_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_fabric** | **str**|  | 
 **service_node** | **str**|  | 
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

# **rest_fabrics_service_fabric_service_nodes_service_node_policies_fabric_attachments_delete**
> rest_fabrics_service_fabric_service_nodes_service_node_policies_fabric_attachments_delete(service_fabric, service_node, fabric, dcnm_token=dcnm_token, content_type=content_type, policy_names=policy_names)

detach service policy

Used to disable the service policies on the source or/and destination networks

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ServiceOperationsApi()
service_fabric = 'service_fabric_example' # str | 
service_node = 'service_node_example' # str | 
fabric = 'fabric_example' # str | 
dcnm_token = 'dcnm_token_example' # str |  (optional)
content_type = 'content_type_example' # str |  (optional)
policy_names = 'policy_names_example' # str |  (optional)

try:
    # detach service policy
    api_instance.rest_fabrics_service_fabric_service_nodes_service_node_policies_fabric_attachments_delete(service_fabric, service_node, fabric, dcnm_token=dcnm_token, content_type=content_type, policy_names=policy_names)
except ApiException as e:
    print("Exception when calling ServiceOperationsApi->rest_fabrics_service_fabric_service_nodes_service_node_policies_fabric_attachments_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_fabric** | **str**|  | 
 **service_node** | **str**|  | 
 **fabric** | **str**|  | 
 **dcnm_token** | **str**|  | [optional] 
 **content_type** | **str**|  | [optional] 
 **policy_names** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_fabrics_service_fabric_service_nodes_service_node_policies_fabric_attachments_post**
> rest_fabrics_service_fabric_service_nodes_service_node_policies_fabric_attachments_post(service_fabric, service_node, fabric, body=body, dcnm_token=dcnm_token, content_type=content_type)

attach service policy

Used to enable the service policies on the source or/and destination networks

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ServiceOperationsApi()
service_fabric = 'service_fabric_example' # str | 
service_node = 'service_node_example' # str | 
fabric = 'fabric_example' # str | 
body = 'body_example' # str |  (optional)
dcnm_token = 'dcnm_token_example' # str |  (optional)
content_type = 'content_type_example' # str |  (optional)

try:
    # attach service policy
    api_instance.rest_fabrics_service_fabric_service_nodes_service_node_policies_fabric_attachments_post(service_fabric, service_node, fabric, body=body, dcnm_token=dcnm_token, content_type=content_type)
except ApiException as e:
    print("Exception when calling ServiceOperationsApi->rest_fabrics_service_fabric_service_nodes_service_node_policies_fabric_attachments_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_fabric** | **str**|  | 
 **service_node** | **str**|  | 
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

# **rest_fabrics_service_fabric_service_nodes_service_node_policies_fabric_deployments_post**
> rest_fabrics_service_fabric_service_nodes_service_node_policies_fabric_deployments_post(service_fabric, service_node, fabric, body=body, dcnm_token=dcnm_token, content_type=content_type)

deploy service policy

Used to deploy the service policy on the source or/and destination network if those networks have been attached.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ServiceOperationsApi()
service_fabric = 'service_fabric_example' # str | 
service_node = 'service_node_example' # str | 
fabric = 'fabric_example' # str | 
body = 'body_example' # str |  (optional)
dcnm_token = 'dcnm_token_example' # str |  (optional)
content_type = 'content_type_example' # str |  (optional)

try:
    # deploy service policy
    api_instance.rest_fabrics_service_fabric_service_nodes_service_node_policies_fabric_deployments_post(service_fabric, service_node, fabric, body=body, dcnm_token=dcnm_token, content_type=content_type)
except ApiException as e:
    print("Exception when calling ServiceOperationsApi->rest_fabrics_service_fabric_service_nodes_service_node_policies_fabric_deployments_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_fabric** | **str**|  | 
 **service_node** | **str**|  | 
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

# **rest_fabrics_service_fabric_service_nodes_service_node_policies_post**
> rest_fabrics_service_fabric_service_nodes_service_node_policies_post(service_fabric, service_node, body=body, dcnm_token=dcnm_token, content_type=content_type)

create service policy

Used to create a service policy for the selected service node under the selected fabric

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ServiceOperationsApi()
service_fabric = 'service_fabric_example' # str | 
service_node = 'service_node_example' # str | 
body = 'body_example' # str |  (optional)
dcnm_token = 'dcnm_token_example' # str |  (optional)
content_type = 'content_type_example' # str |  (optional)

try:
    # create service policy
    api_instance.rest_fabrics_service_fabric_service_nodes_service_node_policies_post(service_fabric, service_node, body=body, dcnm_token=dcnm_token, content_type=content_type)
except ApiException as e:
    print("Exception when calling ServiceOperationsApi->rest_fabrics_service_fabric_service_nodes_service_node_policies_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_fabric** | **str**|  | 
 **service_node** | **str**|  | 
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

# **rest_fabricsservice_fabric_service_node_service_node_peerings_get**
> rest_fabricsservice_fabric_service_node_service_node_peerings_get(service_fabric, service_node, dcnm_token=dcnm_token, content_type=content_type)

get route peering of node

Used to retrieve service route peering(s) for the selected service node under the selected fabric

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ServiceOperationsApi()
service_fabric = 'service_fabric_example' # str | 
service_node = 'service_node_example' # str | 
dcnm_token = 'dcnm_token_example' # str |  (optional)
content_type = 'content_type_example' # str |  (optional)

try:
    # get route peering of node
    api_instance.rest_fabricsservice_fabric_service_node_service_node_peerings_get(service_fabric, service_node, dcnm_token=dcnm_token, content_type=content_type)
except ApiException as e:
    print("Exception when calling ServiceOperationsApi->rest_fabricsservice_fabric_service_node_service_node_peerings_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_fabric** | **str**|  | 
 **service_node** | **str**|  | 
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

# **rest_service_fabric_service_nodes_service_node_delete**
> rest_service_fabric_service_nodes_service_node_delete(service_fabric, service_node, dcnm_token=dcnm_token, content_type=content_type)

delete service node

Removes the service node defined in the URI from the external service fabric (also defined in the URI)

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ServiceOperationsApi()
service_fabric = 'service_fabric_example' # str | 
service_node = 'service_node_example' # str | 
dcnm_token = 'dcnm_token_example' # str |  (optional)
content_type = 'content_type_example' # str |  (optional)

try:
    # delete service node
    api_instance.rest_service_fabric_service_nodes_service_node_delete(service_fabric, service_node, dcnm_token=dcnm_token, content_type=content_type)
except ApiException as e:
    print("Exception when calling ServiceOperationsApi->rest_service_fabric_service_nodes_service_node_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_fabric** | **str**|  | 
 **service_node** | **str**|  | 
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

# **rest_service_fabric_service_nodes_service_node_policies_get**
> rest_service_fabric_service_nodes_service_node_policies_get(service_fabric, service_node, dcnm_token=dcnm_token, content_type=content_type)

get service policy

Used to retrieve service policies for the selected service node under the selected fabric

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ServiceOperationsApi()
service_fabric = 'service_fabric_example' # str | 
service_node = 'service_node_example' # str | 
dcnm_token = 'dcnm_token_example' # str |  (optional)
content_type = 'content_type_example' # str |  (optional)

try:
    # get service policy
    api_instance.rest_service_fabric_service_nodes_service_node_policies_get(service_fabric, service_node, dcnm_token=dcnm_token, content_type=content_type)
except ApiException as e:
    print("Exception when calling ServiceOperationsApi->rest_service_fabric_service_nodes_service_node_policies_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_fabric** | **str**|  | 
 **service_node** | **str**|  | 
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

