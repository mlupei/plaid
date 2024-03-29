# coding: utf-8

"""
    Plaid Institutions API

    API for searching Plaid institutions.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.institutions_search_post200_response import InstitutionsSearchPost200Response

class TestInstitutionsSearchPost200Response(unittest.TestCase):
    """InstitutionsSearchPost200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> InstitutionsSearchPost200Response:
        """Test InstitutionsSearchPost200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `InstitutionsSearchPost200Response`
        """
        model = InstitutionsSearchPost200Response()
        if include_optional:
            return InstitutionsSearchPost200Response(
                institutions = [
                    openapi_client.models.institution.Institution(
                        institution_id = '', 
                        name = '', 
                        country_codes = [
                            ''
                            ], 
                        url = '', 
                        logo = '', 
                        primary_color = '', 
                        products = [
                            ''
                            ], )
                    ],
                request_id = ''
            )
        else:
            return InstitutionsSearchPost200Response(
        )
        """

    def testInstitutionsSearchPost200Response(self):
        """Test InstitutionsSearchPost200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
