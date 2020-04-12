import sys
import json

from simple_aws_crawler_framework.crawl import crawl


def scrape(event={}, context={}):
    crawl(**event)
    return 'finished'


if __name__ == "__main__":
    try:
        event = json.loads(sys.argv[1])
    except IndexError:
        event = {}
    scrape(event)