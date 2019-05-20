import requests
import logging
import json
import base64


# Set log level
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

xforceURL = "https://api.xforce.ibmcloud.com"

# Read API Key & Pass
filename = 'apikey'
with open(filename, 'r') as f:
    data = json.load(f)

    APIKEY = data['apikey']
    APIPASS = data['apipass']


# Prepare authentication header
    token = base64.b64encode((APIKEY + ":" + APIPASS).encode('UTF-8')).decode('ascii')
    http_headers = {'Authorization': "Basic " + token, 'Accept': 'application/json', 'User-Agent': 'Mozilla 5.0'}


logger.debug("Auth Header: %s\n", http_headers)

def askURL(suspiciousURL):
    try:
        logger.info("Asking URL: %s to IBM X-Force\n", suspiciousURL)
        # Build HTTP request
        requestURL = (xforceURL + "/url/" + suspiciousURL)
        response = requests.get(requestURL, params='', headers=http_headers, timeout=30)
        logger.debug("Request sent to: %s\n", requestURL)
        logger.debug("Response: %s - %s\n", response.text, type(response))

        all_json = response.json()

        json.dumps(all_json, indent=4, sort_keys=True)

    except:
        logger.error("Cannot complete operation for %s\n", suspiciousURL)