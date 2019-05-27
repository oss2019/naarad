from selenium import webdriver


class Facebook:

    def __init__(self):
        self.link = input('Please provide a group link to enter:')
        self.driver = webdriver.Chrome()

    def open_group(self):
        self.driver.get(self.link)

Facebook().open_group()
