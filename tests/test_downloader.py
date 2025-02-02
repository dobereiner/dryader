import pytest
import requests_mock
import os
from dryader.downloader import download_files_parallel

@pytest.fixture
def mock_file_download():
    """ Mock file download """
    with requests_mock.Mocker() as m:
        m.get('https://datadryad.org/files/123/download', text='fake content')
        yield m


def test_download_files_parallel(mock_file_download, tmp_path):
    """ Test file download """
    output_dir = tmp_path / "downloads"
    output_dir.mkdir()

    file_links = [('https://datadryad.org/files/123/download', str(output_dir / "test_file.txt"))]

    download_files_parallel(file_links, max_workers=1)

    downloaded_file = output_dir / "test_file.txt"
    assert downloaded_file.exists()
    assert downloaded_file.read_text() == 'fake content'
