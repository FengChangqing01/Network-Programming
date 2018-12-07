from selenium import webdriver

def start_chorme():
    driver = webdriver.Chrome(executable_path="spider\chromedriver.exe")
    driver.start_client()
    return driver


start_chorme()