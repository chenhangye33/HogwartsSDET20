from time import sleep

import yaml
from selenium import webdriver


class TestCookieLogin:
    def setup_class(self):
        self.driver = webdriver.Chrome()

    def test_get_cookies(self):
        #1、访问企业微信主页
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        #2、等待20秒扫码登录
        sleep(20)
        #3、等登录成功后 再去获取cookies
        cookie = self.driver.get_cookies()
        #4、将cookie存入一个可持久存储的地方，文件
        #打开文件的时候添加写入权限
        with open("cookie.yaml","w") as f:
            #第一个参数是要写入的数据
            yaml.safe_dump(cookie,f)


    # def test_add_cookies(self):
    #     # 1、访问企业微信主页
    #     self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
    #
    #     #2、定义cookie,cookie信息从文件中获取
    #     cookie = yaml.safe_load(open("cookie.yaml"))
    #      #3、植入cookie
    #     for c in cookie:
    #          self.driver.add_cookie(c)
    #
    #      #4、等待3秒,再次登录企业微信界面，发现无需扫码自动登录
    #     sleep(3)
    #     self.driver.get("https://work.weixin.qq.com/wework_admin/frame")

