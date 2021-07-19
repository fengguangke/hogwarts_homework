"""
获取config下的data.yml配置文件的配置数据
"""
import yaml
import os.path as path
import requests
import random
import string

def load_data():
    """
    :return:
    """
    data_file = path.join(path.dirname(path.dirname(__file__)),'config/data.yml')
    with open(data_file) as f:
        data = yaml.safe_load(f)
    return data

def get_wechat_token():
    """
    :return:
    """
    data = load_data()
    corpid = data.get('wechat').get('corpid')
    corpsecret = data.get('wechat').get('corpsecret')
    url_token = data.get('wechat').get('baseUrl').get('token')
    query = {"corpid":corpid,"corpsecret":corpsecret}
    r = requests.get(url=url_token,params=query)
    r_json = r.json()
    if r_json.get('errcode') == 0:
        access_token = r_json.get('access_token')
        return access_token
    return None

def generator_random_str(prefix:str=None):
    """
    生成随机字符串
    :param prefix: 随机字符串前缀
    :return:
    """
    random_str = "".join(random.sample(string.ascii_letters+string.digits,8))
    return prefix+random_str if prefix else random_str

def generator_mobile(prefix:str=None):
    """
    生产随机手机号码
    :param prefix:
    :return:
    """
    random_str = "".join(random.sample(string.digits, 8))
    return prefix + random_str if prefix else random_str


if __name__ == '__main__':
    print(load_data())
    print(get_wechat_token())
    print(generator_random_str("hogwarts_"))
