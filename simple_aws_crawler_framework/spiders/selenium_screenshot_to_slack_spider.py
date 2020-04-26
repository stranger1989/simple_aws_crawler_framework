import os

from scrapy.spiders import CrawlSpider

from selenium import webdriver
import requests


class SeleniumScreenshotToSlackSpider(CrawlSpider):
    name = "selenium_screenshot_to_slack_spider"

    start_urls = [
        "https://www.google.com/"
    ]

    def parse(self, response):
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        options.add_argument("--disable-gpu")
        options.add_argument("--window-size=1280x1696")
        options.add_argument("--disable-application-cache")
        options.add_argument("--disable-infobars")
        options.add_argument("--no-sandbox")
        options.add_argument("--hide-scrollbars")
        options.add_argument("--enable-logging")
        options.add_argument("--log-level=0")
        options.add_argument("--single-process")
        options.add_argument("--homedir=/tmp")
        options.add_argument("--ignore-certificate-errors")
        options.add_argument('--disable-dev-shm-usage')

        driver = webdriver.Chrome(options=options)
        driver.get(url="https://www.google.com/")

        # save screenshot
        screen_shot_path = os.path.dirname(__file__) + '/screenshot/screenshot.png'
        driver.save_screenshot(screen_shot_path)
        driver.quit()

        # send screenshot to slack
        files = {'file': open(os.path.dirname(__file__) + '/screenshot/screenshot.png', 'rb')}
        param = {
            'token': os.environ["SLACK_TOKEN"],
            'channels': os.environ["CHANNELS"]
        }
        res = requests.post(
            "https://slack.com/api/files.upload",
            params=param,
            files=files
        )
        print(res)

