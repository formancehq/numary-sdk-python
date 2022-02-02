import json

from ledgerclient import rest
from ledgerclient.configuration import Configuration

StagingAuthEndpoint = "https://api.staging.numary.cloud/auth/authenticate/tokens"
ProdAuthEndpoint = "https://api.numary.cloud/auth/authenticate/tokens"

StagingLedgerEndpoint = "https://api.staging.numary.cloud/ledger"
ProdLedgerEndpoint = "https://api.numary.cloud/auth/ledger"


class TokenFetcher(object):
    def __init__(self, url, token):
        self.url = url;
        self.token = token;

    def fetch_token(self):
        config = Configuration()
        client = rest.RESTClientObject(config)
        ret = client.POST(self.url, headers={
            'Content-Type': 'application/json'
        }, body={
            'strategy': 'm2m',
            'token': self.token
        })
        return json.loads(ret.data)['data']['jwt']