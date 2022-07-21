import json
from bs4 import BeautifulSoup
import requests
from 크롤링_3페이지_상세페이지 import extract_cocktail_collection

page_3 = "https://www.diffordsguide.com/cocktails/search?include%5Bdg%5D=1&limit=20&sort=rating&offset=40"
soup = BeautifulSoup(requests.get(page_3).text, "html.parser")
grid = soup.find("div", {"class": "grid-x grid-margin-x grid-margin-y landing-page-grid"})
anchors = grid.find_all("a")
links = []
cocktail_JSON = []

for anchor in anchors[1:]: #칵테일별 상세페이지로 연결되지 않는 0번째 요소 제거
    hrefs = f"https://www.diffordsguide.com{anchor['href']}"
    links.append(hrefs)

for link in links:
    cocktail_data = extract_cocktail_collection(link)
    cocktail_JSON.append(cocktail_data)
    print(f"...Information of {cocktail_data['name']} was collected")

with open('page_3_new.json', 'w', encoding="utf-8") as f:
    json.dump(cocktail_JSON, f, indent="\t", ensure_ascii=False)




