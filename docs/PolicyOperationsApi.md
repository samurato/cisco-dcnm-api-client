# swagger_client.PolicyOperationsApi

All URIs are relative to *https://{{dcnm}}*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_control_policies_deploy_post**](PolicyOperationsApi.md#rest_control_policies_deploy_post) | **POST** /rest/control/policies/deploy | deploy policy
[**rest_control_policies_policy_id_number_delete**](PolicyOperationsApi.md#rest_control_policies_policy_id_number_delete) | **DELETE** /rest/control/policies/{policy_id_number} | delete policy
[**rest_control_policies_post**](PolicyOperationsApi.md#rest_control_policies_post) | **POST** /rest/control/policies | create policy
[**rest_control_policies_switches_get**](PolicyOperationsApi.md#rest_control_policies_switches_get) | **GET** /rest/control/policies/switches | get policies

# **rest_control_policies_deploy_post**
> rest_control_policies_deploy_post(body=body, dcnm_token=dcnm_token, content_type=content_type)

deploy policy

Deploys the created policy-switch assignment to the devices

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PolicyOperationsApi()
body = 'body_example' # str |  (optional)
dcnm_token = 'dcnm_token_example' # str |  (optional)
content_type = 'content_type_example' # str |  (optional)

try:
    # deploy policy
    api_instance.rest_control_policies_deploy_post(body=body, dcnm_token=dcnm_token, content_type=content_type)
except ApiException as e:
    print("Exception when calling PolicyOperationsApi->rest_control_policies_deploy_post: %s\n" % e)
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

# **rest_control_policies_policy_id_number_delete**
> rest_control_policies_policy_id_number_delete(policy_id_number, dcnm_token=dcnm_token, content_type=content_type)

delete policy

Deletes a given policy as defined by the policyID value defined within the URI

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PolicyOperationsApi()
policy_id_number = 'policy_id_number_example' # str | 
dcnm_token = 'dcnm_token_example' # str |  (optional)
content_type = 'content_type_example' # str |  (optional)

try:
    # delete policy
    api_instance.rest_control_policies_policy_id_number_delete(policy_id_number, dcnm_token=dcnm_token, content_type=content_type)
except ApiException as e:
    print("Exception when calling PolicyOperationsApi->rest_control_policies_policy_id_number_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_id_number** | **str**|  | 
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

# **rest_control_policies_post**
> rest_control_policies_post(body=body, dcnm_token=dcnm_token, content_type=content_type)

create policy

Creates a specific application of a policy against the switch defined by the serial number in the payload

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PolicyOperationsApi()
body = 'body_example' # str |  (optional)
dcnm_token = 'dcnm_token_example' # str |  (optional)
content_type = 'content_type_example' # str |  (optional)

try:
    # create policy
    api_instance.rest_control_policies_post(body=body, dcnm_token=dcnm_token, content_type=content_type)
except ApiException as e:
    print("Exception when calling PolicyOperationsApi->rest_control_policies_post: %s\n" % e)
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

# **rest_control_policies_switches_get**
> rest_control_policies_switches_get(dcnm_token=dcnm_token, content_type=content_type, serial_number=serial_number)

get policies

List the applied policies to a switch based on the comma-separated list of serial numbers defined within the URI

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PolicyOperationsApi()
dcnm_token = 'dcnm_token_example' # str |  (optional)
content_type = 'content_type_example' # str |  (optional)
serial_number = 'serial_number_example' # str |  (optional)

try:
    # get policies
    api_instance.rest_control_policies_switches_get(dcnm_token=dcnm_token, content_type=content_type, serial_number=serial_number)
except ApiException as e:
    print("Exception when calling PolicyOperationsApi->rest_control_policies_switches_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dcnm_token** | **str**|  | [optional] 
 **content_type** | **str**|  | [optional] 
 **serial_number** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

