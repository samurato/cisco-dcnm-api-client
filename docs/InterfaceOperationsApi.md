# swagger_client.InterfaceOperationsApi

All URIs are relative to *https://{{dcnm}}*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_interface_adminstatus_post**](InterfaceOperationsApi.md#rest_interface_adminstatus_post) | **POST** /rest/interface/adminstatus | shutdown interface
[**rest_interface_deploy_post**](InterfaceOperationsApi.md#rest_interface_deploy_post) | **POST** /rest/interface/deploy | deploy interface
[**rest_interface_get**](InterfaceOperationsApi.md#rest_interface_get) | **GET** /rest/interface | query inteface
[**rest_interface_post**](InterfaceOperationsApi.md#rest_interface_post) | **POST** /rest/interface/ | config ethernet
[**rest_interface_post_0**](InterfaceOperationsApi.md#rest_interface_post_0) | **POST** /rest/interface | create routed subif

# **rest_interface_adminstatus_post**
> rest_interface_adminstatus_post(body=body, dcnm_token=dcnm_token)

shutdown interface

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.InterfaceOperationsApi()
body = NULL # object |  (optional)
dcnm_token = 'dcnm_token_example' # str |  (optional)

try:
    # shutdown interface
    api_instance.rest_interface_adminstatus_post(body=body, dcnm_token=dcnm_token)
except ApiException as e:
    print("Exception when calling InterfaceOperationsApi->rest_interface_adminstatus_post: %s\n" % e)
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

# **rest_interface_deploy_post**
> rest_interface_deploy_post(body=body, dcnm_token=dcnm_token, content_type=content_type)

deploy interface

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.InterfaceOperationsApi()
body = 'body_example' # str |  (optional)
dcnm_token = 'dcnm_token_example' # str |  (optional)
content_type = 'content_type_example' # str |  (optional)

try:
    # deploy interface
    api_instance.rest_interface_deploy_post(body=body, dcnm_token=dcnm_token, content_type=content_type)
except ApiException as e:
    print("Exception when calling InterfaceOperationsApi->rest_interface_deploy_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **rest_interface_get**
> rest_interface_get(dcnm_token=dcnm_token, serial_number=serial_number, if_name=if_name)

query inteface

Returns the Policy attached with each interface and corresponding config parameters(`nv_pairs`)

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.InterfaceOperationsApi()
dcnm_token = 'dcnm_token_example' # str |  (optional)
serial_number = 'serial_number_example' # str |  (optional)
if_name = 'if_name_example' # str |  (optional)

try:
    # query inteface
    api_instance.rest_interface_get(dcnm_token=dcnm_token, serial_number=serial_number, if_name=if_name)
except ApiException as e:
    print("Exception when calling InterfaceOperationsApi->rest_interface_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dcnm_token** | **str**|  | [optional] 
 **serial_number** | **str**|  | [optional] 
 **if_name** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_interface_post**
> rest_interface_post(body=body, dcnm_token=dcnm_token, content_type=content_type)

config ethernet

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.InterfaceOperationsApi()
body = 'body_example' # str |  (optional)
dcnm_token = 'dcnm_token_example' # str |  (optional)
content_type = 'content_type_example' # str |  (optional)

try:
    # config ethernet
    api_instance.rest_interface_post(body=body, dcnm_token=dcnm_token, content_type=content_type)
except ApiException as e:
    print("Exception when calling InterfaceOperationsApi->rest_interface_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **rest_interface_post_0**
> rest_interface_post_0(body=body, dcnm_token=dcnm_token, content_type=content_type)

create routed subif

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.InterfaceOperationsApi()
body = 'body_example' # str |  (optional)
dcnm_token = 'dcnm_token_example' # str |  (optional)
content_type = 'content_type_example' # str |  (optional)

try:
    # create routed subif
    api_instance.rest_interface_post_0(body=body, dcnm_token=dcnm_token, content_type=content_type)
except ApiException as e:
    print("Exception when calling InterfaceOperationsApi->rest_interface_post_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

