from homework.wechat.util.data import load_data,get_wechat_token,generator_random_str,generator_mobile

BASE_URLS = load_data().get("wechat").get('baseUrl')
TOKEN = get_wechat_token()