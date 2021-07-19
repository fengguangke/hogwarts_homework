from homework.wechat import BASE_URLS,TOKEN
import requests

class Department:
    path_add = "/create"
    path_update = "/update"
    path_delete = "/delete"
    path_query = "/list"

    def __init__(self):
        self._base_url = BASE_URLS.get('department')

    def add(self):
        pass

    def update(self):
        pass

    def delete(self):
        pass

    def query(self,**kwargs):
        """
        获取部门列表
        :param kwargs: {id:部门id},获取指定部门及其下的子部门（以及及子部门的子部门等等，递归）。 如果不填，默认获取全量组织架构
        :return:list,部门列表
       """
        url = self._base_url + self.path_query
        param = {"access_token":TOKEN}
        param.update(**kwargs)
        r = requests.get(url=url,params=param)
        r_json = r.json()
        if r_json.get('errcode') == 0:
            return r_json.get('department')
        return None

    def get_one_department(self,**kwargs):
        """
        获取一个部门信息
        :return:
        """
        deparrments = self.query(**kwargs)
        if not deparrments:
            print("获取部门列表失败")
        else:
            return deparrments[0]


if __name__ == '__main__':
    print(Department().query())