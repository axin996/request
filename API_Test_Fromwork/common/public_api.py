from API_Test_Fromwork.common.config_utils import config
import json

def get_access_token_api(session,url_params):
    response = session.get('https://%s/cgi-bin/token' % config.HOST,
                            params=url_params)
    return response

def create_user_tag_api(session,url_params,post_date):
    data_json_params = json.dumps(post_date, ensure_ascii=False)
    response = session.post(url='https://api.weixin.qq.com/cgi-bin/tags/create',
                             params=url_params,
                             data=data_json_params.encode('utf-8'))
    return response