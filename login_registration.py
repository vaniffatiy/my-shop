from selenium import webdriver
driver = webdriver.Chrome()
driver.implicitly_wait(20)
driver.maximize_window()
driver.get("http://practice.automationtesting.in/")
driver.find_element_by_link_text("My Account").click()
driver.find_element_by_id("reg_email").send_keys("svyatoslav@mail.ru")
driver.find_element_by_id("reg_password").send_keys("svyatoslavM73")
driver.find_element_by_css_selector(".woocomerce-FormRow.form-row>input:nth-child(3)").click()
driver.quit()


from selenium import webdriver
driver = webdriver.Chrome()
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver.implicitly_wait(20)
driver.maximize_window()
driver.get("http://practice.automationtesting.in/")
driver.find_element_by_link_text("My Account").click()
driver.find_element_by_id("username").send_keys("svyatoslav@mail.ru")
driver.find_element_by_id("password").send_keys("svyatoslavM73")
driver.find_element_by_css_selector(".form-row>input:nth-child(3)").click()
logout_check = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.LINK_TEXT, "Logout")))
driver.quit()
