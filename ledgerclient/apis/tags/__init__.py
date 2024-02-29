# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from ledgerclient.apis.tag_to_api import tag_to_api

import enum


class TagValues(str, enum.Enum):
    LEDGER = "Ledger"
    ACCOUNTS = "Accounts"
    BALANCES = "Balances"
    TRANSACTIONS = "Transactions"
    SERVER = "Server"
    MAPPING = "Mapping"
    LOGS = "Logs"
    STATS = "Stats"
    SCRIPT = "Script"
