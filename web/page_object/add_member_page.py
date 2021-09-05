'''
(1)使用po思想完成添加成员操作的自动化测试
(2)要求: 至少每个函数添加注释；基础薄弱的同学尽量每行添加注释
'''
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from web.page_object.base_page import BasePage

class AddMemberPage(BasePage):
    #定义私有变量_username、_memberAdd_acctid、_phone，私有变量以"_"开头
    _username=(By.ID,'username')
    _memberAdd_acctid=(By.ID,'memberAdd_acctid')
    _phone=(By.CSS_SELECTOR,'.ww_telInput_mainNumber')

    #添加成员的姓名、账号、手机，然后点击保存，返回到通讯录界面
    def add_member(self,name,acctid,phone):
        from web.page_object.contact_page import ContactPage
        self.find(self._username).send_keys(name)
        self.find(self._memberAdd_acctid).send_keys(acctid)
        self.find(self._phone).send_keys(phone)
        self.find(By.CSS_SELECTOR,'.js_btn_save').click()
        return ContactPage(self.driver)

    def add_member_fail(self,name,acctid,phone):
        """
        添加成员失败
        因为根据业务逻辑的不同，所以封装不同的场景
        :param acctid:
        :param phone:
        :return:断言添加成员失败的一个场景，返回异常信息，用作断言
        """
        self.find(self._username).send_keys(name)
        self.find(self._memberAdd_acctid).send_keys(acctid)
        self.find(self._phone).send_keys(phone)
        #获得已有账号的报错信息
        time.sleep(3)
        messages=self.driver.find_elements(By.CSS_SELECTOR,'.ww_inputWithTips_tips')
        error_messages = []
        # 获得报错信息中的txt
        for c in messages:
            error_messages.append(c.text)
        print(f"已有账号的报错信息{error_messages}")
        # 返回手机数据信息
        return error_messages

