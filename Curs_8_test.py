from selenium import webdriver
from selenium.webdriver.common.by import By
import time
# Seteaza driverul
driver = webdriver.Chrome(executable_path="C:\chromedriver_win32\chromedriver.exe")

# Navigam catre un url
driver.get('https://wizzair.com/#/')
# Selector by ID
wp_search = driver.find_element(By.ID, '#search-departure-station').click()
wp_search.send_keys('Romania')
#driver.find_element_by_xpath(""" //button*[@aria-label='Search'] """).click()
#first_name = driver.find_element(By.ID, 'first-name')
#first_name.send_keys('Andy')
#driver.find_element(By.CSS_SELECTOR, 'body > div.wp-site-blocks > header > div > form > div > button').click()



# driver.get('https://www.youtube.com/')
# driver.find_element(By.CSS_SELECTOR, '#content > div.body.style-scope.ytd-consent-bump-v2-lightbox > div.eom-buttons.style-scope.ytd-consent-bump-v2-lightbox > div:nth-child(1) > ytd-button-renderer:nth-child(1) > yt-button-shape > button > yt-touch-feedback-shape > div > div.yt-spec-touch-feedback-shape__fill').click()
# youtube_search = driver.find_element(By.CSS_SELECTOR, '#search')
# youtube_search.send_keys('i feel good')
# driver.find_element(By.CSS_SELECTOR, '#search-icon-legacy > yt-icon').click()
#
# driver.find_element(By.CSS_SELECTOR, '#video-title').click()


#wp-block-search__input-6
#body > div > div > div.is-layout-flow.wp-elements-1f89954b750767c4ade805a0485eda56.wp-block-column.has-text-color.has-background.has-link-color > div > div > a
print("am ajuns la final")
#driver.quit()
