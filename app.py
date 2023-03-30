from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient

import certifi

ca = certifi.where()

client = MongoClient('mongodb+srv://sparta:test@cluster0.nxpuz9m.mongodb.net/?retryWrites=true&w=majority', tlsCAFile=ca)
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
    #강의목록 페이지/
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
    name_receive = request.form['user_name_give']
    id_receive = request.form['user_id_give']
    pw_receive = request.form['user_pw_give']
    re_pw_receive = request.form['re_pw_give']


    doc = {
        'user_name' : name_receive,
        'user_id' : id_receive,
        'user_pw' : pw_receive,        
    }
    db.user_list.insert_one(doc)
    # print(doc)
    return jsonify({'msg':'가입이 완료되었습니다.'})



@app.route("/api/login", methods = ['POST']) #POST로 데이터 담거나, GET으로 파라미터 쿼리 날리기
def login_api():
    id_receive = request.form['user_id_give']
    pw_receive = request.form['user_pw_give']

    user = db.user_list.find_one({'user_id':id_receive},{'_id':False})
    # print(user)
    # print('====')

    # print(f'입력한 pw 타입 : {type(pw_receive)}')
    # print(f'db의 pw 타입: {type(user["user_pw"])}')

    user['user_pw'] == pw_receive
    # print(user['user_pw'] == pw_receive)
    if user['user_pw'] == pw_receive : 
        return jsonify({'result' : 1}) 
    else : 
        return jsonify({'result' : 0}) 
    #로그인 요청

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
    # print(searchdb)
    return jsonify({'keyword': searchdb})

@app.route("/api/wish_button", methods = ['POST'])
def wish_button_api():
    #희망과목 담기 요청
    wish_class = request.form['wishlist']
    # db.user_info.insert_one({'wishlist' : [wish_class]})
    db.user_info.update_one(
        {'user_id':'jaehyung1'},
        {'$push':{'wishlist': wish_class}}
    )
    return jsonify({'msg' : 'user_id에 class_code 넣었슴다~'})


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
        # print("-----------", class_info)
        class_info_list.append(class_info)
        # print("+++++++++++", class_info_list)
    return jsonify({'result': class_info_list, 'code_list' : wishlist})

@app.route("/api/enroll_button", methods=["POST"])
def enroll_button_api():
    #수강신청 요청
    enrollcode = request.form['enrollment']
    user_id = request.form['user_id']
     
    db.user_info.update_one(
        {'user_id': user_id},
        {'$push':{'enrollment': enrollcode}}
    )
    # if doc == doc :
    #     return jsonify({'msg': '중복입니다.'})
    # else :
    return jsonify({'msg': '신청되었습니다.'})

@app.route("/api/wishlist_delete", methods=["POST"])
def wishlist_delete_api():

    # 희망과목 삭제버튼
    class_code_receive = request.form['code_give']
    user_id = request.form['user_id']

    db.user_info.update_one(
        {'user_id': user_id},
        {'$pull':{'wishlist': class_code_receive}}
    )

    return jsonify({'msg' : '삭제되었습니다.'})

@app.route("/api/enroll_list", methods=["POST"])
def get_enroll_list_api():
    #신청내역페이지
    # user_id 받아오기
    id_receive = request.form['user_id']
    # user_id로 user_data 받아오기
    user_data = list(db.user_info.find({'user_id':id_receive},{'_id' : False}))
    # print(user_data)
    class_info_list = []
    # 신청내역리스트 추출
    enrollment = user_data[0]['enrollment']
    # print(enrollment)
    # 신청내역리스트에서 과목코드 추출
    # print(e)
    for e in enrollment:
        # 추출한 과목코드로 강의정보 받아오기
        class_info = db.class_list.find_one({'class_code': e}, {'_id':False})
        
        # print("-----------", class_info)
        # 강의정보리스트에 강의정보 넣기
        class_info_list.append(class_info)
        
        # print("+++++++++++", class_info_list)
    return jsonify({'result' : class_info_list, 'code_list' : enrollment})

@app.route("/api/enroll_delete", methods=["POST"])
def delete_enroll_api():

    # 신청내역삭제요청
    # 데이터 받아오기
    user_id = request.form['user_id']
    chklist = request.form['chklist']
    # ,로 자르기
    delcode = chklist.split(',')
    
    user_data = list(db.user_info.find({'user_id':user_id},{'_id' : False}))
    enrollment = user_data[0]['enrollment']
    # 새로 넣을 배열 생성(배열 빼기 연산)
    new_arr = list(set(enrollment)-set(delcode))
    # print(new_arr)
    db.user_info.update_one({'user_id':user_id},{'$set':{'enrollment': new_arr}})
    
    return jsonify({'msg' : '취소 되었습니다.'})
    
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
    
    print(draw_info)
    return jsonify({'result' : draw_info})

if __name__ == '__main__':
   app.run('0.0.0.0', port=5001, debug=True)