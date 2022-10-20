# swagger_client.ImagePackageManagementApi

All URIs are relative to *https://{{dcnm}}*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_imagemanagement_job_job_id_get**](ImagePackageManagementApi.md#rest_imagemanagement_job_job_id_get) | **GET** /rest/imagemanagement/job/{job_id} | get job details
[**rest_imagemanagement_job_post**](ImagePackageManagementApi.md#rest_imagemanagement_job_post) | **POST** /rest/imagemanagement/job | upgrade nxos
[**rest_packagemgnt_activate_post**](ImagePackageManagementApi.md#rest_packagemgnt_activate_post) | **POST** /rest/packagemgnt/activate | uninstall package
[**rest_packagemgnt_packages_get**](ImagePackageManagementApi.md#rest_packagemgnt_packages_get) | **GET** /rest/packagemgnt/packages | get all active and inactive packages
[**rest_packagemgnt_uploaded_packages_get**](ImagePackageManagementApi.md#rest_packagemgnt_uploaded_packages_get) | **GET** /rest/packagemgnt/uploaded-packages | get available uploaded packages
[**rest_poap_servers_smart_image_delete**](ImagePackageManagementApi.md#rest_poap_servers_smart_image_delete) | **DELETE** /rest/poap/servers/smart-image | delete image
[**rest_poap_servers_smart_image_upload_post**](ImagePackageManagementApi.md#rest_poap_servers_smart_image_upload_post) | **POST** /rest/poap/servers/SmartImageUpload | image upload
[**rest_poap_servers_uploaded_images_table_get**](ImagePackageManagementApi.md#rest_poap_servers_uploaded_images_table_get) | **GET** /rest/poap/servers/uploaded-images-table | get all uploaded images

# **rest_imagemanagement_job_job_id_get**
> rest_imagemanagement_job_job_id_get(job_id, content_type=content_type, dcnm_token=dcnm_token)

get job details

Retrieves the status of an image compatibility or upgrade job

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ImagePackageManagementApi()
job_id = 'job_id_example' # str | 
content_type = 'content_type_example' # str |  (optional)
dcnm_token = 'dcnm_token_example' # str |  (optional)

try:
    # get job details
    api_instance.rest_imagemanagement_job_job_id_get(job_id, content_type=content_type, dcnm_token=dcnm_token)
except ApiException as e:
    print("Exception when calling ImagePackageManagementApi->rest_imagemanagement_job_job_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**|  | 
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

# **rest_imagemanagement_job_post**
> rest_imagemanagement_job_post(body=body, dcnm_token=dcnm_token)

upgrade nxos

Uses same endpoint as compatibility check, but with unique payload for image upgrade.   Full payload example: ``` Example Body: {\"id\":\"1\",\"eraseStartUp\":false,\"saverunningConfig\":true,\"archiveFailureLog\":true,\"concurrentExec\":true,\"executeImmediately\":false, \"comments\":\"\",\"jobOwner\":\"admin\",\"jobType\":0,\"strScheduledTime\":\"Apr/26/2019,11:30:00\",\"strJobCreationTime\":\"Apr/26/2019,11:30:00\", \"maintenanceMode\":false,\"skipDisruptiveUpgrade\":false,\"taskList\":[{\"kickStartImage\":\"/NotApplicable\",\"systemImageFile\":\"/var/lib/dcnm/images/nxos.9.2.3.bin\", \"ssiImageFile\":\"/NotApplicable\",\"installLog\":\"\",\"taskAction\":\"Completed\",\"statusDescr\":\"\",\"compatibilty_desc\":\"Disruptiveupgrade\", \"path\":null,\"strStatus\":\"NA\",\"strCompStatus\":\"SUCCESS\",\"vrfSelected\":\"management\",\"actionType\":0,\"sequence\":1,\"jobId\":1,\"bdualSup\":false, \"strScheduledTime\":null,\"strCompletedTime\":null,\"bMaintenanceMode\":false,\"parallelLineCardUpgrade\":false,\"noReload\":false,\"nonDisruptive\":false, \"nonInterruptive\":true,\"biosForce\":false,\"id\":2,\"hostName\":\"spine-1\",\"ipAddress\":\"10.195.198.244\",\"platform\":\"N9K\",\"version\":\"7.0(3)I7(6)\", \"serverName\":\"Default_SCP_Repository\",\"maintenanceDesc\":null,\"type\":\"SERVER\",\"status\":\"NA\",\"compatibilty_status\":\"SUCCESS\"}]}  ```

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ImagePackageManagementApi()
body = NULL # object |  (optional)
dcnm_token = 'dcnm_token_example' # str |  (optional)

try:
    # upgrade nxos
    api_instance.rest_imagemanagement_job_post(body=body, dcnm_token=dcnm_token)
except ApiException as e:
    print("Exception when calling ImagePackageManagementApi->rest_imagemanagement_job_post: %s\n" % e)
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

# **rest_packagemgnt_activate_post**
> rest_packagemgnt_activate_post(body=body, dcnm_token=dcnm_token, content_type=content_type)

uninstall package

Uninstalls package from device

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ImagePackageManagementApi()
body = 'body_example' # str |  (optional)
dcnm_token = 'dcnm_token_example' # str |  (optional)
content_type = 'content_type_example' # str |  (optional)

try:
    # uninstall package
    api_instance.rest_packagemgnt_activate_post(body=body, dcnm_token=dcnm_token, content_type=content_type)
except ApiException as e:
    print("Exception when calling ImagePackageManagementApi->rest_packagemgnt_activate_post: %s\n" % e)
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

# **rest_packagemgnt_packages_get**
> rest_packagemgnt_packages_get(dcnm_token=dcnm_token)

get all active and inactive packages

Lists all active and inactive RPMs/SMUs within DCNM

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ImagePackageManagementApi()
dcnm_token = 'dcnm_token_example' # str |  (optional)

try:
    # get all active and inactive packages
    api_instance.rest_packagemgnt_packages_get(dcnm_token=dcnm_token)
except ApiException as e:
    print("Exception when calling ImagePackageManagementApi->rest_packagemgnt_packages_get: %s\n" % e)
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

# **rest_packagemgnt_uploaded_packages_get**
> rest_packagemgnt_uploaded_packages_get(dcnm_token=dcnm_token)

get available uploaded packages

Lists all active and inactive RPMs/SMUs within DCNM

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ImagePackageManagementApi()
dcnm_token = 'dcnm_token_example' # str |  (optional)

try:
    # get available uploaded packages
    api_instance.rest_packagemgnt_uploaded_packages_get(dcnm_token=dcnm_token)
except ApiException as e:
    print("Exception when calling ImagePackageManagementApi->rest_packagemgnt_uploaded_packages_get: %s\n" % e)
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

# **rest_poap_servers_smart_image_delete**
> rest_poap_servers_smart_image_delete(dcnm_token=dcnm_token)

delete image

Removes image from DCNM image store

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ImagePackageManagementApi()
dcnm_token = 'dcnm_token_example' # str |  (optional)

try:
    # delete image
    api_instance.rest_poap_servers_smart_image_delete(dcnm_token=dcnm_token)
except ApiException as e:
    print("Exception when calling ImagePackageManagementApi->rest_poap_servers_smart_image_delete: %s\n" % e)
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

# **rest_poap_servers_smart_image_upload_post**
> rest_poap_servers_smart_image_upload_post(image_file_name=image_file_name, dcnm_token=dcnm_token, content_type=content_type)

image upload

Uploads an image to DCNM

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ImagePackageManagementApi()
image_file_name = 'image_file_name_example' # str |  (optional)
dcnm_token = 'dcnm_token_example' # str |  (optional)
content_type = 'content_type_example' # str |  (optional)

try:
    # image upload
    api_instance.rest_poap_servers_smart_image_upload_post(image_file_name=image_file_name, dcnm_token=dcnm_token, content_type=content_type)
except ApiException as e:
    print("Exception when calling ImagePackageManagementApi->rest_poap_servers_smart_image_upload_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image_file_name** | **str**|  | [optional] 
 **dcnm_token** | **str**|  | [optional] 
 **content_type** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_poap_servers_uploaded_images_table_get**
> rest_poap_servers_uploaded_images_table_get(dcnm_token=dcnm_token)

get all uploaded images

Retrieves a table of all uploaded NXOS images within DCNM

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ImagePackageManagementApi()
dcnm_token = 'dcnm_token_example' # str |  (optional)

try:
    # get all uploaded images
    api_instance.rest_poap_servers_uploaded_images_table_get(dcnm_token=dcnm_token)
except ApiException as e:
    print("Exception when calling ImagePackageManagementApi->rest_poap_servers_uploaded_images_table_get: %s\n" % e)
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

