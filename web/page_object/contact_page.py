import time

import pytest
from selenium.webdriver.common.by import By

from web.page_object.base_page import BasePage


class ContactPage(BasePage):
    """
    通讯录页面
    """
    #定位 不止有界面元素，还有定位方式
    _memberAdd_acctid_locator = (By.ID, 'memberAdd_acctid')

    def  goto_add_member(self):
        # 跳转到添加成员页面
        # 如果A 导入B ， B导入A ，有循环导入的场景，那么
        # 只需要在方法内做导包操作即可避免
        from web.page_object.add_member_page import AddMemberPage
        return AddMemberPage(self.driver)

        pass

    def get_members(self):
        """
        获取成员信息
        :return:
        """
        #隐式等待，2秒内找到元素就开始执行，找不到就超时
        self.driver.implicitly_wait(2)
        #定位通讯录列表手机定位元素
        eles =self.driver.find_elements(By.CSS_SELECTOR,".member_colRight_memberTable_td:nth-child(5)")
        phone_list = []
        # 获得列表手机数据
        for c in eles:
            phone_list.append(c.text)
        #打印手机数据信息
        print(phone_list)
        #返回手机数据信息
        return phone_list

    def add_members(self,name,acctid,phone):
        """
        1、通讯录界面点击添加成员按钮
        2、输入成员的姓名、账号、手机，然后点击保存，返回到通讯录界面
        :return:
        """
        time.sleep(3)
        self.find(By.CSS_SELECTOR,'.js_add_member:nth-child(2)').click()
        self.find(By.ID, 'username').send_keys(name)
        self.find(self._memberAdd_acctid_locator).send_keys(acctid)
        self.find(By.CSS_SELECTOR, '.ww_telInput_mainNumber').send_keys(phone)
        self.find(By.CSS_SELECTOR, '.js_btn_save').click()
        return ContactPage(self.driver)

    def add_member_fail(self,name,acctid,phone):
        """
        1、先判断是否
        :param name:
        :param acctid:
        :param phone:
        :return:
        """