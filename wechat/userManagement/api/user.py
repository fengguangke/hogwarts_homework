from homework.wechat import BASE_URLS,TOKEN
import requests


class User:
    path_add = "/create"
    path_query = "/get"
    path_update = "/update"
    path_delete = "/delete"
    path_search = "/simplelist"

    def __init__(self):
        self._base_url = BASE_URLS.get('user')

    def add(self,userid, name, department, **kwargs):
        """
        创建成员
        :param userid:
        :param name:
        :param department:
        :param kwargs:
        :return:
        """
        url = self._base_url + self.path_add
        param = {"access_token":TOKEN}
        body = {"userid": userid, "name": name, "department": department}
        mobile = kwargs.get('mobile')
        email = kwargs.get('email')
        if not mobile and not email:
            print("mobile/email不能同时为空!")
        body.update(**kwargs)
        r = requests.post(url=url,params=param,json=body)
        r_json = r.json()
        if r_json.get('errcode') == 0:
            return True
        return False

    def update(self,userid,**kwargs):
        """
        更新成员
        :param userid:
        :return:
        """
        url = self._base_url + self.path_update
        param = {"access_token": TOKEN}
        body = {"userid": userid}
        body.update(**kwargs)
        r = requests.post(url=url, params=param, json=body)
        r_json = r.json()
        if r_json.get('errcode') == 0:
            return True
        return False

    def delete(self, userid):
        """
        删除成员
        :param userid:
        :return:
        """
        url = self._base_url + self.path_delete
        param = {"access_token": TOKEN}
        param.update({"userid": userid})
        r = requests.get(url=url, params=param)
        r_json = r.json()
        if r_json.get('errcode') == 0:
            return True
        return False

    def query(self, userid):
        """
        读取成员
        :param userid:
        :return:
        """
        url = self._base_url + self.path_query
        param = {"access_token": TOKEN}
        param.update({"userid": userid})
        r = requests.get(url=url, params=param)
        r_json = r.json()
        return r_json

    def search_user(self,department_id,prefix:str=None,**kwargs):
        """
        搜索userid以prefix开头的成员
        :param department_id:
        :param prefix:
        :return:
        """
        url = self._base_url + self.path_search
        param = {"access_token": TOKEN}
        param.update({"department_id": department_id})
        param.update(**kwargs)
        r = requests.get(url=url, params=param)
        r_json = r.json()
        if r_json.get('errcode') == 0:
            userlist = r_json.get('userlist')
            filter_user = list(filter(lambda x: x.get('userid').startswith(prefix),userlist))
            return filter_user
        return None

