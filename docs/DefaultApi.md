# openapi_client.DefaultApi

All URIs are relative to *https://sandbox.plaid.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**institutions_search_post**](DefaultApi.md#institutions_search_post) | **POST** /institutions/search | Search institutions


# **institutions_search_post**
> InstitutionsSearchPost200Response institutions_search_post(institutions_search_post_request)

Search institutions

Allows clients to search institutions by name or other criteria.

### Example


```python
import openapi_client
from openapi_client.models.institutions_search_post200_response import InstitutionsSearchPost200Response
from openapi_client.models.institutions_search_post_request import InstitutionsSearchPostRequest
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sandbox.plaid.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://sandbox.plaid.com"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    institutions_search_post_request = openapi_client.InstitutionsSearchPostRequest() # InstitutionsSearchPostRequest | 

    try:
        # Search institutions
        api_response = api_instance.institutions_search_post(institutions_search_post_request)
        print("The response of DefaultApi->institutions_search_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->institutions_search_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **institutions_search_post_request** | [**InstitutionsSearchPostRequest**](InstitutionsSearchPostRequest.md)|  | 

### Return type

[**InstitutionsSearchPost200Response**](InstitutionsSearchPost200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of institutions that match the search criteria. |  -  |
**400** | Bad request, such as missing required parameters. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

