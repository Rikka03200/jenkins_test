class TestLogin:
    # 类前置处理
    def setup_class(self):
        print("我是类前置处理 我只执行1次")

    # 类后置处理
    def teardown_class(self):
        print("我是类后置处理 我只执行1次")

    # 方法前置处理
    def setup_method(self):
        print("我是方法前置处理 每条用例执行之前我都会被执行1次")

    # 方法后置处理
    def teardown_method(self):
        print("我是方法后置处理 每条用例执行之后我都会被执行1次")

    # 用例1：
    def test_login01(self):
        print("case01:登录失败（账号为空）")

    # 用例2：
    def test_login02(self):
        print("case02：登录失败（密码为空）")

    # 用例3：
    def test_login03(self):
        print("case03：登录成功")
