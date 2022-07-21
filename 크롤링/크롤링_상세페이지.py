import json
import re #파이썬 정규표현식 라이브러리
from bs4 import BeautifulSoup
import requests

def extract_cocktail_collection(url):
    page_detail = requests.get(url)
    soup = BeautifulSoup(page_detail.text, "html.parser")

    # 크롤링으로 수집 가능 정보↓
    # <script>태그 안 JSON에 저장된 정보
    cocktail_page = soup.find("script", {"type": "application/ld+json"})
    string_cocktail_page = cocktail_page.text  # HTML 요소 내 JSON으로 작성된 부분 문자열화
    dict_result = json.loads(string_cocktail_page)  # 문자열화한 결과를 다시 JSON으로 변환

    # 칵테일 이름
    Name = dict_result['name']
    # 이미지url
    Img = dict_result['image']
    # 레시피 재료
    Ingredients = dict_result['recipeIngredient']
    # 주재료
    ingredient_base = Ingredients[0].lower()
    ingredients_info = []
    for ingredient in Ingredients:
        ingredient_numbers = re.findall("\d*\.?\d+", ingredient) #정수,소수 모두 포함 실수 추출 정규표현식
        ingredient_amount = ingredient_numbers[0]
        if ingredient.find("ml") != -1:
            ingredient_strings = ingredient.split("ml")
            ingredient_name = ingredient_strings[1]
            ingredient_amount = f"{ingredient_amount} ml"
        else:
            ingredient_name = re.sub(r'[0-9]+', '', ingredient) #문자열에서 숫자 모두 제거
            ingredient_amount = ingredient_amount.rstrip()
        ingredients_info.append(ingredient_amount)
        ingredients_info.append(ingredient_name.lstrip())
    try:
        if ingredient_base.find("whisky") != -1:
            Base = "Whisky"
        elif ingredient_base.find("brandy") != -1:
            Base = "Brandy"
        elif ingredient_base.find("gin") != -1:
            Base = "Gin"
        elif ingredient_base.find("rum") != -1:
            Base = "Rum"
        elif ingredient_base.find("tequila") != -1:
            Base = "Tequila"
        elif ingredient_base.find("vodka") != -1:
            Base = "Vodka"
        elif ingredient_base.find("vermouth") != -1:
            Base = "Vermouth"
        elif ingredient_base.find("sherry") != -1:
            Base = "Sherry"
        else:
            Base = "Etc."
    except Exception as e:
        Base = "Etc."
    # 부재료(=가니쉬)
    cells = soup.find_all("div", {"class": "cell"})
    paragraphs = []
    for cell in cells:
        p = cell.find("p", {"class":""})
        if p is not None:
            paragraphs.append(p)
    Garnish = paragraphs[0].text
    # 맛
    try:
        range_div = soup.findAll("div", {"class": "svg-range"})
        Flavor_div = range_div[1]
        Flavor = int(Flavor_div.find("img")["alt"])
    except:
        Flavor = "Undefined" #flavor 척도 없는 경우의 예외 처리
    # 상세도수
    Alcohol_content = soup.find("ul", {"class": "no-margin-bottom"}).find_all("li")
    AbV = Alcohol_content[1].get_text()
    try:
        Floats_in_AbV = re.findall("\d+.\d+", AbV)  # 정규표현식으로 AbV라는 문자열 안에 있는 숫자 추출
        Alc_by_vol = float(Floats_in_AbV[0])  # 추출한 숫자의 자료형: 문자열>실수 로 변환
    except:
        Floats_in_AbV = re.findall("\d+", AbV)
        Alc_by_vol = float(Floats_in_AbV[0])
    # 도수(범주형)
    AbV_level = "Undefined"
    if Alc_by_vol <= 10:
        AbV_level = 1
    elif Alc_by_vol <= 20:
        AbV_level = 2
    elif Alc_by_vol <= 30:
        AbV_level = 3
    elif Alc_by_vol <= 40:
        AbV_level = 4
    elif Alc_by_vol <= 50:
        AbV_level = 5
    elif Alc_by_vol >= 51:
        AbV_level = 6
    # 레시피
    Recipe = dict_result['recipeInstructions'][0]['text']

    cocktail_data = {
        "name" : Name,
        "name_kor" : "직접 작성 필요",
        "img" : Img,
        "base" : Base,
        "garnish" : Garnish,
        "flavor" : Flavor,
        "abv": Alc_by_vol,
        "abv_lv" : AbV_level,
        "ingredients" : ingredients_info,
        "recipe" : Recipe,
        "tag" : {
            "기분별": ["태그가 아직 입력되지 않았습니다","태그가 아직 입력되지 않았습니다"],
            "인원별": ["태그가 아직 입력되지 않았습니다","태그가 아직 입력되지 않았습니다"],
            "상황별": ["태그가 아직 입력되지 않았습니다","태그가 아직 입력되지 않았습니다"]
        }
    }
    return cocktail_data
