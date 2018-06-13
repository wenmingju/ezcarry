from selenium.webdriver.common.by import By
"""
ezcarry登录页面
"""
login_link = (By.LINK_TEXT, '登录')
username = (By.ID, "UserName")
password = (By.ID, 'PassWord')
login_btn = (By.XPATH, '/html/body/div[2]/div/div/div/form/fieldset/div[3]/div/button')
login_assert = (By.XPATH, '//*[@id="login_end"]/li[2]/a')
