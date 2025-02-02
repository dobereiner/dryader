import argparse
from dryader.api import get_file_links
from dryader.downloader import download_files_parallel


def main():
    parser = argparse.ArgumentParser(description='Dryader - Download Dryad datasets')
    parser.add_argument('doi', help='DOI of the dataset (e.g., 10.5061/dryad.8pk0p2ns8)')
    parser.add_argument('-o', '--output', default='downloads', help='Output directory')
    parser.add_argument('-t', '--threads', type=int, default=4, help='Number of threads')
    args = parser.parse_args()

    print(f'Fetching file links for DOI: {args.doi}')
    file_links = get_file_links(args.doi)

    print(f'Downloading {len(file_links)} files to {args.output} using {args.threads} threads')
    download_files_parallel(file_links, output_dir=args.output, max_workers=args.threads)


if __name__ == '__main__':
    main()
