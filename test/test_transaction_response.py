"""
    Ledger API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1.10.0-rc.2
    Contact: support@numary.com
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import ledgerclient
from ledgerclient.model.transaction import Transaction
globals()['Transaction'] = Transaction
from ledgerclient.model.transaction_response import TransactionResponse


class TestTransactionResponse(unittest.TestCase):
    """TransactionResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testTransactionResponse(self):
        """Test TransactionResponse"""
        # FIXME: construct object with mandatory attributes with example values
        # model = TransactionResponse()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
