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
from ledgerclient.model.aggregated_volumes import AggregatedVolumes
from ledgerclient.model.metadata import Metadata
from ledgerclient.model.posting import Posting
globals()['AggregatedVolumes'] = AggregatedVolumes
globals()['Metadata'] = Metadata
globals()['Posting'] = Posting
from ledgerclient.model.transaction import Transaction


class TestTransaction(unittest.TestCase):
    """Transaction unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testTransaction(self):
        """Test Transaction"""
        # FIXME: construct object with mandatory attributes with example values
        # model = Transaction()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
