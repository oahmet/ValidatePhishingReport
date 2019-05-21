import sys
import logging
import xforce
from html.parser import HTMLParser
import urllib3

# Set log level
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


urls = []
# Extract URLs from HTML e-mail

# FIXME - Python HTMLParser requires to define ou own class.
class URLHTMLParser(HTMLParser):

    url_list = []
    def handle_starttag(self, tag, attrs):
        if tag != 'a':
            return

        for attr in attrs:
            if 'href' in attr[0]:
                self.url_list.append(attr[1])
                break

def extractURL(content):
    parser = URLHTMLParser()
    parser.feed(content)
    return parser.url_list


# FIXME - Wrok with following test data until completing fetchmail

urls = extractURL('<html><head><title>Test</title></head>'
        '<body><h1>sdgsdg</h1><a href="https://panel.vargakragard.se">aa</a> sdgsdgsg <a href="http://example.com">dg</a>"</body></html>')


# Ask URL to X-force

for url in urls:
    xforce.askURL(url)