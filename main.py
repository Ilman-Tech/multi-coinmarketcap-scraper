import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
print('start app')
options = Options()

options.add_argument("--disable-blink-features=AutomationControlled")
print("disable-blink-features=AutomationControlled")
options.add_argument("--start-maximized")
print("start-maximized")
driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=options
)
print('create browers')
driver.get("https://www.coinmarketcap.com/")

time.sleep(9)

previous_row_count = 0
links = []
print('start while')
while True:
    driver.execute_script("window.scrollBy(0, 800);")
    time.sleep(1.5)
    rows = driver.find_elements(By.XPATH, "//div[@class='sc-4c05d6ef-0 sc-8dd8fbb5-0 dlQYLv urcFe']")
    for row in rows:
        try:
            link = row.find_element(By.XPATH, './/a[contains(@href, "/currencies/")]').get_attribute('href')
            if "coinmarketcap-20-index" in link:
                continue
            print(link)
            links.append(link)
        except Exception:
            continue
    current_row_count = len(rows)
    if current_row_count == previous_row_count:
        print("تمام لینک‌ها بارگذاری شدند.")
        break
    previous_row_count = current_row_count

for link in links:
    print(link)

print(len(links))

driver.quit()
