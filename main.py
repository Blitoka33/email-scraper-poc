######### USE IT ON YOUR OWN RESPONSIBILITY #########
######### I AM NOT RESPONSIBLE FOR ANY DAMAGE #########
import os
import requests
from bs4 import BeautifulSoup

emails = []

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
}

query = input("Enter a keyword you want me to scrape: ")

url = f"https://www.google.com/search?q={query}"

if not os.path.exists("emails.txt"):
    with open("emails.txt", "w") as f:
        f.write("")

r = requests.get(url, headers=headers)
html = r.text
soup = BeautifulSoup(html, "html.parser")
results = soup.find_all("div", class_="g")

links = []
for result in results:
    try:
        link = result.find("a")["href"]
        if "google" not in link:
            links.append(link)
    except:
        pass

backlinks = []

for link in links:
    try:    
        r = requests.get(link, headers=headers, timeout=10)
        print("Scraping SERP: " + link)
        html = r.text
        soup = BeautifulSoup(html, "html.parser")
        email_potential = soup.find_all("a", href=True)
        for email in email_potential:
            if "mailto:" in email["href"]:
                print("Found email: " + email["href"].replace("mailto:", ""))
                with open("emails.txt", "a") as f:
                    f.write("\n" + email["href"].replace("mailto:", ""))
            else:
                if "http" in email["href"] and "shopify" not in email["href"] and "amazon" not in email["href"] and "google" not in email["href"]:
                    backlinks.append(email["href"])
    except:
        pass

def scrapebacklinks(bvar):
    backlinks2 = []
    for link in bvar:
        try:
            r = requests.get(link, headers=headers, timeout=10)
            print("Scraping backlink: " + link)
            html = r.text
            soup = BeautifulSoup(html, "html.parser")
            email_potential = soup.find_all("a", href=True)
            for email in email_potential:
                if "mailto:" in email["href"]:
                    print("Found email: " + email["href"].replace("mailto:", ""))
                    with open("emails.txt", "a") as f:
                        f.write("\n" + email["href"].replace("mailto:", ""))
                else:
                    if "http" in email["href"] and "shopify" not in email["href"] and "amazon" not in email["href"] and "google" not in email["href"]:
                        backlinks2.append(email["href"])
        except:
            pass
    scrapebacklinks(backlinks2)

scrapebacklinks(backlinks)    