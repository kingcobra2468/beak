#!/usr/bin/env python3

import logging
import sys
import argparse

from beak.beak import Beak

logging.basicConfig(stream=sys.stdout, level=logging.INFO,
                    format='%(asctime)s %(levelname)-8s %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

parser = argparse.ArgumentParser(
    description='Beak, a site resource downloader')

parser.add_argument('--regex', '-r', dest='resource_regex', default='.*',
                    help='Regex expression for specifying resources to download')
parser.add_argument('--url', '-u', dest='url', required=True,
                    help='Site url to extract resources')
parser.add_argument('--output-dir', '-o', dest='output_dir', required=True,
                    help='Output directory to save resources to')
parser.add_argument('--dry-mode', '-d', dest='dry_run', default=False, action='store_true',
                    help='Dry run of beak')

cli_data = parser.parse_args()

beak = Beak(cli_data.url, cli_data.resource_regex, cli_data.output_dir)
beak.download(cli_data.dry_run)
