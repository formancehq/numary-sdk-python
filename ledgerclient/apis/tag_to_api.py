import typing_extensions

from ledgerclient.apis.tags import TagValues
from ledgerclient.apis.tags.ledger_api import LedgerApi
from ledgerclient.apis.tags.accounts_api import AccountsApi
from ledgerclient.apis.tags.balances_api import BalancesApi
from ledgerclient.apis.tags.transactions_api import TransactionsApi
from ledgerclient.apis.tags.server_api import ServerApi
from ledgerclient.apis.tags.mapping_api import MappingApi
from ledgerclient.apis.tags.logs_api import LogsApi
from ledgerclient.apis.tags.stats_api import StatsApi
from ledgerclient.apis.tags.script_api import ScriptApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.LEDGER: LedgerApi,
        TagValues.ACCOUNTS: AccountsApi,
        TagValues.BALANCES: BalancesApi,
        TagValues.TRANSACTIONS: TransactionsApi,
        TagValues.SERVER: ServerApi,
        TagValues.MAPPING: MappingApi,
        TagValues.LOGS: LogsApi,
        TagValues.STATS: StatsApi,
        TagValues.SCRIPT: ScriptApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.LEDGER: LedgerApi,
        TagValues.ACCOUNTS: AccountsApi,
        TagValues.BALANCES: BalancesApi,
        TagValues.TRANSACTIONS: TransactionsApi,
        TagValues.SERVER: ServerApi,
        TagValues.MAPPING: MappingApi,
        TagValues.LOGS: LogsApi,
        TagValues.STATS: StatsApi,
        TagValues.SCRIPT: ScriptApi,
    }
)
