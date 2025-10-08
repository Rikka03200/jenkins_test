# 导包
import time
import config
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


class TestLogin:
    # 类前置处理
    def setup_class(self):
        # 打开浏览器
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        # 窗口最大化
        self.driver.maximize_window()
        #隐式等待
        self.driver.implicitly_wait(5)

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
        pass

    def test_login01(self):
        # 页面定位+操作
        self.driver.find_element(By.ID, "username").send_keys("")
        self.driver.find_element(By.ID, "password").send_keys("123456")
        self.driver.find_element(By.ID, "verify_code").send_keys("8888")
        self.driver.find_element(By.NAME, "sbtbutton").click()
        # 断言
        # print(self.driver.find_element(By.CLASS_NAME, "layui-layer-padding").text)
        # assert "用户名不能为空" in self.driver.find_element(By.CLASS_NAME, "layui-layer-padding").text
        # 断言
        # // *[ @ id = "layui-layer2"] / div[2] / text()
        print(self.driver.find_element(By.XPATH, '//*[@class="layui-layer layui-layer-dialog  layer-anim"]/div[2]').text)
        assert "用户名不能为空" in self.driver.find_element(By.XPATH, '//*[@class="layui-layer layui-layer-dialog  layer-anim"]/div[2]').text


    def test_login02(self):
        # 页面定位+操作
        self.driver.find_element(By.ID, "username").send_keys("13488888888")
        self.driver.find_element(By.ID, "password").send_keys("")
        self.driver.find_element(By.ID, "verify_code").send_keys("8888")
        self.driver.find_element(By.NAME, "sbtbutton").click()
        # 断言
        # print(self.driver.find_element(By.CLASS_NAME, "layui-layer-padding").text)
        # assert "密码不能为空" in self.driver.find_element(By.CLASS_NAME, "layui-layer-padding").text

        # 断言
        print(self.driver.find_element(By.XPATH, '//*[@class="layui-layer layui-layer-dialog  layer-anim"]/div[2]').text)
        assert "密码不能为空" in self.driver.find_element(By.XPATH, '//*[@class="layui-layer layui-layer-dialog  layer-anim"]/div[2]').text