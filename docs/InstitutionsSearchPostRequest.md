# InstitutionsSearchPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_id** | **str** | Your Plaid client ID. | 
**secret** | **str** | Your Plaid secret. | 
**query** | **str** | The query string to search institutions. | 
**products** | **List[str]** | List of Plaid products to filter institutions. | [optional] 
**country_codes** | **List[str]** | An array of country codes, used to filter institutions. | 

## Example

```python
from openapi_client.models.institutions_search_post_request import InstitutionsSearchPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of InstitutionsSearchPostRequest from a JSON string
institutions_search_post_request_instance = InstitutionsSearchPostRequest.from_json(json)
# print the JSON string representation of the object
print InstitutionsSearchPostRequest.to_json()

# convert the object into a dict
institutions_search_post_request_dict = institutions_search_post_request_instance.to_dict()
# create an instance of InstitutionsSearchPostRequest from a dict
institutions_search_post_request_form_dict = institutions_search_post_request.from_dict(institutions_search_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


