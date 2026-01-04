# Article Scraper

A Python web scraper that extracts titles and links from articles using BeautifulSoup and Requests.

## Features

- Scrapes articles from any URL
- Extracts titles and links
- Saves output to text file
- Command-line interface with argparse
- Comprehensive error handling and logging

## Installation
```bash
# Clone the repository
git clone https://github.com/yourusername/ArticleScraper.git
cd ArticleScraper

# Install dependencies
pip install -r requirements.txt
```

## Usage
```bash
python main.py -a https://example.com/article
```

## Requirements

- Python 3.7+
- requests
- beautifulsoup4

## Project Structure
```
article-scraper/
├── main.py           # Main entry point
├── scraper.py        # Scraping logic
├── requirements.txt  # Dependencies
├── README.md         # Documentation
└── .gitignore       # Git ignore rules
```

## License

MIT License