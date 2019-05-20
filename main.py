import sys
import logging
import json
import base64
import xforce
import requests

# Set log level
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Ask URL to X-force
url = "panel.vargakragard.se"
xforce.askURL(url)