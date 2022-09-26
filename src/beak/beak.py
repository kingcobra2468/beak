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
    """Beak retrieves resources from a given website based
    on a resource regex expression.
    """

    def __init__(self, page_url, resource_regex, output_dir):
        """Constructor.

        Args:
            page_url (str): The website to extract resources from.
            resource_regex (str): A regex expression to determine if a given
            resource needs to be downlaoded.
            output_dir (str): The output directory to store the downloaded
            resources.
        """
        self._page_url = page_url
        self._resource_regex = resource_regex
        self._output_dir = output_dir

    def download(self, dry_run=False):
        """Downloads all resources from the given page that match
        the resource regex expression.

        Args:
            dry_run (bool, optional): Whether to perform a dry run of
            the download operations. Defaults to False.
        """
        for url in self._get_resources_urls():
            logger.info(f'Downloading {url}')
            if dry_run:
                continue

            urllib.request.urlretrieve(url, os.path.join(
                self._output_dir, os.path.basename(url)))

    def _get_resources_urls(self):
        """Retrieves the urls of all the resources that match
        the resource regex expression.

        Returns:
            List(str): A list of urls to the resources. 
        """
        resp = requests.get(self._page_url)

        soup = BeautifulSoup(resp.text, features="html.parser")
        urls = []
        for a_tag in soup.find_all('a'):
            # get the actual url if the href attribute only stores
            # a partial route
            url = self._get_absolute_url(a_tag.get('href'))
            if re.match(self._resource_regex, url):
                urls.append(url)

        return urls

    def _get_absolute_url(self, url):
        """Gets the absolute url path to the resource.

        Args:
            url (str): The href url of a resource.

        Returns:
            str: A valid url to the resource. 
        """
        if validators.url(url):
            return url

        return urllib.parse.urljoin(self._page_url, url)
