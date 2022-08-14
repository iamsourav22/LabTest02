import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains


class LabTest02():
    def purchase(self):
        print("Running")
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get('http://automationpractice.com/index.php')
        driver.maximize_window()

# Account create
        signinBtn = driver.find_element(By.CSS_SELECTOR, '#header > div.nav > div > div > nav > div.header_user_info > a')
        signinBtn.click()
        time.sleep(2)

        cemail = driver.find_element(By.ID, 'email_create')
        cemail.send_keys("sourav.chak0@gmail.com")

        createaccountBtn = driver.find_element(By.CSS_SELECTOR, '#SubmitCreate > span')
        createaccountBtn.click()
        time.sleep(5)

        title = driver.find_element(By.CSS_SELECTOR, '#id_gender1')
        title.click()

        fname = driver.find_element(By.ID, 'customer_firstname')
        fname.send_keys("Sourav")
        time.sleep(2)

        lname = driver.find_element(By.ID, 'customer_lastname')
        lname.send_keys("Chak")
        time.sleep(2)

        apassword = driver.find_element(By.ID, 'passwd')
        apassword.send_keys("123454321")
        time.sleep(2)

        address = driver.find_element(By.ID, 'address1')
        address.send_keys("Mirpur, Dhaka, 1216.")
        time.sleep(2)

        city = driver.find_element(By.ID, 'city')
        city.send_keys("Dhaka")
        time.sleep(2)

        State = driver.find_element(By.ID, "id_state")
        all_State = Select(State)
        all_State.select_by_index(1)

        zip = driver.find_element(By.ID, 'postcode')
        zip.send_keys("12161")
        time.sleep(2)

        phone = driver.find_element(By.ID, 'phone_mobile')
        phone.send_keys("00000000000")
        time.sleep(2)

        register = driver.find_element(By.CSS_SELECTOR, '#submitAccount > span')
        register.click()
        print(driver.title)

        signout = driver.find_element(By.CSS_SELECTOR, '#header > div.nav > div > div > nav > div:nth-child(2) > a')
        signout.click()
        time.sleep(2)

# Sign in to the Website

        email = driver.find_element(By.NAME, 'email')
        email.send_keys("sourav.chak0@gmail.com")
        password = driver.find_element(By.NAME, 'passwd')
        password.send_keys("123454321")

        html = driver.find_element(By.XPATH, '/html')
        html.click()

        signinBtn = driver.find_element(By.CSS_SELECTOR, '#SubmitLogin > span')
        signinBtn.click()
        time.sleep(4)

# Tshirt
        tshirt = driver.find_element(By.CSS_SELECTOR, '#block_top_menu > ul > li:nth-child(3) > a')
        tshirt.click()
        time.sleep(2)

        blue = driver.find_element(By.CSS_SELECTOR, '#layered_id_attribute_group_14')
        blue.click()
        print(driver.title)
        time.sleep(2)

        actions = ActionChains(driver)

        addtocarthover = driver.find_element(By.XPATH, '//*[@id="center_column"]/ul/li/div/div[2]/span/span')
        actions.move_to_element(addtocarthover).perform()


        addtocart = driver.find_element(By.XPATH, '//*[@id="center_column"]/ul/li/div/div[2]/div[2]/a[1]/span')
        addtocart.click()
        time.sleep(10)
        print(driver.title)

        checkout = driver.find_element(By.CSS_SELECTOR, '#layer_cart > div.clearfix > div.layer_cart_cart.col-xs-12.col-md-6 > div.button-container > a > span')
        checkout.click()

        pcheckout = driver.find_element(By.CSS_SELECTOR, '#center_column > p.cart_navigation.clearfix > a.button.btn.btn-default.standard-checkout.button-medium > span')
        pcheckout.click()

        apcheckout = driver.find_element(By.CSS_SELECTOR, '#center_column > form > p > button > span')
        apcheckout.click()
        time.sleep(2)

        checkbox = driver.find_element(By.CSS_SELECTOR, '#cgv')
        checkbox.click()
        time.sleep(2)

        html = driver.find_element(By.XPATH, '/html')
        html.click()

        aapcheckout = driver.find_element(By.CSS_SELECTOR, '#form > p > button > span')
        aapcheckout.click()
        time.sleep(10)

        html = driver.find_element(By.XPATH, '/html')
        html.click()

        signout = driver.find_element(By.CSS_SELECTOR, '#header > div.nav > div > div > nav > div:nth-child(2) > a')
        signout.click()
        time.sleep(5)

        driver.close()


obj = LabTest02()
obj.purchase()