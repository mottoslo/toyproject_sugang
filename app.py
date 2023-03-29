from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('mongodb+srv://sparta:test@cluster0.nxpuz9m.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta


from func import *
import random

col_list = ['#ff6347', '#006CB7', '#009900', '#660099', '#f29886', '#ffd400', '#964b00', '#ffc0cb', '#555555']

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
    return jsonify({'msg' : '필요한 데이터 담기'})

@app.route("/api/enroll_delete", methods=["POST"])
def delete_enroll_api():
    #신청내역삭제요청
    return jsonify({'msg' : '필요한 데이터 담기'})

@app.route("/api/get_table_position", methods=["POST"])
def get_table_position():
    code_list_len = int(request.form['code_list_len'])
    code_list = [request.form[f'code_list{i}'] for i in range(code_list_len)]
    draw_info = []
    for code in code_list:
        thisclass = db.class_list.find_one({'class_code' : code},{'_id' : False})
        dic = {'class_name' : thisclass['class_name'],
               'class_pos' : position_finder_list(thisclass['class_time']),
               'class_color' : random.choice(col_list)
        }
        draw_info.append(dic)
    
    # print(draw_info)
    return jsonify({'result' : draw_info})



if __name__ == '__main__':
   app.run('0.0.0.0', port=5000, debug=True)