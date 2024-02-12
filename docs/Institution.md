# Institution


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**institution_id** | **str** | The institution&#39;s ID in Plaid. | [optional] 
**name** | **str** | The institution&#39;s name. | [optional] 
**country_codes** | **List[str]** | The country codes where the institution operates. | [optional] 
**url** | **str** | The institution&#39;s official website URL. | [optional] 
**logo** | **str** | A URL to the institution&#39;s logo. | [optional] 
**primary_color** | **str** | The primary color of the institution in hexadecimal. | [optional] 
**products** | **List[str]** | The Plaid products that the institution supports. | [optional] 

## Example

```python
from openapi_client.models.institution import Institution

# TODO update the JSON string below
json = "{}"
# create an instance of Institution from a JSON string
institution_instance = Institution.from_json(json)
# print the JSON string representation of the object
print Institution.to_json()

# convert the object into a dict
institution_dict = institution_instance.to_dict()
# create an instance of Institution from a dict
institution_form_dict = institution.from_dict(institution_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


