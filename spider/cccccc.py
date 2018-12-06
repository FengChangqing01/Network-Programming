# -*- coding:utf-8 -*-
from selenium import webdriver
import time


url = "https://pan.baidu.com/s/1k8sf9eB-N6xAzbppKHmmWA#list/path=%2F111111%E6%BC%AB%E7%94%BB%E5%A4%A7%E5%85%A8%2F%E7%83%AD%E9%97%A8%E8%BF%9E%E8%BD%BD%E6%BC%AB%E7%94%BB%2F06%E3%80%81%E5%81%B7%E4%BA%8F%EF%BC%88%E4%BA%8F%E8%A7%86%E8%80%85%EF%BC%89%EF%BC%8C%E7%AC%AC%E4%BA%8C%E5%AD%A3%E6%9B%B4%E6%96%B0%E4%B8%AD%2F%E5%81%B7%E7%AA%A5%E7%AC%AC%E4%BA%8C%E5%AD%A3&parentPath=%2F111111%E6%BC%AB%E7%94%BB%E5%A4%A7%E5%85%A8%2F%E7%83%AD%E9%97%A8%E8%BF%9E%E8%BD%BD%E6%BC%AB%E7%94%BB"

def start_chrome():
    driver = webdriver.Chrome(executable_path="spider\chromedriver.exe")
    driver.start_client()
    return driver

def get_date():
    sel = "div > dd"
    datas = driver.find_elements_by_css_selector(sel)
    return [data.find_element_by_css_selector('div.ctime').text for data in datas]

while True:
    driver = start_chrome()
    driver.get(url)
    time.sleep(10)
    dates = get_date()
    driver.close()


print(dates)

