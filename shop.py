# 4 shop
from selenium import webdriver
driver = webdriver.Chrome()
import time
driver.implicitly_wait(20)
driver.maximize_window()
driver.get("http://practice.automationtesting.in/")
driver.find_element_by_link_text("My Account").click()
driver.find_element_by_id("username").send_keys("svyatoslav@mail.ru")
driver.find_element_by_id("password").send_keys("svyatoslavM73")
driver.find_element_by_css_selector(".form-row>input:nth-child(3)").click()
driver.find_element_by_link_text("Shop").click()
driver.execute_script("window.scrollBy(0, 600);")
time.sleep(5)
driver.find_element_by_xpath("//img[@alt='Mastering HTML5 Forms']").click()
html5 = driver.find_element_by_css_selector(".entry-summary>h1")
html5_check = html5.text
time.sleep(5)
assert html5_check == "HTML5 Forms"
driver.quit()

# 5 shop
from selenium import webdriver
driver = webdriver.Chrome()
import time
driver.implicitly_wait(20)
driver.maximize_window()
driver.get("http://practice.automationtesting.in/")
driver.find_element_by_link_text("My Account").click()
driver.find_element_by_id("username").send_keys("svyatoslav@mail.ru")
driver.find_element_by_id("password").send_keys("svyatoslavM73")
driver.find_element_by_css_selector(".form-row>input:nth-child(3)").click()
driver.find_element_by_link_text("Shop").click()
time.sleep(5)
html=driver.find_element_by_css_selector("li:nth-child(2)>span")
html.click()
html_count = html.text
time.sleep(5)
assert html_count == "(3)"
driver.quit()

# 6 shop
from selenium import webdriver
driver = webdriver.Chrome()
import time
driver.implicitly_wait(20)
driver.maximize_window()
driver.get("http://practice.automationtesting.in/")
driver.find_element_by_link_text("My Account").click()
driver.find_element_by_id("username").send_keys("svyatoslav@mail.ru")
driver.find_element_by_id("password").send_keys("svyatoslavM73")
driver.find_element_by_css_selector(".form-row>input:nth-child(3)").click()
driver.find_element_by_link_text("Shop").click()
time.sleep(5)
driver.execute_script("window.scrollBy(0, 100)")
order=driver.find_element_by_css_selector(".orderby>option:nth-child(1)")
order_status=order.get_attribute("selected")
time.sleep(5)
assert order_status is not None
driver.quit()

# 7 shop
from selenium import webdriver
driver = webdriver.Chrome()
import time
driver.implicitly_wait(20)
driver.maximize_window()
driver.get("http://practice.automationtesting.in/")
driver.find_element_by_link_text("My Account").click()
driver.find_element_by_id("username").send_keys("svyatoslav@mail.ru")
driver.find_element_by_id("password").send_keys("svyatoslavM73")
driver.find_element_by_css_selector(".form-row>input:nth-child(3)").click()
driver.find_element_by_link_text("Shop").click()
time.sleep(5)
driver.execute_script("window.scrollBy(0, 600)")
time.sleep(5)
driver.find_element_by_css_selector(".post-169>a:nth-child(2)").click()
del_price=driver.find_element_by_css_selector(".price>del>span")
ins_price=driver.find_element_by_css_selector(".price>ins>span")
time.sleep(5)
assert del_price.text == "₹600.00"
assert ins_price.text == "₹450.00"
driver.quit()

# 8 shop
from selenium import webdriver
driver = webdriver.Chrome()
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
driver.implicitly_wait(20)
driver.maximize_window()
driver.get("http://practice.automationtesting.in/")
driver.find_element_by_link_text("Shop").click()
time.sleep(10)
driver.execute_script("window.scrollBy(0, 1200)")
time.sleep(3)
driver.find_element_by_css_selector(".post-165>a:nth-child(2)").click()
time.sleep(3)
assert driver.find_element_by_css_selector(".wpmenucart-contents>span:nth-child(3)").text == "₹350.00"
cart_items=driver.find_element_by_css_selector(".wpmenucart-contents>span:nth-child(2)")
time.sleep(5)
assert cart_items.text == "1 Item"
driver.find_element_by_css_selector(".wpmenucart-contents").click()
subtotal_check = WebDriverWait(driver, 20).until(
EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".cart-subtotal>td>span"), "₹350.00"))
total_check = WebDriverWait(driver, 20).until(
EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".order-total>td>strong>span"), "₹357.00"))
driver.quit()

