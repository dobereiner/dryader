import pytest
import requests_mock
from dryader.api import get_file_links

@pytest.fixture
def mock_dryad_api():
    with requests_mock.Mocker() as m:
        m.get(
            'https://datadryad.org/api/v2/datasets/doi%3A10.5061%2Fdryad.8pk0p2ns8/versions',
            json={
                "_embedded": {
                    "stash:versions": [
                        {"_links": {"self": {"href": "/api/v2/versions/221917"}}}
                    ]
                }
            }
        )

        m.get(
            'https://datadryad.org/api/v2/versions/221917/files?page=1',
            json={
                "_embedded": {
                    "stash:files": [
                        {
                            "_links": {
                                "stash:download": {"href": "/files/123/download"}
                            },
                            "path": "test_file.txt"
                        }
                    ]
                },
                "_links": {}
            }
        )

        yield m


def test_get_file_links(mock_dryad_api):
    """ Check that get_file_links extracts file links correctly """
    file_links = get_file_links('10.5061/dryad.8pk0p2ns8')

    assert len(file_links) == 1
    assert file_links[0] == ('https://datadryad.org/files/123/download', 'test_file.txt')
