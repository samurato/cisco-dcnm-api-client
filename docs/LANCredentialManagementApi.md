# swagger_client.LANCredentialManagementApi

All URIs are relative to *https://{{dcnm}}*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fm_fmrest_lan_config_get_lan_switch_credentials_get**](LANCredentialManagementApi.md#fm_fmrest_lan_config_get_lan_switch_credentials_get) | **GET** /fm/fmrest/lanConfig/getLanSwitchCredentials | get default lan credentials
[**fm_fmrest_lan_config_save_default_credentials_post**](LANCredentialManagementApi.md#fm_fmrest_lan_config_save_default_credentials_post) | **POST** /fm/fmrest/lanConfig/saveDefaultCredentials | update default lan credentials

# **fm_fmrest_lan_config_get_lan_switch_credentials_get**
> fm_fmrest_lan_config_get_lan_switch_credentials_get(dcnm_token=dcnm_token)

get default lan credentials

Retrieves LAN credentials currently present.  Will not display usernames or passwords in clear text.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LANCredentialManagementApi()
dcnm_token = 'dcnm_token_example' # str |  (optional)

try:
    # get default lan credentials
    api_instance.fm_fmrest_lan_config_get_lan_switch_credentials_get(dcnm_token=dcnm_token)
except ApiException as e:
    print("Exception when calling LANCredentialManagementApi->fm_fmrest_lan_config_get_lan_switch_credentials_get: %s\n" % e)
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

# **fm_fmrest_lan_config_save_default_credentials_post**
> fm_fmrest_lan_config_save_default_credentials_post(username=username, password=password, dcnm_token=dcnm_token, content_type=content_type)

update default lan credentials

Sends updated device credentials to DCNM.  Uses defined ENV vars

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LANCredentialManagementApi()
username = 'username_example' # str |  (optional)
password = 'password_example' # str |  (optional)
dcnm_token = 'dcnm_token_example' # str |  (optional)
content_type = 'content_type_example' # str |  (optional)

try:
    # update default lan credentials
    api_instance.fm_fmrest_lan_config_save_default_credentials_post(username=username, password=password, dcnm_token=dcnm_token, content_type=content_type)
except ApiException as e:
    print("Exception when calling LANCredentialManagementApi->fm_fmrest_lan_config_save_default_credentials_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | [optional] 
 **password** | **str**|  | [optional] 
 **dcnm_token** | **str**|  | [optional] 
 **content_type** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

