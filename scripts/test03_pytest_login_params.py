"""
技术点： 参数化（数据驱动）
作用：将测试数据和测试脚本分离，后期代码维护焦点放在数据
使用：装饰器@（不改变方法内部的代码逻辑 新增功能）
     @pytest.mark.parametrize==》循环遍历测试数据 调用测试脚本
步骤：
① 准备测试数据，格式：[(),(),()]
② 在被测试方法前面引入装饰器
    @pytest.mark.parametrize("保存数据的变量，注意变量个数=(中数据的个数)", 测试数据)
    def test_login(self, 直接复制装饰器中保存数据的一组变量名即可):
        pass
③ 修改测试方法代码 引用变量中的数据完成测试
"""

# 导包
import time
import config
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


test_data = [
    ("", "123456", "8888"),
    ("13488888888", "", "8888"),
    ("13488887799", "123456", "8888"),
    ("13488888888", "123457", "8888"),
    ("13488888888", "123456", "8888")
]


class TestLogin:
    # 类前置处理
    def setup_class(self):
        # 打开浏览器
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        # driver = webdriver.Chrome()
        # 窗口最大化
        self.driver.maximize_window()

    # 类后置处理
    def teardown_class(self):
        # 退出浏览器
        self.driver.quit()

    # 方法前置处理
    def setup_method(self):
        # 打开页面
        self.driver.get("https://hmshop-test.itheima.net/index.php/Home/user/login.html")

    # 方法后置处理
    def teardown_method(self):
        # 等待3秒
        time.sleep(3)

    @pytest.mark.parametrize("username, password, code", test_data)
    def test_login(self, username, password, code):
        # 页面定位+操作
        self.driver.find_element(By.ID, "username").send_keys(username)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.ID, "verify_code").send_keys(code)
        self.driver.find_element(By.NAME, "sbtbutton").click()

