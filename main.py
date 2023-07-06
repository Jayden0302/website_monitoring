import sys
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

def check_website(url, required_contents):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            content = response.text
            for required_content in required_contents:
                if required_content in content:
                    logger.info(f"Response Time: {response.elapsed.total_seconds()}s\t{url} is up and contains the required content '{required_content}'.")
                else:
                    logger.info(f"Response Time: {response.elapsed.total_seconds()}s\t{url} is up but does not contain the required content '{required_content}'.")
        else:
            logger.warning(f"Response Time: {response.elapsed.total_seconds()}s\t{url} is down. Status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        logger.error(f"Error connecting to {url}: {str(e)}")

def monitor_websites(config, interval):
    while True:
        for website in config["websites"]:
            url = website["url"]
            required_contents = website["required_contents"]
            check_website(url, required_contents)
        time.sleep(interval)

if __name__ == "__main__":
    # Load the configuration from JSON file
    with open("config.json") as f:
        config = json.load(f)

    # Check if interval argument is provided
    if len(sys.argv) > 1:
        try:
            interval = int(sys.argv[1])
        except ValueError:
            print("Invalid interval value. Please provide a valid integer value.")
            sys.exit(1)
    else:
        interval = config["default_time_interval"]  # Default interval from config.json

    # Monitor the websites with the specified interval
    monitor_websites(config, interval)