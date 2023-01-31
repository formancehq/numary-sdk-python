# coding: utf-8

"""
    Ledger API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1.9.0-rc.8
    Contact: support@numary.com
    Generated by: https://openapi-generator.tech
"""

from ledgerclient.paths.ledger_balances.get import GetBalances
from ledgerclient.paths.ledger_aggregate_balances.get import GetBalancesAggregated


class BalancesApi(
    GetBalances,
    GetBalancesAggregated,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass
