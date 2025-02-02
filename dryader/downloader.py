import os
import requests
from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor

CHUNK_SIZE = 1024 * 1024  # 1MB


def download_file(url, filename, output_dir='data'):
    '''
    Downloads a file from a given URL and saves it to the specified directory.
    :param url: File download link.
    :param filename: Original filename.
    :param output_dir: Directory to save the file.
    '''
    os.makedirs(output_dir, exist_ok=True)
    file_path = os.path.join(output_dir, filename)

    # Skip download if file already exists
    if os.path.exists(file_path):
        print(f'[✔] {filename} already downloaded, skipping...')
        return

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
        'Referer': 'https://datadryad.org/'
    }

    response = requests.get(url, headers=headers, stream=True)
    response.raise_for_status()
    
    total_size = int(response.headers.get('content-length', 0))
    progress_bar = tqdm(total=total_size, unit='B', unit_scale=True, desc=filename)

    with open(file_path, 'wb') as file:
        for chunk in response.iter_content(CHUNK_SIZE):
            file.write(chunk)
            progress_bar.update(len(chunk))

    progress_bar.close()
    print(f'[✔] {filename} downloaded to {output_dir}')


def download_files_parallel(file_links, output_dir='data', max_workers=4):
    '''
    Downloads multiple files in parallel.
    :param file_links: List of (URL, filename) tuples.
    :param output_dir: Directory to save the files.
    :param max_workers: Number of threads for parallel downloads.
    '''
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = [executor.submit(download_file, url, filename, output_dir) for url, filename in file_links]
        for future in futures:
            future.result()
