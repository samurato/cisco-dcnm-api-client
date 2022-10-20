# swagger_client.TemplateOperationsApi

All URIs are relative to *https://{{dcnm}}*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_config_templates_get**](TemplateOperationsApi.md#rest_config_templates_get) | **GET** /rest/config/templates/ | get all templates
[**rest_config_templates_telemetry_config_delete**](TemplateOperationsApi.md#rest_config_templates_telemetry_config_delete) | **DELETE** /rest/config/templates/telemetry_config | delete template
[**rest_config_templates_telemetry_config_get**](TemplateOperationsApi.md#rest_config_templates_telemetry_config_get) | **GET** /rest/config/templates/telemetry_config | get specific template
[**rest_config_templates_telemetry_config_populate_post**](TemplateOperationsApi.md#rest_config_templates_telemetry_config_populate_post) | **POST** /rest/config/templates/telemetry_config/populate | template variable population
[**rest_config_templates_telemetry_config_put**](TemplateOperationsApi.md#rest_config_templates_telemetry_config_put) | **PUT** /rest/config/templates/telemetry_config | update  template config
[**rest_config_templates_template_post**](TemplateOperationsApi.md#rest_config_templates_template_post) | **POST** /rest/config/templates/template | create template config
[**rest_config_templates_validate_post**](TemplateOperationsApi.md#rest_config_templates_validate_post) | **POST** /rest/config/templates/validate | validate template data

# **rest_config_templates_get**
> rest_config_templates_get(dcnm_token=dcnm_token, content_type=content_type)

get all templates

Query all configuration templates defined inside of DCNM (includes both system- and user-defined templates)

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TemplateOperationsApi()
dcnm_token = 'dcnm_token_example' # str |  (optional)
content_type = 'content_type_example' # str |  (optional)

try:
    # get all templates
    api_instance.rest_config_templates_get(dcnm_token=dcnm_token, content_type=content_type)
except ApiException as e:
    print("Exception when calling TemplateOperationsApi->rest_config_templates_get: %s\n" % e)
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

# **rest_config_templates_telemetry_config_delete**
> rest_config_templates_telemetry_config_delete(dcnm_token=dcnm_token, content_type=content_type)

delete template

Removes the template defined in the URI from DCNM

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TemplateOperationsApi()
dcnm_token = 'dcnm_token_example' # str |  (optional)
content_type = 'content_type_example' # str |  (optional)

try:
    # delete template
    api_instance.rest_config_templates_telemetry_config_delete(dcnm_token=dcnm_token, content_type=content_type)
except ApiException as e:
    print("Exception when calling TemplateOperationsApi->rest_config_templates_telemetry_config_delete: %s\n" % e)
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

# **rest_config_templates_telemetry_config_get**
> rest_config_templates_telemetry_config_get(dcnm_token=dcnm_token, content_type=content_type, populate=populate)

get specific template

Gathers the specific configuration template as defined by the name of the template within the URI

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TemplateOperationsApi()
dcnm_token = 'dcnm_token_example' # str |  (optional)
content_type = 'content_type_example' # str |  (optional)
populate = true # bool |  (optional)

try:
    # get specific template
    api_instance.rest_config_templates_telemetry_config_get(dcnm_token=dcnm_token, content_type=content_type, populate=populate)
except ApiException as e:
    print("Exception when calling TemplateOperationsApi->rest_config_templates_telemetry_config_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dcnm_token** | **str**|  | [optional] 
 **content_type** | **str**|  | [optional] 
 **populate** | **bool**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_config_templates_telemetry_config_populate_post**
> rest_config_templates_telemetry_config_populate_post(body=body, content_type=content_type, dcnm_token=dcnm_token)

template variable population

Creates the configuration output from a template given the inputs defined within the payload of this request and the name of the template defined in the URI

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TemplateOperationsApi()
body = 'body_example' # str |  (optional)
content_type = 'content_type_example' # str |  (optional)
dcnm_token = 'dcnm_token_example' # str |  (optional)

try:
    # template variable population
    api_instance.rest_config_templates_telemetry_config_populate_post(body=body, content_type=content_type, dcnm_token=dcnm_token)
except ApiException as e:
    print("Exception when calling TemplateOperationsApi->rest_config_templates_telemetry_config_populate_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **rest_config_templates_telemetry_config_put**
> rest_config_templates_telemetry_config_put(body=body, dcnm_token=dcnm_token, content_type=content_type)

update  template config

Updates the configuration defined in an existing template within DCNM

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TemplateOperationsApi()
body = 'body_example' # str |  (optional)
dcnm_token = 'dcnm_token_example' # str |  (optional)
content_type = 'content_type_example' # str |  (optional)

try:
    # update  template config
    api_instance.rest_config_templates_telemetry_config_put(body=body, dcnm_token=dcnm_token, content_type=content_type)
except ApiException as e:
    print("Exception when calling TemplateOperationsApi->rest_config_templates_telemetry_config_put: %s\n" % e)
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

# **rest_config_templates_template_post**
> rest_config_templates_template_post(body=body, dcnm_token=dcnm_token, content_type=content_type)

create template config

Creates a configuration template within DCNM using the verified configuration data from the verification step

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TemplateOperationsApi()
body = 'body_example' # str |  (optional)
dcnm_token = 'dcnm_token_example' # str |  (optional)
content_type = 'content_type_example' # str |  (optional)

try:
    # create template config
    api_instance.rest_config_templates_template_post(body=body, dcnm_token=dcnm_token, content_type=content_type)
except ApiException as e:
    print("Exception when calling TemplateOperationsApi->rest_config_templates_template_post: %s\n" % e)
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

# **rest_config_templates_validate_post**
> rest_config_templates_validate_post(body=body, dcnm_token=dcnm_token)

validate template data

Validates the structure of a given template configuration against the DCNM syntax and language.  This input is strictly a string in nature

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TemplateOperationsApi()
body = 'body_example' # str |  (optional)
dcnm_token = 'dcnm_token_example' # str |  (optional)

try:
    # validate template data
    api_instance.rest_config_templates_validate_post(body=body, dcnm_token=dcnm_token)
except ApiException as e:
    print("Exception when calling TemplateOperationsApi->rest_config_templates_validate_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**str**](str.md)|  | [optional] 
 **dcnm_token** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

