import json

from ledgerclient import rest
from ledgerclient.configuration import Configuration

AuthEndpoint = "https://api.numary.cloud/auth/authenticate/tokens"
LedgerEndpoint = "https://api.numary.cloud/auth/ledger"


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