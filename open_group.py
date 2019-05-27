# from selenium.webdriver import ChromeOptions, Chrome
import getpass
from selenium import webdriver


print("Please enter your details for facebook login")


class Facebook:

    def __init__(self):
        self.username = input("enter your username: ")
        self.password = getpass.getpass("enter your password: ")
        i = input("To enter a group link press '1':")
        if i is '1':
            self.link = input("enter the link:")
            print("taking you to group page")
        else:
            print("Welcome to FB homepage")
        self.driver = webdriver.Chrome()

    def group_login(self):
        self.driver.get('https://facebook.com')  # To hit the URL
        self.driver.find_element_by_id('email').send_keys(self.username)
        self.driver.find_element_by_id('pass').send_keys(self.password)
        self.driver.find_element_by_id('loginbutton').click()
        self.driver.get(self.link)


Facebook().group_login()

# opts = ChromeOptions()
# opts.add_experimental_option("detach", True)
# driver = Chrome(chrome_options=opts)

