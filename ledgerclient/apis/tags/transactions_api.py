# coding: utf-8

"""
    Ledger API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1.9.0-rc.10
    Contact: support@numary.com
    Generated by: https://openapi-generator.tech
"""

from ledgerclient.paths.ledger_transactions_txid_metadata.post import AddMetadataOnTransaction
from ledgerclient.paths.ledger_transactions.head import CountTransactions
from ledgerclient.paths.ledger_transactions.post import CreateTransaction
from ledgerclient.paths.ledger_transactions_batch.post import CreateTransactions
from ledgerclient.paths.ledger_transactions_txid.get import GetTransaction
from ledgerclient.paths.ledger_transactions.get import ListTransactions
from ledgerclient.paths.ledger_transactions_txid_revert.post import RevertTransaction


class TransactionsApi(
    AddMetadataOnTransaction,
    CountTransactions,
    CreateTransaction,
    CreateTransactions,
    GetTransaction,
    ListTransactions,
    RevertTransaction,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass
