from githubUserInfo import username, password
from selenium.webdriver.common.by import By
from selenium import webdriver
import time


class Github:
    def __init__(self, username, password):
        self.browser = webdriver.Firefox()
        self.username = username
        self.password = password

    def signIn(self):
        self.browser.get("https://github.com/login")
        time.sleep(2)
        self.browser.find_element(
            By.XPATH, "//*[@id='login_field']").send_keys(self.username)
        self.browser.find_element(By.XPATH,
                                  "//*[@id='password']").send_keys(self.password)
        self.browser.find_element(By.XPATH,
                                  "/html/body/div[3]/main/div/div[4]/form/div/input[11]").click()


github = Github(username, password)
github.signIn()
