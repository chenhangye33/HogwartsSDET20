import time
from time import sleep

import yaml
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
     #定义私有变量
    _base_url="https://work.weixin.qq.com/wework_admin/frame"
    def __init__(self,base_driver: WebDriver=None):
        '''

        :param base_driver: 起到的作用是传递driver对象
        '''
        #如果没有给base_driver赋值，那么默认值为None
        if base_driver == None:
            #driver初始化
            self.driver = webdriver.Chrome()

            #进入index界面
            self.driver.get(self._base_url)
            # 定义cookie,cookie信息从文件中获取
            cookie = yaml.safe_load(open("../conf/cookie.yaml"))
            #加入隐式等待
            self.driver.implicitly_wait(3)
            # time.sleep(3)
            # 植入cookie
            for c in cookie:
                self.driver.add_cookie(c)

            #打开企业微信主页
            self.driver.get(self._base_url)

        else:
            #base_driver是一个形参，传递Driver对象，即我们的浏览器驱动
            self.driver =base_driver


    def find(self,by,locator=None):
            '''
             by:定位方式
             locator:定位元素s
            :return:
            '''
            #如果locator = None，则传入的式一个元组
            #元组解包 （by,locator）,*（by，locator）分别以by，locator形式传入
            if locator == None:
                 ele = self.driver.find_element(*by)
            else:
                 ele = self.driver.find_element(by=by, value=locator)
            print(f"返回定位元素{ele}")
            return ele