from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

def start_gmeet_recording(meeting_id, meeting_link):
    print(f"start_gmeet_recording called with meeting_id: {meeting_id} and meeting_link: {meeting_link}")
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    chrome_driver_path = '/usr/local/bin/chromedriver'
    service = Service(chrome_driver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)

    driver.get(meeting_link)
    print(f"Starting Google Meet recording for {meeting_id} with link {meeting_link}")
    driver.quit()
