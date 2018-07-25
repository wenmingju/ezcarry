from Pages import PageLogin
from Basic.Base import Base
class Login(Base):
    def __init__(self, driver):
            Base.__init__(self, driver)

    def login(self, login_username, login_password):
        language = self.find_element(PageLogin.ele_language).text
        if (language == '中文'):
            self.click_element(PageLogin.ele_language)
        self.click_element(PageLogin.login_link)
        self.elment_sendkeys(PageLogin.username, login_username)
        self.elment_sendkeys(PageLogin.password, login_password)
        self.click_element(PageLogin.login_btn)
        login_assert = self.find_element(PageLogin.login_assert).text
        return login_assert

    def exitLogin(self):
        self.goToIndex()
        self.click_element(PageLogin.exit_btn)


