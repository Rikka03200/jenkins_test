# 导包
import time
import config
import tempfile
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


class TestLogin:
    # 类前置处理
    def setup_class(self):
        # 为每个测试创建独立的用户数据目录
        self.temp_dir = tempfile.mkdtemp()
        user_data_dir = os.path.join(self.temp_dir, "user-data")

        # 配置Chrome选项
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")  # 无头模式，适合服务器环境

        # 启动浏览器
        self.driver = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()),
            options=options
        )
        # 窗口最大化
        #self.driver.maximize_window()
        #隐式等待
        self.driver.implicitly_wait(10)

    # 类后置处理
    def teardown_class(self):
        # 确保浏览器关闭
        if hasattr(self, 'driver') and self.driver:
            self.driver.quit()
        # 清理临时目录
        if hasattr(self, 'temp_dir') and os.path.exists(self.temp_dir):
            import shutil
            shutil.rmtree(self.temp_dir)

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
        assert "666" in self.driver.find_element(By.XPATH, '//*[@class="layui-layer layui-layer-dialog  layer-anim"]/div[2]').text