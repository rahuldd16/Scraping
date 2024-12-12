import requests
from bs4 import BeautifulSoup
import csv
import re
from serpapi import GoogleSearch

# Constants
SERP_API_KEY = "2bb088365d156a3dd9a09733ac634d2240d925ea3210d312546e06c20f31d311"  # Sign up at https://serpapi.com/ for a free API key
HEADERS = {"User-Agent": "Mozilla/5.0"}


def get_search_results(query, num_results=30):
    """Fetch search results using SERP API."""
    params = {
        "engine": "google",
        "q": query,
        "api_key": SERP_API_KEY,
        "num": num_results,
    }
    search = GoogleSearch(params)
    results = search.get_dict()
    return [result["link"] for result in results.get("organic_results", [])]


def scrape_page(url):
    """Scrape a webpage for company details."""
    try:
        response = requests.get(url, headers=HEADERS, timeout=10)
        soup = BeautifulSoup(response.text, "html.parser")

        # Extract title as company name (simple heuristic)
        title = soup.title.string if soup.title else "Unknown"

        # Extract contact information (emails)
        emails = set(re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", response.text))

        return {"url": url, "title": title, "emails": list(emails)}
    except Exception as e:
        print(f"Error scraping {url}: {e}")
        return {"url": url, "title": "Error", "emails": []}


def main():
    # Input query
    query = input("Enter a search query (e.g., 'ENOVIA PLM support'): ")
    print("Fetching search results...")

    # Fetch search results
    search_results = get_search_results(query)

    print("Scraping pages...")
    scraped_data = [scrape_page(url) for url in search_results]

    # Save results to a CSV file
    output_file = "output.csv"
    with open(output_file, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["url", "title", "emails"])
        writer.writeheader()
        writer.writerows(scraped_data)

    print(f"Scraping complete. Results saved to {output_file}")


if __name__ == "__main__":
    main()
