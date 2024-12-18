import requests
from bs4 import BeautifulSoup


def scrape_google_scholar(url):
    # URL = f'https://scholar.google.com/scholar?q={query}'
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")

    papers = []
    for item in soup.select(".gs_ri"):
        title = item.h3.get_text()
        link = item.a["href"]
        papers.append({"title": title, "link": link})
    return papers


def convert_to_markdown(papers):
    markdown_records = []
    for paper in papers:
        record = f'- [{paper["title"]}]({paper["link"]})'
        markdown_records.append(record)
    return markdown_records
