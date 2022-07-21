import json
from 크롤링_상세페이지 import extract_cocktail_collection

links = [
    "https://www.diffordsguide.com/cocktails/recipe/4226/caribbean-colada",
    "https://www.diffordsguide.com/cocktails/recipe/1737/san-francisco",
    "https://www.diffordsguide.com/cocktails/recipe/270/blue-riband",
    "https://www.diffordsguide.com/cocktails/recipe/7952/pink-spritz",
    "https://www.diffordsguide.com/cocktails/recipe/5409/pacific-breeze",
    "https://www.diffordsguide.com/cocktails/recipe/10508/belafonte",
    "https://www.diffordsguide.com/cocktails/recipe/4812/morado",
    "https://www.diffordsguide.com/cocktails/recipe/1062/jelly-belly-beany",
    "https://www.diffordsguide.com/cocktails/recipe/4847/blanco-43",
    "https://www.diffordsguide.com/cocktails/recipe/4636/doctor-pepper",
    "https://www.diffordsguide.com/cocktails/recipe/5931/coffee-and-tonic",
    "https://www.diffordsguide.com/cocktails/recipe/3972/optimist",
    "https://www.diffordsguide.com/cocktails/recipe/4395/white-americano",
    "https://www.diffordsguide.com/cocktails/recipe/1549/pink-lemonade-alcohol-free",
    "https://www.diffordsguide.com/cocktails/recipe/2309/blue-hawaii",
    "https://www.diffordsguide.com/cocktails/recipe/3963/prohibition-daisy-alcohol-free",
    "https://www.diffordsguide.com/cocktails/recipe/5461/palo-negro",
    "https://www.diffordsguide.com/cocktails/recipe/10731/christmas-negroni",
    "https://www.diffordsguide.com/cocktails/recipe/4780/virgin-passion-alcohol-free",
    "https://www.diffordsguide.com/cocktails/recipe/1523/pimms-cup-or-classic-pimms",
    "https://www.diffordsguide.com/cocktails/recipe/1690/rosarita-margarita",
    "https://www.diffordsguide.com/cocktails/recipe/263/blue-lady",
    "https://www.diffordsguide.com/cocktails/recipe/4594/egg-sour",
    "https://www.diffordsguide.com/cocktails/recipe/4999/sweet-libertys-sherry-cobbler",
    "https://www.diffordsguide.com/cocktails/recipe/222/black-and-tan",
    "https://www.diffordsguide.com/cocktails/recipe/825/garibaldi",
    "https://www.diffordsguide.com/cocktails/recipe/3944/when-the-smoke-cleared",
    "https://www.diffordsguide.com/cocktails/recipe/4718/journey-of-brothers",
    "https://www.diffordsguide.com/cocktails/recipe/835/gin-and-tonic",
    "https://www.diffordsguide.com/cocktails/recipe/11088/garibaldino",
    "https://www.diffordsguide.com/cocktails/recipe/10509/porto-tonico-white-port-and-tonic",
    "https://www.diffordsguide.com/cocktails/recipe/4338/sbagliato-with-tonic"
]
cocktail_JSON = []

for link in links:
    cocktail_data = extract_cocktail_collection(link)
    cocktail_JSON.append(cocktail_data)
    print(f"...Information of {cocktail_data['name']} was collected")

with open('../DB/added_cocktails.json', 'w', encoding="utf-8") as f:
    json.dump(cocktail_JSON, f, indent="\t", ensure_ascii=False)




