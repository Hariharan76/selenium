import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
# options.add_argument('--headless')
# # options.add_argument('--no-sandbox')
# options.add_argument('--disable-dev-shm-usage')

# driver1 = webdriver.Chrome()
# driver2=
a="hariharan"
for i in range(10):
    driver = webdriver.Firefox()
    c=a+str(i)
    driver.get('https://stagemeet.worktual.co.uk/YWQ-Pf-yxL-C1')
    g = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div/button[1]/span")
    g.click()
    gg = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div[2]/div/input")
    gg.send_keys(c)
    ggg = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div[2]/button").click()

# driver.findElement(By.CssSelector("a.item")).Click();(By.CSS_SELECTOR, 'h1>span')
# print(a)
# search = driver.find_element_by_class("rightcontainer_cusLabel__1SHPk")
# search.send_keys("hari")
# driver.find_element("join").click()
# search.send_keys(Keys.RETURN)

time.sleep(600)
