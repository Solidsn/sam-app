import unittest

from src import app


class TestHandlerCase(unittest.TestCase):

    def test_reponse(self):
        event = {
                    "queryStringParameters": {
                        "personId": '1234'
                    }
                }
        print('testing response')
        result = app.lambda_handler(event, None)
        print(result)
        self.assertEqual(result['statusCode'], 200)
        self.assertIn(event['queryStringParameters']['personId'] + ' from Lambda', result['body'])