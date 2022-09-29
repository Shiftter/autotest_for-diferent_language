import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_check_button_add_to_basket(browser):
    try:
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        browser.get(link)
        button = browser.find_element(By.CLASS_NAME,'btn-add-to-basket')
        assert button != None, 'No button add to basket'
    finally:
        print('No button add to basket')