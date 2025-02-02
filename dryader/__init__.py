"""
dryader: A Python library for downloading datasets from DRYAD
"""
__version__ = '0.1.0'

from .api import get_file_links
from .downloader import download_files_parallel
