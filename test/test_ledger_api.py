"""
    Ledger API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1.10.0
    Contact: support@numary.com
    Generated by: https://openapi-generator.tech
"""


import unittest

import ledgerclient
from ledgerclient.api.ledger_api import LedgerApi  # noqa: E501


class TestLedgerApi(unittest.TestCase):
    """LedgerApi unit test stubs"""

    def setUp(self):
        self.api = LedgerApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_ledger_info(self):
        """Test case for get_ledger_info

        Get information about a ledger  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
