from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
import certifi

ca = certifi.where()

client = MongoClient('mongodb+srv://sparta:test@cluster0.ofitrvq.mongodb.net/?retryWrites=true&w=majority', tlsCAFile=ca)

db = client.dbsparta
#######################################페이지들###########################

# db.user_list.insert_one({
#     'user_name' : '홍길동',
#     'user_id' : 'gildong',
#     'user_pw' : '1234'
# })

# db.user_list.insert_one({
#     'user_name' : '이윤성',
#     'user_id' : 'lys3367',
#     'user_pw' : '1234'
# })
# db.user_info.insert_one({
#     'user_id' : 'gildong',
#     'wishlist' : ['STAT420', 'COSE241', 'SNOW343'],
#     'enrollment' : ['TEST121', 'KIDS888']
# })
# db.user_info.insert_one({
#     'user_id' : 'abcd',
#     'wishlist' : ['STAT420', 'COSE241', 'SNOW343'],
#     'enrollment' : ['STAT420', 'COSE241', 'SNOW343']
# })
# db.class_list.insert_one({
#     'class_name' : '웹개발종합반',
#     'instructor' : '이범규',
#     'class_time' : {'day':'Mon',
#                     'start_time' : '0900',
#                     'end_time' : '1030'
#                     },
#     'class_code' : 'COSE241',
#     'class_max' : 37,
#     'class_now' : 100
# })
# db.class_list.insert_one({
#     'class_name' : '자바스크립트 문법뽀개기',
#     'instructor' : '김신록',
#     'class_time' : {'day':'Wed',
#                     'start_time' : '1130',
#                     'end_time' : '1300'
#                     },
#     'class_code' : 'STAT420',
#     'class_max' : 37,
#     'class_now' : 100
# })
# db.class_list.insert_one({
#     'class_name' : '웹퍼블리싱 정복반',
#     'instructor' : '임흥선',
#     'class_time' : {'day':'Fri',
#                     'start_time' : '1530',
#                     'end_time' : '1700'
#                     },
#     'class_code' : 'SNOW343',
#     'class_max' : 82,
#     'class_now' : 100
# })
# db.class_list.insert_one({
#     'class_name' : '코딩네컷',
#     'instructor' : '최원장',
#     'class_time' : {'day':'Wed',
#                     'start_time' : '1300',
#                     'end_time' : '1400'
#                     },
#     'class_code' : 'KIDS888',
#     'class_max' : 71,
#     'class_now' : 100
# })
# db.class_list.insert_one({
#     'class_name' : 'Java 문법뽀개기',
#     'instructor' : '이윤성',
#     'class_time' : {'day':'Mon',
#                     'start_time' : '1000',
#                     'end_time' : '1200'
#                     },
#     'class_code' : 'TEST121',
#     'class_max' : 23,
#     'class_now' : 100
# })

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

@app.route("/wishlist")
def wishlist():
    #희망과목페이지
    return render_template('wishlist.html')

@app.route("/myclass")
def myclass():
    #신청내역페이지
    return render_template('myclasspage.html')

############################fetch 요청 경로들##################################

@app.route("/api/registerpage", methods = ['POST'])
def register_api():
    #회원정보 생성
    return jsonify({'msg' : '필요한 데이터 담기'})

@app.route("/api/login", methods = ['GET']) #POST로 데이터 담거나, GET으로 파라미터 쿼리 날리기
def login_api():
    #로그인 요청
    return jsonify({'msg' : '필요한 데이터 담기'})

@app.route("/api/classlist", methods = ['GET'])
def get_classlist_api():
    #강의목록 받아오기 요청
    return jsonify({'msg' : '필요한 데이터 담기'})

@app.route("/api/wish_button", methods = ['POST'])
def wish_button_api():
    #희망과목 담기 요청
    return jsonify({'msg' : '필요한 데이터 담기'})

# //////////
@app.route("/api/post_wishlist", methods = ['POST'])
def post_wishlist_api():
    #희망과목 불러오기 요청
    id_receive = request.form['user_id']

    user_data = list(db.user_info.find({'user_id':id_receive},{'_id':False}))

    class_info_list = []

    wishlist = user_data[0]['wishlist']

    for w in wishlist :
        class_info = db.class_list.find_one({'class_code':w},{'_id':False})
        print("-----------", class_info)
        class_info_list.append(class_info)
        print("+++++++++++", class_info_list)
    return jsonify({'result': class_info_list, 'code_list' : wishlist})

@app.route("/api/enroll_button", methods=["POST"])
def enroll_button_api():
    #수강신청 요청
    class_code_receive = request.form['class_code_give']
    class_name_receive = request.form['class_name_give']
    instructor_receive = request.form['instructor_give']
    class_day_receive = request.form['class_day_give']
    class_time_receive = request.form['class_time_give']
    
    doc = {
        'class_code' : class_code_receive,
        'class_name' : class_name_receive,
        'instructor' : instructor_receive,
        'class_day' : class_day_receive,
        'class_time' : class_time_receive
    }

    db.enrolllist.insert_one(doc)

    # if doc == doc :
    #     return jsonify({'msg': '중복입니다.'})
    # else :
    return jsonify({'msg': '신청되었습니다.'})

@app.route("/api/wishlist_delete", methods=["POST"])
def wishlist_delete_api():
    # 희망과목 삭제버튼
    user_id_receive = request.form['user_id_give']
    class_code_receive = request.form['code_give']
   
    db.wishlist.delete_one({'user_id' : user_id_receive , 'code' : class_code_receive})

    return jsonify({'msg' : '삭제되었습니다.'})

# ////////////

@app.route("/api/enroll_list", methods=["POST"])
def get_enroll_list_api():
    #신청내역페이지
    return jsonify({'msg' : '필요한 데이터 담기'})

@app.route("/api/enroll_delete", methods=["POST"])
def delete_enroll_api():
    #신청내역삭제요청
    return jsonify({'msg' : '필요한 데이터 담기'})

if __name__ == '__main__':
   app.run('0.0.0.0', port=5001, debug=True)