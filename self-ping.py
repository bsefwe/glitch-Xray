#!/usr/bin/env python3
# Script to send GET request to the glitch app URL every 25 minutes to prevent the app from sleeping.
# ARG of self-ping
url = "https://***.glitch.me"
import os
import logging
try:
    import requests
except:
    os.system("pip3 install requests")
    import requests
from time import sleep
if __name__ == "__main__":

    logging.basicConfig(filename="/app/pinging.log", format='%(asctime)s %(message)s', filemode='w')
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)


    while True:
        try:
            logger.info(f"Pinging "+url)
            requests.get(url)
        except:
            logger.warning("Ping failed, retrying...")
            try:
                requests.get(url)
            except:
                logger.error("Cannot ping app, terminating...")
        sleep(4*60)