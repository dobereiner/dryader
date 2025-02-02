import requests

DRYAD_API_BASE = 'https://datadryad.org/api/v2'


def get_file_links(dataset_doi):
    '''
    Fetches a list of file download links for a given dataset DOI.
    :param dataset_doi: DOI of the dataset (e.g., '10.5061/dryad.8pk0p2ns8').
    :return: List of tuples (download_url, filename).
    '''
    dataset_doi_encoded = dataset_doi.replace(':', '%3A').replace('/', '%2F')
    url = f'{DRYAD_API_BASE}/datasets/doi%3A{dataset_doi_encoded}/versions'
    
    response = requests.get(url, headers={'Accept': 'application/json'})
    response.raise_for_status()
    data = response.json()

    if '_embedded' not in data or 'stash:versions' not in data['_embedded']:
        raise ValueError(f'⚠ No versions found for DOI {dataset_doi}')
    
    versions = data['_embedded']['stash:versions']
    
    latest_version = versions[-1]
    latest_version_id = latest_version.get('id')
    
    if not latest_version_id:
        raise ValueError(f'⚠ Could not determine latest version ID for DOI {dataset_doi}')
    
    print(f'Using dataset version ID: {latest_version_id}')

    file_links = []
    page = 1
    while True:
        files_url = f'{DRYAD_API_BASE}/versions/{latest_version_id}/files?page={page}'
        response = requests.get(files_url, headers={'Accept': 'application/json'})
        response.raise_for_status()
        data = response.json()
        
        if '_embedded' not in data or 'stash:files' not in data['_embedded']:
            break
        
        for file in data['_embedded']['stash:files']:
            download_url = 'https://datadryad.org' + file['_links']['stash:download']['href']
            filename = file['path']
            file_links.append((download_url, filename))
        
        if 'next' not in data['_links']:  # Stop if there are no more pages
            break
        page += 1

    return file_links
