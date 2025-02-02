import argparse
from dryader.api import get_file_links
from dryader.downloader import download_files_parallel

def main():
    parser = argparse.ArgumentParser(description='Download files from Dryad using a dataset DOI')
    parser.add_argument('doi', help='Dataset DOI (e.g., 10.5061/dryad.8pk0p2ns8)')
    parser.add_argument('-o', '--output', default='data', help='Output directory (default: data)')
    parser.add_argument('-t', '--threads', type=int, default=4, help='Number of download threads (default: 4)')
    
    args = parser.parse_args()

    print(f'Fetching file links for DOI: {args.doi}')
    file_links = get_file_links(args.doi)

    print(f'Found {len(file_links)} files, starting download...')
    download_files_parallel(file_links, output_dir=args.output, max_workers=args.threads)


if __name__ == '__main__':
    main()
