# swagger_client.DefaultApi

All URIs are relative to *https://{{dcnm}}*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_logon_post**](DefaultApi.md#rest_logon_post) | **POST** /rest/logon | dcnm login - gather token

# **rest_logon_post**
> rest_logon_post(body=body, content_type=content_type)

dcnm login - gather token

Used to gather the DCNM token for API operations.  Authenticates using encoding of the username and password defined within the ENV.  The returned key is added to an ENV var for use by every other DCNM API call using a JS test.  Timeout value is excessively long for testing purposes and is defined in milliseconds

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
body = 'body_example' # str |  (optional)
content_type = 'content_type_example' # str |  (optional)

try:
    # dcnm login - gather token
    api_instance.rest_logon_post(body=body, content_type=content_type)
except ApiException as e:
    print("Exception when calling DefaultApi->rest_logon_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**str**](str.md)|  | [optional] 
 **content_type** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

