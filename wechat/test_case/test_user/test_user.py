import pytest
import allure
from homework.wechat import generator_random_str,generator_mobile
from homework.wechat.departmentManagement import Department
from homework.wechat.userManagement import User

@allure.feature("成员管理接口测试")
class TestUser:

    def setup_class(self):
        self.depart = Department()
        self.user = User()

    @allure.story("添加成员")
    def test_add_user(self):
        userid = generator_random_str('hogwarts')
        name = generator_random_str('hogwarts_')
        department = self.depart.get_one_department().get('id')
        email = generator_random_str('hogwarts_email') + "@126.com"
        mobile = generator_mobile('135')
        result = self.user.add(userid=userid,name=name,department=[department],email=email,mobile=mobile)
        assert result == True

    @allure.story("删除成员")
    def test_delete_user(self):
        department = self.depart.get_one_department().get('id')
        userids = self.user.search_user(department_id=department,prefix='hogwarts')
        result = self.user.delete(userid=userids[0].get('userid'))
        assert result == True

    @allure.story("更新成员name")
    def test_update_user(self):
        department = self.depart.get_one_department().get('id')
        userids = self.user.search_user(department_id=department, prefix='hogwarts')
        name = generator_random_str('hogwarts_update_')
        result = self.user.update(userid=userids[0].get('userid'),name=name)
        assert result == True

    @allure.story("查询成员")
    def test_query_user(self):
        department = self.depart.get_one_department().get('id')
        userids = self.user.search_user(department_id=department, prefix='hogwarts')
        result = self.user.query(userid=userids[0].get('userid'))
        assert result.get('errcode') == 0
        assert result.get('userid') == userids[0].get('userid')
