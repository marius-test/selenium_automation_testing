from selenium import webdriver
from selenium.webdriver.chrome.service import Service


PATH = Service("C:\\Users\\mariu\\chromedriver.exe")
driver = webdriver.Chrome(service=PATH)


def main():
    pass


if __name__ == '__main__':
    main()
