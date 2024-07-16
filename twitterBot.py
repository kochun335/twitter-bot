import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class InternetSpeedTwitterBot:
    def __init__(self, down, up):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(chrome_options)
        self.up = up
        self.down = down

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        start_btn = self.driver.find_element(By.CLASS_NAME, "start-text")
        start_btn.click()
        time.sleep(60)
        down = self.driver.find_element(By.CLASS_NAME, "download-speed").text
        up = self.driver.find_element(By.CLASS_NAME, "upload-speed").text
        speed = [down, up]
        # self.driver.close()
        return speed

    def tweet_at_provider(self, email, password):
        self.driver.get("https://x.com")
        time.sleep(2)
        self.driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div[2]/main/div/div/div[1]/div[1]/div/div["
                                          "3]/div[3]/a").click()
        time.sleep(2)
        email_input = self.driver.find_element(By.CSS_SELECTOR, "input")
        email_input.send_keys(email + Keys.ENTER)
        time.sleep(2)
        pw_inputs = self.driver.find_elements(By.CSS_SELECTOR, "input")[-1]
        pw_inputs.send_keys(password + Keys.ENTER)
        time.sleep(5)
        tweet_input = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div/div[2]/div/div/div/div/span")
        msg = (f"Hey Internet provider, why is my internet speed {self.down} Mbps for download and {self.up} Mbps for "
               f"upload while I payed for 100 Mbps for download and 30 Mbps for upload")
        tweet_input.send_keys(msg)
        post_btn = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/button/div/span/span")
        post_btn.click()


# bot = InternetSpeedTwitterBot(150, 10)
# bot.tweet_at_provider("dmc.dante.zzzz@gmail.com", "Kochun1!")
