import requests
from bs4 import BeautifulSoup

def scrape_products(search_query):
    url = f"https://www.amazon.in/s?k={search_query.replace(' ', '+')}"
    headers = {"User-Agent": "Mozilla/5.0"}

    try:
        res = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(res.text, "html.parser")

        products = []
        for item in soup.select(".s-result-item")[:5]:
            title = item.select_one("h2 span")
            if title:
                products.append(title.text.strip())

        return products if products else [search_query]

    except Exception as e:
        print("Scraper error:", e)
        return [search_query]
