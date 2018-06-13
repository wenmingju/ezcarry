import pytest
from Page.Pages import Page
from Basic.init_driver import init_driver
from Basic.Read_data import read_data
def read_login_data():
        data_list = []
        data = read_data("data_login").get("Logindata")
        for i in data.keys():
            data_list.append((data.get(i).get("user"), data.get(i).get("passwd"), data.get(i).get("expect")))
        return data_list

class Test_login(object):
        def setup_class(self):
            self.driver = init_driver()
            self.login_obj = Page(self.driver).page_login()
            self.driver.maximize_window()
            self.driver.get("http://uitest.ezcarry.com")

        def teardown_class(self):
            self.driver.quit()

        @pytest.mark.parametrize("user, passwd, expect", read_login_data())
        def test_login(self, user, passwd, expect):
                self.login_obj.click_login_link()
                self.login_obj.input_username(user)
                self.login_obj.input_password(passwd)
                self.login_obj.click_login_button()
                get_assert = self.login_obj.find_username()
                assert get_assert == expect, '用户名错误'