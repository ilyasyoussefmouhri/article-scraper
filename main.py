import logging
from scraper import parse
import argparse


def main():
    # Configure logging
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    # Getting the URL through the CLI
    parser = argparse.ArgumentParser(description="Scrape articles from a URL")
    parser.add_argument("-a", "--article", help="Article URL to scrape", required=True)
    args = parser.parse_args()

    url = args.article

    if not url.startswith("http://", "https://"):
        logging.error("Invalid URL")
        exit(1)

    # Parsing and writing data to output.txt
    try:
        logging.info(f"Scraping URL: {url}")

        data = parse(url)

        # Check if parsing was successful
        if data is None:
            logging.error("Failed to parse article")
            exit(1)

        # Write to file
        with open('output.txt', 'w') as f:
            f.write('Titles and Links:\n')
            f.write('=' * 50 + '\n\n')

            for title, link in data:
                f.write(f'Title: {title}\n')
                f.write(f'Link: {link}\n')
                f.write('-' * 50 + '\n')

        logging.info(f'Successfully wrote {len(data)} items to output.txt')

    except Exception as e:
        logging.error(f"Error: {e}")
        exit(1)


if __name__ == "__main__":
    main()