# swagger_client.DCNMAdministrationApi

All URIs are relative to *https://{{dcnm}}*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fm_fmrest_dbadmin_add_user_post**](DCNMAdministrationApi.md#fm_fmrest_dbadmin_add_user_post) | **POST** /fm/fmrest/dbadmin/addUser | add user
[**rest_dcnm_version_get**](DCNMAdministrationApi.md#rest_dcnm_version_get) | **GET** /rest/dcnm-version | get version

# **fm_fmrest_dbadmin_add_user_post**
> fm_fmrest_dbadmin_add_user_post(body=body, dcnm_token=dcnm_token, content_type=content_type)

add user

Adds user to DCNM store.  Pay attention to `role` and `expiration` values if used outside of lab/test environments.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DCNMAdministrationApi()
body = 'body_example' # str |  (optional)
dcnm_token = 'dcnm_token_example' # str |  (optional)
content_type = 'content_type_example' # str |  (optional)

try:
    # add user
    api_instance.fm_fmrest_dbadmin_add_user_post(body=body, dcnm_token=dcnm_token, content_type=content_type)
except ApiException as e:
    print("Exception when calling DCNMAdministrationApi->fm_fmrest_dbadmin_add_user_post: %s\n" % e)
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

# **rest_dcnm_version_get**
> rest_dcnm_version_get()

get version

Used to grab version value of DCNM application.  Does not require token for information.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DCNMAdministrationApi()

try:
    # get version
    api_instance.rest_dcnm_version_get()
except ApiException as e:
    print("Exception when calling DCNMAdministrationApi->rest_dcnm_version_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

