import unittest
from Practica5_strategy import *

class StrategyTest(unittest.TestCase):

    def test_basic_auth_strategy(self):
        context = AuthContext(BasicAuthConcreteStrategy(usr='tintin', passwd='123456'))
        self.assertEqual(
            context.authenticate(),
            '### Authenticated with Basic Auth\n\tUser: tintin\n\tPass: 123456'
        )

    def test_oauth_strategy(self):
        cred = {
            "access_token": "una cadena muy larga",
            "token_type": "Bearer",
            "expires_in": 3600,
            "refresh_token": "una cadena muy larga 2",
            "scope": "readAndWrite"
        }
        context = AuthContext(OauthAuthConcreteStrategy(credentials=cred))
        self.assertEqual(
            context.authenticate(),
            '### Authenticated with OAuth\n\tCredentials: {"access_token":"una cadena muy larga","token_type":"Bearer","expires_in":3600,"refresh_token":"una cadena muy larga 2","scope":"readAndWrite"}'
        )

    def test_api_key_strategy(self):
        context = AuthContext(ApiKeyConcreteStrategy(api_key='tintin-123456'))
        self.assertEqual(
            context.authenticate(),
            '### Authenticated with API Key\n\tKey: tintin-123456'
        )

    def test_default_strategy(self):
        self.assertEqual(
            AuthContext().authenticate(),
            '### Authenticated with OAuth\n\tCredentials: {"access_token":"una cadena muy larga","token_type":"Bearer","expires_in":3600,"refresh_token":"una cadena muy larga 2","scope":"default"}'
        )

    def test_updating_strategy(self):
        context = AuthContext(BasicAuthConcreteStrategy(usr='tintin', passwd='123456'))
        self.assertEqual(
            context.authenticate(),
            '### Authenticated with Basic Auth\n\tUser: tintin\n\tPass: 123456'
        )
        context.set_strategy(ApiKeyConcreteStrategy(api_key='tintin-123456'))
        self.assertEqual(
            context.authenticate(),
            '### Authenticated with API Key\n\tKey: tintin-123456'
        )

if __name__ == "__main__":
    unittest.main() 