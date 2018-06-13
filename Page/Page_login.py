import Page
from Basic.Base import Base
class Login(Base):
    def __init__(self, driver):
            Base.__init__(self, driver)

    def click_login_link(self):
        self.click_element(Page.login_link)

    def input_username(self, login_username):
        self.elment_sendkeys(Page.username, login_username)

    def input_password(self, login_password):
        self.elment_sendkeys(Page.password, login_password)

    def click_login_button(self):
        self.click_element(Page.login_btn)

    def find_username(self):
        login_assert = self.find_element(Page.login_assert).text
        return login_assert
