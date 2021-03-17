import unittest
import requests
import jsonpath
from API_Test_Fromwork.common.config_utils import config
from API_Test_Fromwork.common.public_api import get_access_token_api

class TestsGetAccessTokenApi(unittest.TestCase):
    def setUp(self) -> None:
        self.host=config.HOST
        self.session=requests.session()
    def tearDown(self) -> None:
        self.session.close()

    def test_01_getaccess_token(self):
        self._testMethodName='get_token'
        self._testMethodDoc='测试获取access_token'
        url_params = {
            'grant_type': 'client_credential',
            'appid': 'wxdc8562b5d4150019',
            'secret': 'ecd278da52077dade43b50ad7c7ddeb6'
        }
        response = get_access_token_api(self.session,url_params)
        json_body=response.json()
        access_token=jsonpath.jsonpath(json_body,'$.access_token')
        self.assertTrue(access_token)
        # print(json_body)

    def test02_(self):
        self._testMethodName='lack_secret'
        self._testMethodDoc='验证缺少secret参数获取token'
        url_params = {
            'grant_type': 'client_credential',
            'appid': 'wxdc8562b5d4150019',
            'secret': ''
        }
        response = requests.get(' https://%s/cgi-bin/token' % self.host,
                                params=url_params)
        json_body = response.json()
        # print(json_body)
        code = jsonpath.jsonpath(json_body, '$.errcode')[0]
        self.assertEqual(code,41004)

if __name__ == '__main__':
    unittest.main(verbosity=2)