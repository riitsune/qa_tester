from selenium import webdriver

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://www.google.com")
driver.implicitly_wait(10)
driver.find_element(By.NAME, "q").send_keys("yes!!!")
driver.find_element(By.NAME, "btnK").click()
driver.quit()

driver = webdriver.Chrome()
driver.get("http://testerlaru.temp.swtest.ru/index.php?route=account/login")
driver.implicitly_wait(10)
driver.find_element(By.NAME, "email").send_keys("test11@test.ru")
driver.find_element(By.NAME, "password").send_keys("QA_12345678")
driver.find_element(By.XPATH,"/html/body/div[2]/div[2]/div/div/div[2]/div/form/input").click()
driver.quit()