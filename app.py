from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('mongodb+srv://sparta:test@cluster0.bohxmsb.mongodb.net/?retryWrites=true&w=majority')
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

@app.route("/api/register", methods = ['POST'])
def register_api():
    #회원가입 요청
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
    #희망과목 삭제버튼
    return jsonify({'msg' : '필요한 데이터 담기'})

@app.route("/api/enroll_list", methods=["POST"])
def get_enroll_list_api():
    #신청내역페이지
    # user_id 받아오기
    id_receive = request.form['user_id']
    # user_id로 user_data 받아오기
    user_data = list(db.user_info.find({'user_id':id_receive}))
    print(user_data)
    class_info_list = []
    # 신청내역리스트 추출
    enrollment=user_data[0]['enrollment']
    print(enrollment)
    # 신청내역리스트에서 과목코드 추출
    for e in enrollment:
        # 추출한 과목코드로 강의정보 받아오기
        class_info = db.class_list.find_one({'class_code': e}, {'_id':False})
        print("-----------", class_info)
        # 강의정보리스트에 강의정보 넣기
        class_info_list.append(class_info)
        print("+++++++++++", class_info_list)
    return jsonify({'result' : class_info_list, 'code_list' : enrollment})

@app.route("/api/enroll_delete", methods=["POST"])
def delete_enroll_api():
    #신청내역삭제요청
    user_id = request.form['user_id']
    chklist = request.form['chklist']
    print(user_id)
    print(chklist)

    return jsonify({'msg' : '필요한 데이터 담기'})

# @app.route("/api/add_data", methods=["POST"])
# def add_data_api():
#     id_receive = request.form['user_id']
#     erlist_receive = request.form['erlist']
#     print(id_receive)
#     print("********", erlist_receive)


#     return jsonify({'msg':'POST 연결 완료!'})



if __name__ == '__main__':
   app.run('0.0.0.0', port=5000, debug=True)