"""
    Ledger API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1.10.0
    Contact: support@numary.com
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import ledgerclient
from ledgerclient.model.transaction import Transaction
globals()['Transaction'] = Transaction
from ledgerclient.model.transactions_response import TransactionsResponse


class TestTransactionsResponse(unittest.TestCase):
    """TransactionsResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testTransactionsResponse(self):
        """Test TransactionsResponse"""
        # FIXME: construct object with mandatory attributes with example values
        # model = TransactionsResponse()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
