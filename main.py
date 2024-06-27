import json
import time

from box import Box
from utils.constants import config
from spiders.spider import Spider


def main():
    while True:
        with open("news_sites.json", "r") as file:
            sites = Box(json.load(file))

        for site in sites.rss_feeds:
            Spider(site.url, site.local_db_key, site.name)

        time.sleep(config.spider_sleep_time * 3600)


if __name__ == "__main__":
    main()
