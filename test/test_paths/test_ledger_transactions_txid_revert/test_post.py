# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

import unittest
from unittest.mock import patch

import urllib3

import ledgerclient
from ledgerclient.paths.ledger_transactions_txid_revert import post  # noqa: E501
from ledgerclient import configuration, schemas, api_client

from .. import ApiTestMixin


class TestLedgerTransactionsTxidRevert(ApiTestMixin, unittest.TestCase):
    """
    LedgerTransactionsTxidRevert unit test stubs
        Revert a ledger transaction by its ID.  # noqa: E501
    """
    _configuration = configuration.Configuration()

    def setUp(self):
        used_api_client = api_client.ApiClient(configuration=self._configuration)
        self.api = post.ApiForpost(api_client=used_api_client)  # noqa: E501

    def tearDown(self):
        pass

    response_status = 200




if __name__ == '__main__':
    unittest.main()
