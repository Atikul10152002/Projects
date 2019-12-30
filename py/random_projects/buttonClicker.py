from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())


driver.get("https://b975.com/band-orchestra-choir-competition/")
driver.find_element_by_xpath('//*[@id="PDI_answer48369198"]').click()
driver.find_element_by_xpath('//*[@id="pd-vote-button10471105"]').click()
driver.delete_all_cookies()
driver.refresh()

driver.close()