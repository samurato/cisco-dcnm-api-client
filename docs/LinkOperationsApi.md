# swagger_client.LinkOperationsApi

All URIs are relative to *https://{{dcnm}}*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_control_links_fabrics_fabric_get**](LinkOperationsApi.md#rest_control_links_fabrics_fabric_get) | **GET** /rest/control/links/fabrics/{fabric} | get all links in fabric
[**rest_control_links_get**](LinkOperationsApi.md#rest_control_links_get) | **GET** /rest/control/links | get all links
[**rest_control_links_linkuuid57500_delete**](LinkOperationsApi.md#rest_control_links_linkuuid57500_delete) | **DELETE** /rest/control/links/LINK-UUID-57500 | delete link
[**rest_control_links_linkuuid57500_put**](LinkOperationsApi.md#rest_control_links_linkuuid57500_put) | **PUT** /rest/control/links/LINK-UUID-57500 | modify link
[**rest_control_links_linkuuid88310_get**](LinkOperationsApi.md#rest_control_links_linkuuid88310_get) | **GET** /rest/control/links/LINK-UUID-88310 | get link info by uuid

# **rest_control_links_fabrics_fabric_get**
> rest_control_links_fabrics_fabric_get(fabric, dcnm_token=dcnm_token)

get all links in fabric

Gathers detailed information for all links within the fabric named within the URI

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LinkOperationsApi()
fabric = 'fabric_example' # str | 
dcnm_token = 'dcnm_token_example' # str |  (optional)

try:
    # get all links in fabric
    api_instance.rest_control_links_fabrics_fabric_get(fabric, dcnm_token=dcnm_token)
except ApiException as e:
    print("Exception when calling LinkOperationsApi->rest_control_links_fabrics_fabric_get: %s\n" % e)
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

# **rest_control_links_get**
> rest_control_links_get(dcnm_token=dcnm_token)

get all links

Used to list all of the links within DCNM

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LinkOperationsApi()
dcnm_token = 'dcnm_token_example' # str |  (optional)

try:
    # get all links
    api_instance.rest_control_links_get(dcnm_token=dcnm_token)
except ApiException as e:
    print("Exception when calling LinkOperationsApi->rest_control_links_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dcnm_token** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_control_links_linkuuid57500_delete**
> rest_control_links_linkuuid57500_delete(dcnm_token=dcnm_token)

delete link

Deletes the link named by the UUID given in the URI

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LinkOperationsApi()
dcnm_token = 'dcnm_token_example' # str |  (optional)

try:
    # delete link
    api_instance.rest_control_links_linkuuid57500_delete(dcnm_token=dcnm_token)
except ApiException as e:
    print("Exception when calling LinkOperationsApi->rest_control_links_linkuuid57500_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dcnm_token** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_control_links_linkuuid57500_put**
> rest_control_links_linkuuid57500_put(body=body, dcnm_token=dcnm_token)

modify link

Modifies the parameters of an existing link through details given within the payload.  Payload can be retrieved from one of the `GET` operations listed within this folder

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LinkOperationsApi()
body = NULL # object |  (optional)
dcnm_token = 'dcnm_token_example' # str |  (optional)

try:
    # modify link
    api_instance.rest_control_links_linkuuid57500_put(body=body, dcnm_token=dcnm_token)
except ApiException as e:
    print("Exception when calling LinkOperationsApi->rest_control_links_linkuuid57500_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**object**](object.md)|  | [optional] 
 **dcnm_token** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_control_links_linkuuid88310_get**
> rest_control_links_linkuuid88310_get(dcnm_token=dcnm_token)

get link info by uuid

Gathers the link details for a given link defined by the UUID within the URI

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LinkOperationsApi()
dcnm_token = 'dcnm_token_example' # str |  (optional)

try:
    # get link info by uuid
    api_instance.rest_control_links_linkuuid88310_get(dcnm_token=dcnm_token)
except ApiException as e:
    print("Exception when calling LinkOperationsApi->rest_control_links_linkuuid88310_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dcnm_token** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

