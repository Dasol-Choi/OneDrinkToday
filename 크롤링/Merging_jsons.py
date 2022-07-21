import json

with open("../DB/cocktail_data_file_page_1.json", encoding="utf-8") as page_1:
    data1 = json.load(page_1)

with open("../DB/page2.json", encoding="utf-8") as page_2:
    data2 = json.load(page_2)

with open("./page_3.json", encoding="utf-8") as page_3:
    data3 = json.load(page_3)

with open("../DB/page_4_new.json", encoding="utf-8") as page_4:
    data4 = json.load(page_4)

with open('../DB/Cocktail_DB.json', 'w', encoding="utf-8") as f:
    json.dump(data1+data2+data3+data4, f, indent="\t", ensure_ascii=False)
