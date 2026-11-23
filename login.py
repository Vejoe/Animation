import time
from getpass import getpass

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

URL = (
    "https://tessera.tsec-plg.com/"
    "?clientId=GQAlKv7tn4hr2MhlG8MrF"
    "&env=SBX"
    "&agent%20icCollect=1"
    "&verbose=1"
    "&debug=0"
)

EMAIL = "sam@tessera.test"


def main():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 20)

    try:
        driver.get(URL)
        time.sleep(0.1)

        wait.until(
            EC.element_to_be_clickable((By.ID, "lnk.nav.login"))
        ).click()
        time.sleep(0.1)

        wait.until(
            EC.visibility_of_element_located((By.ID, "inp.login.email"))
        ).send_keys(EMAIL)
        time.sleep(0.1)

        wait.until(
            EC.visibility_of_element_located((By.ID, "inp.login.password"))
        ).send_keys("Password123!")
        time.sleep(0.1)

        wait.until(
            EC.element_to_be_clickable((By.ID, "btn.login.submit"))
        ).click()

        print("Login form submitted.")
        input("按 Enter 关闭浏览器…")
    finally:
        driver.quit()


if __name__ == "__main__":
    main()