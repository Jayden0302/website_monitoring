import requests
import json
import time
import logging

#Configure Logging 
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.FileHandler('output.log'),
        logging.StreamHandler()
    ]
)

logger = logging

def check_website(url, required_content):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            content = response.text
            if required_content in content:
                # pass
                logger.info(f"Response Time: {response.elapsed.total_seconds()}s\t{url} is up and contains the required content.")
            else:
                # pass
                logger.info(f"Response Time: {response.elapsed.total_seconds()}s\t{url} is up but does not contain the required content.")
        else:
                # pass
            logger.warning(f"Response Time: {response.elapsed.total_seconds()}s\t{url} is down. Status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        logger.error(f"Error connecting to {url}: {str(e)}")

def monitor_websites(config, interval):
    while True:
        for website in config["websites"]:
            url = website["url"]
            required_content = website["required_content"]
            check_website(url, required_content)
            print(website)
        time.sleep(interval)

# Load the configuration from JSON file
with open("config.json") as f:
    config = json.load(f)

# Monitor the websites every 5 mins
monitor_websites(config, 300)