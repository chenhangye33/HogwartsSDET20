from time import sleep
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
        print(cookie)


    def test_add_cookies(self):
        # 1、访问企业微信主页
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")

        #2、定义cookie,先黏贴，再优化
        cookie = [{'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False, 'value': '1688851921258419'},
                  {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False, 'value': '1970325112169054'},
                  {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False, 'value': '1688851921258419'},
                  {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False, 'value': 'direct'},
                  {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False, 'value': '1'},
                  {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False, 'value': 'a1217899'},
                  {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.logined', 'path': '/', 'secure': False, 'value': 'true'},
                  {'domain': '.qq.com', 'expiry': 1630283080, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False, 'value': 'GA1.2.1181350627.1630196674'},
                  {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False, 'value': '3691495388147370'},
                  {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.cs_ind', 'path': '/', 'secure': False, 'value': ''},
                  {'domain': '.qq.com', 'expiry': 1630196734, 'httpOnly': False, 'name': '_gat', 'path': '/', 'secure': False, 'value': '1'},
                  {'domain': '.work.weixin.qq.com', 'expiry': 1661732673, 'httpOnly': False, 'name': 'wwrtx.c_gdpr', 'path': '/', 'secure': False, 'value': '0'},
                  {'domain': '.qq.com', 'expiry': 1693268680, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False, 'value': 'GA1.2.168208236.1630196674'},
                  {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False, 'value': 'BHl99IbnFJ1eDhhEYkoOplAA5K37Oe2Qu4TqBREXUkNRmlvbenDw0nzhoeh-f3Qd'},
                  {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False, 'value': 'NciXGt0nPchx_wli-8qsmkgfoumCqL4Z8yZhjn1qjr6bnqjwsQ5MFsifTP_JTY2lT6Q0KzWEm_G-HSXO8fhliHb-PbiBxckZrNw_9TLqP9Ai3gLVGnAAXpTpf9LWvv_3UKTrZZCzv6v9IPr1jHJVauRpl80pHoz6g5rh4TeLVb8f9G5PNTfBABBRpiYaOg1ikvfP-rl29HVyw59TKTzZcedQlKLNiwL2vBJWA5u8mkB9aNczZOhgMO41x7NrACocUMr1mUYU0OZbLaBKLbb05A'},
                  {'domain': '.work.weixin.qq.com', 'expiry': 1632788683, 'httpOnly': False, 'name': 'wwrtx.i18n_lan', 'path': '/', 'secure': False, 'value': 'zh'}]

         #3、植入cookie
        for c in cookie:
             self.driver.add_cookie(c)

         #4、等待3秒,再次登录企业微信界面，发现无需扫码自动登录
        sleep(3)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")

