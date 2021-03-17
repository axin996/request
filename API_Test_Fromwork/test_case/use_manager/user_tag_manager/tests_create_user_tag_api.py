import requests
import unittest
import jsonpath
import json
from API_Test_Fromwork.common.config_utils import config

class TestCreatUserTagApi(unittest.TestCase):
    def setUp(self) -> None:
        self.host=config.HOST
        self.session=requests.session()
    def tearDown(self) -> None:
        self.session.close()

    def test01_tag_repeat(self):
        url_params = {
            'grant_type': 'client_credential',
            'appid': 'wxdc8562b5d4150019',
            'secret': 'ecd278da52077dade43b50ad7c7ddeb6'
        }
        response = requests.get('https://%s/cgi-bin/token' % self.host,
                                params=url_params)
        json_body = response.json()
        access_token = jsonpath.jsonpath(json_body, '$.access_token')

        url_params = {'access_token': access_token}
        data_params = {
            'tag': {'name': '大学生组6'}
        }
        data_json_params = json.dumps(data_params, ensure_ascii=False)
        response = requests.post(url='https://api.weixin.qq.com/cgi-bin/tags/create',
                                  params=url_params,
                                  data=data_json_params.encode('utf-8'))
        json_body = response.json()
        # print(json_body)
        code = jsonpath.jsonpath(json_body, '$.errcode')[0]
        self.assertEqual(code, 45157)

if __name__ == '__main__':
    unittest.main()