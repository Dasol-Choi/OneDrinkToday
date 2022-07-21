from flask import Flask, render_template, jsonify, request, redirect, url_for
from pymongo import MongoClient
from api.search import search_name;

app = Flask(__name__)
app.secret_key = 'some_secret'

client = MongoClient('mongodb://ReadOnly_5rink:to5ay5rinks@3.36.229.90', 27017)
db = client.To5ay5rink #DB명: To5ay5rink, 콜렉션명: Cocktails 입니다
# DB 활용 예시코드
# print(db.Cocktails.find_one({"name":"April Fool"}))

@app.route('/')
def home():
   return render_template('main.html')

# 템플릿엔진 사용할 때 쓸 layout 예시입니다
@app.route('/layout_example')
def example():
   return render_template('_layout_example.html',
                            title="레이아웃 예시", # [필수] page title
                            wrapClass="wrap_example") # [선택] 해당 페이지에서 wrap에 클래스 넣을 때

def search_cat():
    Categories = dict(list())
    Categories['bases'] = db.Cocktails.aggregate([{"$group": {"_id": {'base': "$base", 'base_kor': "$base_kor"}}}])
    Categories['abv_lvs'] = db.Cocktails.distinct('abv_lv')
    return Categories

@app.route('/list')
def cocktailList():
    # 카테고리
    categiries =search_cat()
    return render_template('list.html',
                           wrapClass="bg_dark",
                           categories=categiries)

@app.route('/situation')
def cocktailSituation():
    # 상황별 추천
    categiries =search_cat()
    return render_template('situation.html',
                           wrapClass="bg_dark",
                           categories=categiries)


@app.route('/search/<category>/<detail>/<title>')
def search_detail(category, detail, title):
    if(category == 'base'):
        condition = {'base':detail}
    elif(category == 'abv_lv'):
        condition = {'abv_lv': int(detail)}
    elif(category == 'flavor'):
        cat = 'flavor'
        det = int(detail)
        if(det == 4):
            condition = {'$and':[{'flavor': {'$gt': 0}}, {'flavor': {'$lt': 5}}]}
        elif(det == 7):
            condition = {'$and':[{'flavor': {'$gt': 4}}, {'flavor': {'$lt': 7}}]}
        else:
            condition = {'$or': [{'flavor': 7}, {'flavor': 8}, {'flavor':  9}]}
    else:
        if(category == 'default'):
            condition = {}
        else:
            condition = {'tag.'+category:detail}

    if (title != '__default'):
        cocktail_result = list(db.Cocktails.find({'$and': [condition, {'$or': [
                {'name_kor': {'$regex': title}},
                {'name': {'$regex': title, '$options': 'i'}}
            ]}]}, {'_id': False}))
    else: cocktail_result = list(db.Cocktails.find(condition, {'_id': False}))

    return jsonify({'cocktail_result':cocktail_result})

@app.route('/search', methods=['GET'])
def search():
    keyword_receive = request.args.get('keyword')

    # 카테고리
    categiries = search_cat()

    if(keyword_receive is None) :
        keyword_receive = ''

    if (keyword_receive) :
        cocktails = search_name(keyword_receive)
        if (cocktails) :
            return render_template('search.html',
                               cocktailList=cocktails,
                               wrapClass="bg_dark",
                               title=keyword_receive+' | 검색 결과', categories=categiries)

    empty=db.Cocktails.aggregate([{'$sample': {'size': 3}}])
    return render_template('search.html',
                            emptyList=empty,
                            wrapClass="bg_dark",
                            title=keyword_receive+' | 검색 결과', categories=categiries)


@app.route('/api/search', methods=['GET'])
def api_search():
    keyword_receive = request.args.get('keyword')

    if(keyword_receive is None) :
        keyword_receive = ''

    cocktails = search_name(keyword_receive)
    return jsonify({'cocktail_result':cocktails})

@app.route('/<cocktailName>')
def home1(cocktailName):
    cocktail_info = (db.Cocktails.find_one({"name": cocktailName}, {'_id': False}))
    random_info = db.Cocktails.aggregate([{'$sample': {'size': 3}}])
    return render_template('detailPage.html', cocktail_info=cocktail_info,random_info=random_info,wrapClass="bg_dark")

@app.route('/detail', methods=['GET'])
def read_cocktails():
    name_recieve = request.args.get('name_give')
    cocktail_info = (db.Cocktails.find_one({"name": name_recieve}, {'_id': False}))

    return jsonify({'all_details': cocktail_info})

@app.route('/recommend', methods=['GET'])
def recommend_cocktails():
    all_info = list(db.Cocktails.find({}, {'_id': False}))
    return jsonify({'all_details': all_info})

@app.route('/map')
def show_map():
    return render_template('find_map.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=1)