# 9 shop
from selenium import webdriver
driver = webdriver.Chrome()
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
driver.implicitly_wait(20)
driver.maximize_window()
driver.get("http://practice.automationtesting.in/")
driver.find_element_by_link_text("Shop").click()
time.sleep(10)
driver.execute_script("window.scrollBy(0, 1200)")
time.sleep(5)
driver.find_element_by_css_selector(".post-165>a:nth-child(2)").click()
time.sleep(3)
driver.find_element_by_css_selector(".wpmenucart-contents").click()
driver.find_element_by_css_selector(".product-remove>.remove").click()
driver.find_element_by_link_text("Undo?").click()
driver.find_element_by_css_selector(".quantity>input").clear()
driver.find_element_by_css_selector(".quantity>input").send_keys("3")
driver.find_element_by_xpath("//input[@value='Update Basket']").click()
assert driver.find_element_by_css_selector(".quantity>input").get_attribute("value") == "3"
time.sleep(5)
driver.find_element_by_css_selector(".coupon>input:nth-child(3)").click()
error_check = WebDriverWait(driver, 20).until(
EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".woocommerce-error>li"), "Please enter a coupon code."))
driver.quit()

# 10 shop
from selenium import webdriver
driver = webdriver.Chrome()
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
driver.implicitly_wait(20)
driver.maximize_window()
driver.get("http://practice.automationtesting.in/")
driver.find_element_by_link_text("Shop").click()
time.sleep(10)
driver.execute_script("window.scrollBy(0, 1200)")
time.sleep(5)
driver.find_element_by_css_selector(".post-165>a:nth-child(2)").click()
time.sleep(5)
driver.find_element_by_css_selector(".wpmenucart-contents").click()
time.sleep(5)
driver.execute_script("window.scrollBy(0, 300)")
time.sleep(5)
proceed_check = WebDriverWait(driver, 20).until(
EC.element_to_be_clickable((By.CSS_SELECTOR, ".wc-proceed-to-checkout>a")))
driver.find_element_by_css_selector(".wc-proceed-to-checkout>a").click()
time.sleep(5)
name_check=WebDriverWait(driver, 20).until(
EC.element_to_be_clickable((
By.ID, "billing_first_name")))
driver.find_element_by_id("billing_first_name").send_keys("NAME")
driver.find_element_by_id("billing_last_name").send_keys("LASTNAME")
driver.find_element_by_id("billing_email").send_keys("mytsykov@mail.ru")
driver.find_element_by_id("billing_phone").send_keys("+79150386589")
time.sleep(5)
driver.execute_script("window.scrollBy(0, 400)")
time.sleep(5)
driver.find_element_by_id("s2id_billing_country").click()
driver.find_element_by_id("s2id_autogen1_search").send_keys("Russia")
driver.find_element_by_id("select2-results-1").click()
driver.find_element_by_id("billing_address_1").send_keys("Lenina, 1")
driver.find_element_by_id("billing_city").send_keys("Moscow")
driver.find_element_by_id("billing_state").send_keys("Moscow")
driver.find_element_by_id("billing_postcode").send_keys("432054")
driver.execute_script("window.scrollBy(0, 900)")
time.sleep(10)
driver.find_element_by_id("payment_method_cheque").click()
driver.find_element_by_id("place_order").click()
WebDriverWait(driver, 20).until(
EC.text_to_be_present_in_element((
By.CSS_SELECTOR, ".woocommerce>p:nth-child(1)"), "Thank you. Your order has been received."))
WebDriverWait(driver, 20).until(
EC.text_to_be_present_in_element((
By.CSS_SELECTOR, ".order_details>tfoot>tr:nth-child(3)>td"), "Check Payments"))
driver.quit()
