import pytest
from web.page_object.index_page import IndexPage


class TestAddMember:
    """
    测试用例类
    """

    #参数化
    @pytest.mark.parametrize("name,acctid,phone", [('绿萝','apple7','13812345677'),('绣球','apple8','13812345678')],ids=['添加成员绿萝','添加成员三角梅'])
    def test_add_member(self,name,acctid,phone):
        """
        1. 在首页点击添加成员
        2. 在添加成员填充成员信息， 姓名、手机号、账号
        3. 在添加成员页面点击保存
        4. 在通讯录页面查看成员是否保存成功
        5. 在通讯录页面添加成员点击保存
        6. 在通讯录页面添加成员是否保存成功
        """
        # 获得一个index实例对象
        index = IndexPage()
        #添加成员
        name_list = index.goto_add_member().add_member(name,acctid,phone).get_members()
        assert "13812345677" in name_list

    # 添加成员失败参数化
    @pytest.mark.parametrize("name,acctid,phone", [('绣球', 'apple8','11111111111')],ids=['添加成员绣球失败'])
    def test_add_member_fail(self,name,acctid,phone):
        """
                1. 在首页点击添加成员
                2. 在添加成员填充已有成员信息， 姓名、手机号、账号
                3. 查看是否返回该账号已被占有的报错信息
                """

        # 获得一个index实例对象
        index = IndexPage()
        # 添加成员绣球，提取报错信息
        error_message = index.goto_add_member().add_member_fail(name,acctid,phone)
        # print(error_message)
        #跟name拼接报错信息
        name_error_message='该帐号已被“'+name+'”占有'
        #断言
        assert name_error_message in  error_message



