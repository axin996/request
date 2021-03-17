import requests
import unittest
class test_request(unittest.TestCase):
    def setUp(self) -> None:
        self.host='api.weixin.qq.com'
        self.seesion=requests.session()
    def tearDown(self) -> None:
        self.seesion.close()

    def test01(self):
        url_params={
            'grant_type':'client_credential',
            'appid':'wxdc8562b5d4150019',
            'secret':'ecd278da52077dade43b50ad7c7ddeb6'
        }
        response = requests.get(' https://%s/cgi-bin/token'%self.host,
                                params=url_params)
        print(response.content.decode('utf-8'))

if __name__ == '__main__':
    unittest.main()
    #suite=unittest.TestSuite