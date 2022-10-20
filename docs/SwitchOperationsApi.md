# swagger_client.SwitchOperationsApi

All URIs are relative to *https://{{dcnm}}*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_control_switches95_zcg398_f5_c_fabric_name_get**](SwitchOperationsApi.md#rest_control_switches95_zcg398_f5_c_fabric_name_get) | **GET** /rest/control/switches/95ZCG398F5C/fabric-name | get fabric by serial
[**rest_control_switches95_zcg398_f5_c_myip_get**](SwitchOperationsApi.md#rest_control_switches95_zcg398_f5_c_myip_get) | **GET** /rest/control/switches/95ZCG398F5C/myip | get ip by serial
[**rest_control_switches_roles_get**](SwitchOperationsApi.md#rest_control_switches_roles_get) | **GET** /rest/control/switches/roles | list switch roles
[**rest_control_switches_roles_post**](SwitchOperationsApi.md#rest_control_switches_roles_post) | **POST** /rest/control/switches/roles | set switch role

# **rest_control_switches95_zcg398_f5_c_fabric_name_get**
> rest_control_switches95_zcg398_f5_c_fabric_name_get(dcnm_token=dcnm_token, content_type=content_type)

get fabric by serial

Gather the fabric membership of a single switch based on the serial number defined within the URI

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SwitchOperationsApi()
dcnm_token = 'dcnm_token_example' # str |  (optional)
content_type = 'content_type_example' # str |  (optional)

try:
    # get fabric by serial
    api_instance.rest_control_switches95_zcg398_f5_c_fabric_name_get(dcnm_token=dcnm_token, content_type=content_type)
except ApiException as e:
    print("Exception when calling SwitchOperationsApi->rest_control_switches95_zcg398_f5_c_fabric_name_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **rest_control_switches95_zcg398_f5_c_myip_get**
> rest_control_switches95_zcg398_f5_c_myip_get(dcnm_token=dcnm_token, content_type=content_type)

get ip by serial

Gather the address of a switch (as used for management within DCNM) based on the serial number defined within the URI

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SwitchOperationsApi()
dcnm_token = 'dcnm_token_example' # str |  (optional)
content_type = 'content_type_example' # str |  (optional)

try:
    # get ip by serial
    api_instance.rest_control_switches95_zcg398_f5_c_myip_get(dcnm_token=dcnm_token, content_type=content_type)
except ApiException as e:
    print("Exception when calling SwitchOperationsApi->rest_control_switches95_zcg398_f5_c_myip_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **rest_control_switches_roles_get**
> rest_control_switches_roles_get(dcnm_token=dcnm_token, content_type=content_type)

list switch roles

Lists the roles currently applied to all switches.  Can optionally use a query-filter with a comma-separated list of serial numbers to extract the information for only the desired switches

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SwitchOperationsApi()
dcnm_token = 'dcnm_token_example' # str |  (optional)
content_type = 'content_type_example' # str |  (optional)

try:
    # list switch roles
    api_instance.rest_control_switches_roles_get(dcnm_token=dcnm_token, content_type=content_type)
except ApiException as e:
    print("Exception when calling SwitchOperationsApi->rest_control_switches_roles_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **rest_control_switches_roles_post**
> rest_control_switches_roles_post(body=body, dcnm_token=dcnm_token, content_type=content_type)

set switch role

Used to set the desired device's role within the fabric.  Can be one or more devices defined within the array.    _Please ensure correct serial numbers are used within the array_

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SwitchOperationsApi()
body = 'body_example' # str |  (optional)
dcnm_token = 'dcnm_token_example' # str |  (optional)
content_type = 'content_type_example' # str |  (optional)

try:
    # set switch role
    api_instance.rest_control_switches_roles_post(body=body, dcnm_token=dcnm_token, content_type=content_type)
except ApiException as e:
    print("Exception when calling SwitchOperationsApi->rest_control_switches_roles_post: %s\n" % e)
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

