import requests
from bs4 import BeautifulSoup
import logging

# Configure logging
logging.basicConfig(
        level=logging.INFO,
        filename='app.log',
        format="%(asctime)s >>>> %(filename)s:%(lineno)s | %(levelname)s | %(message)s",
        datefmt="%Y-%m-%d : %H:%M:%S",
)
logger = logging.getLogger()





def parse(url):
    # scraping the article with requests

    try:

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        response = requests.get(url, headers=headers,
                                    timeout=10, allow_redirects=False)

        if response.status_code != 200:
            logger.error("Request failed with status code: " + str(response.status_code))
            return None

        article = response.text
        logger.info('Article scraped successfully')

    except requests.exceptions.Timeout:
        logger.error("Timeout")
        return None # Exit function immediately

    except requests.exceptions.InvalidURL:
        logger.error("InvalidURL")
        return None # Exit function immediately

    except Exception as e:
        logger.error(e)
        return None # Exit function immediately



#fetching and parsing titles and links

    try:
        soup = BeautifulSoup(article, 'html.parser')
        data = []
        for a in soup.find_all('a'):
            title = a.get_text(strip=True)
            link = a.get('href')

            if title and link:
                data.append((title,link))

        logger.info('Article parsed successfully')
        return data
    except Exception as e:
        logger.error('Parsing error: ' + str(e))
