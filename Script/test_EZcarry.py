import pytest

from Basic.Read_data import read_data
from Basic.init_driver import init_driver
from Options.Page_login import Login


def read_login_data(Role):
    '''
    :param Role: 'supplier_data' / 'buyer_data ' / 'platform_data'
    :return: [（'账户' ,'密码', '预期值'）]
    '''
    data_list = []
    data = read_data("data_login").get('Logindata').get(Role)
    data_list.append((data.get("user"), data.get("passwd"), data.get("expect")))
    return data_list

class Test_EZcarry(object):
        def setup_class(self):
            self.driver = init_driver()
            self.login_obj = Login(self.driver)
            self.driver.maximize_window()
            self.login_obj.goToIndex()

        def teardown_class(self):
            self.driver.quit()
        # 登录测试用例
        @pytest.mark.parametrize("user, passwd, expect", read_login_data('supplier_data'))
        def test_login(self, user, passwd, expect):
            get_assert = self.login_obj.login(user, passwd)
            self.login_obj.exitLogin()
            assert get_assert == expect, '用户名错误'