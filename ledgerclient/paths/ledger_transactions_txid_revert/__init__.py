# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from ledgerclient.paths.ledger_transactions_txid_revert import Api

from ledgerclient.paths import PathValues

path = PathValues.LEDGER_TRANSACTIONS_TXID_REVERT