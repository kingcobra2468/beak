import urllib.parse
import urllib.request
import re
import os
import logging

from bs4 import BeautifulSoup
import validators
import requests


logger = logging.getLogger(__name__)


class Beak:
    def __init__(self, page_url, resource_regex, output_dir):
        self._page_url = page_url
        self._resource_regex = resource_regex
        self._output_dir = output_dir

    def download(self, dry_run=False):
        for url in self._get_resources_urls():
            logger.info(f'Downloading {url}')
            if dry_run:
                continue

            urllib.request.urlretrieve(url, os.path.basename(url))

    def _get_resources_urls(self):
        resp = requests.get(self._page_url)

        soup = BeautifulSoup(resp.text, features="html.parser")
        urls = []
        for a_tag in soup.find_all('a'):
            url = self._get_absolute_url(a_tag.get('href'))
            if re.match(self._resource_regex, url):
                urls.append(url)

        return urls

    def _get_absolute_url(self, url):
        if validators.url(url):
            return url

        return urllib.parse.urljoin(self._page_url, url)
