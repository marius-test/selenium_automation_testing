from selenium import webdriver
from selenium.webdriver.chrome.service import Service


PATH = Service(r"C:\Users\mariu\chromedriver.exe")
driver = webdriver.Chrome(service=PATH)
url = r"https://the-internet.herokuapp.com/"


def main():
    pass


if __name__ == '__main__':
    main()
