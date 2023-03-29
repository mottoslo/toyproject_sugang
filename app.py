from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('mongodb+srv://sparta:test@cluster0.q4eauk1.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta

#######################################페이지들###########################

@app.route('/')
def home():
   #로그인 페이지
   return render_template('index.html')

@app.route("/register")
def register_page():
    #회원가입 페이지
    return render_template('registerpage.html')

@app.route("/classes")
def classpage():
    #강의목록 페이지
    return render_template('classlist.html')
3
@app.route("/wishlist")
def wishlist():
    #희망과목페이지
    return render_template('wishlist.html')

@app.route("/myclass")
def myclass():
    #신청내역페이지
    return render_template('myclasspage.html')


############################fetch 요청 경로들##################################
#회원가입
@app.route("/api/registerpage", methods = ['POST'])
def register_api():
     #회원정보 생성
    name_receive = request.form['user_name_give']
    id_receive = request.form['user_id_give']
    pw_receive = request.form['user_pw_give']
    re_pw_receive = request.form['re_pw_give']
        
    doc = {
            'user_name' : name_receive,
            'user_id' : id_receive,
            'user_pw' : pw_receive,
            're_pw' : re_pw_receive
    }
    db.register.insert_one(doc)
    return jsonify({'msg':'입학을 축하합니다.'})

@app.route("/api/login", methods = ['POST']) #POST로 데이터 담거나, GET으로 파라미터 쿼리 날리기
def login_api():
    #로그인 요청
    return jsonify({'msg' : '필요한 데이터 담기'})

@app.route("/api/classlist", methods = ['GET'])
def get_classlist_api():
    # 전체리스트 요청
    all_classList = list(db.class_list.find({},{'_id':False}))
    return jsonify({'result': all_classList})

@app.route("/api/searchlist", methods = ['POST'])
def get_searchlist_api():
    # 검색하여 리스트 요청
    keyword = request.form['keyword']
    searchdb = list(db.class_list.find(
        {'$or':[{'class_name':{'$regex':keyword}},
                {'class_code':{'$regex':keyword}},
                {'instructor':{'$regex':keyword}}]},
                {'_id':False}))
    print(searchdb)
    return jsonify({'keyword': searchdb})

@app.route("/api/wish_button", methods = ['POST'])
def wish_button_api():
    #희망과목 담기 요청
    wish_class = request.form['wishlist']
    # db.user_info.insert_one({'wishlist' : [wish_class]})
    db.user_info.update_one(
        {'user_id':'르탄이'},
        {'$push':{'wishlist': wish_class}}
    )
    return jsonify({'msg' : 'user_id에 class_code 넣었슴다~'})


@app.route("/api/get_wishlist", methods = ['GET'])
def get_wishlist_api():
    #희망과목 불러오기 요청
    return jsonify({'msg' : '필요한 데이터 담기'})


@app.route("/api/enroll_button", methods=["POST"])
def enroll_button_api():
    #수강신청 요청
    return jsonify({'msg' : '필요한 데이터 담기'})

@app.route("/api/wishlist_delete", methods=["POST"])
def wishlist_delete_api():
    #신청내역페이지
    return jsonify({'msg' : '필요한 데이터 담기'})

@app.route("/api/enroll_list", methods=["GET"])
def get_enroll_list_api():
    #신청내역페이지
    return jsonify({'msg' : '필요한 데이터 담기'})

@app.route("/api/enroll_delete", methods=["POST"])
def delete_enroll_api():
    #신청내역페이지
    return jsonify({'msg' : '필요한 데이터 담기'})



if __name__ == '__main__':
   app.run('0.0.0.0', port=5000, debug=True)