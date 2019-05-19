import sys
import logging
import json

# Set log level
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Read API Key & Pass
filename = 'apikey'
with open(filename, 'r') as f:
    data = json.load(f)

    APIKEY = data['apikey']
    APIPASS = data['apipass']




