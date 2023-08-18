# coding: utf-8

"""
    Ledger API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1.10.6
    Contact: support@numary.com
    Generated by: https://openapi-generator.tech
"""

from ledgerclient.paths.ledger_accounts_address_metadata.post import AddMetadataToAccount
from ledgerclient.paths.ledger_accounts.head import CountAccounts
from ledgerclient.paths.ledger_accounts_address.get import GetAccount
from ledgerclient.paths.ledger_accounts.get import ListAccounts


class AccountsApi(
    AddMetadataToAccount,
    CountAccounts,
    GetAccount,
    ListAccounts,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass
