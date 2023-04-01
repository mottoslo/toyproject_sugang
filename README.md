## 💡 우리 프로젝트는요! <br>
수강신청 사이트입니다. 로그인, 회원가입 기능, 강의목록 표시 및 검색, 관심과목 등록 및 삭제, 수강신청 및 신청목록 삭제, 시간표 그리기 등 기능이 있습니다.
<br><br><br>

## 🗓프로젝트 기간
<b>총 기간 :</b> 2023.03.27 (월) 15:00 ~ 2023.03.30 (목) 21:00 <br><br>
<b>기획 및 설계 :</b> 2023.03.27 (월) 15:00 ~ 2023.03.28 (화) 새벽 <br>
<b>제작 :</b> 2023.03.28 (화) 새벽 ~ 2023.03.30 (목) 21:00 <br>
<b>발표 :</b> 2023.03.30 (목) 21:00 ~ 21:10
<br><br><br>

## 👪팀원
모두가 얼떨결에 Full-stack 개발

- `강재형` - 시간표 로직 구현, JWT토큰, API명세, DB설계
- `김석호` - 회원가입, 로그인, JWT토큰
- `김효환` - 강의목록, 검색기능, 사이드바, JWT토큰
- `신민철` - 관심강의, JWT토큰
- `왕정민` - 신청내역, JWT토큰
<br><br><br>

## 🛠기술스택 & 툴
<b>[ SKILL ]</b>
<br>
<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=Python&logoColor=white"> <img src="https://img.shields.io/badge/CSS-1572B6?style=for-the-badge&logo=CSS&logoColor=white"> <img src="https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jQuery&logoColor=white"> <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=JavaScript&logoColor=white"> <img src="https://img.shields.io/badge/HTML-E34F26?style=for-the-badge&logo=HTML&logoColor=white"> <img src="https://img.shields.io/badge/MongoDB-47A248?style=for-the-badge&logo=MongoDB&logoColor=white"> <img src="https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=Flask&logoColor=white">

<b>[ TOOL ]</b>
<br>
<img src="https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=Git&logoColor=white"> <img src="https://img.shields.io/badge/Visual Studio Code-007ACC?style=for-the-badge&logo=Visual Studio Code&logoColor=white"> <img src="https://img.shields.io/badge/Sourcetree-0052CC?style=for-the-badge&logo=Sourcetree&logoColor=white"> <img src="https://img.shields.io/badge/Amazon AWS-232F3E?style=for-the-badge&logo=Amazon AWS&logoColor=white"> <img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=GitHub&logoColor=white">
<br><br><br>

## ✏초안 API명세

![wireframe_1stdraft](https://user-images.githubusercontent.com/36254544/229122453-dd38515d-230f-4c1c-9e07-a9eb702b1091.png)
![api_info_1stdraft](https://user-images.githubusercontent.com/36254544/229122545-b2d0e067-c953-459d-bcd3-5404d3323158.PNG)

<br><br>

## 📑API 명세
![이미지 15](https://user-images.githubusercontent.com/36254544/229122767-9e811b2d-7e3a-4e79-88c8-daabbfd31c5d.png)

<br><br>

## 📈데이터 명세
```
*수업시간 변수 : [{'day' : '요일',
                             'start_time' : '1400',
                             'end_time' : '1530'}]

draw_info : [{'class_name' : '과목이름',
                      'class_color' : '과목색깔',

                      'class_pos' : [111,112,113,114]

                       }]

db.user_list = {'user_name' : '이름',
                         'user_id' : '아이디',
                         'user_pw' : '비밀번호'}

db.user_info = {'user_id' = '아이디', 

                          'wishlist' : ['과목코드들'],

                           'enrollment' : ['과목코드들']}

data['result']['enrollment'] = ['STAT420', 'STAT520', 'COSE423]

db.class_list = {'class_name' : '수업 이름',

                          'instructor' : '강사 이름',
                          'class_time : *수업시간변수,
                          'class_code' : '과목코드',

                          'class_max' : '최대수강인원'

                          'class_now' : '현재신청인원'}
```
<br>

## 📌API 구현 기능
- 회원가입 기능
- 로그인 기능
- 로그인 인증 기능
- 강의목록 호출 기능
- 강의목록 검색 기능
- 관심강의 담기 기능
- 관심강의 호출 기능
- 관심강의 삭제 기능
- 수강신청 기능
- 신청내역 호출 기능
- 신청내역 삭제 기능
- 시간표 그리기 기능
<br><br>

## 💡트러블슈팅
`강재형`
- [x]  ~~ormData의 body에 리스트를 태울 수 없는 문제 발생~~
<br>→ 반복문으로 해결
- [x]  ~~myclasspage에서 표 작게나오는 문제~~
<br>→ 시간표 table을 담고있는 태그의 css가 누락되어있었음
- [x]  ~~시간표 한번 더 누르면 hide~~
<br>→ table의 기본 display를 hide 후, 버튼을 누르면 table의 display옵션을 변경, button 자체의 onclick event와 innerHTML도 수정하여 버튼의 기능, 모양을 바꿔줌
- [x]  그려진 시간표에서 한 강의 안의 boarder를 지워주어 에타처럼 만들고, 강의명 써주기 (구조변경필요)
<br>→ table태그는 좌에서 우로 그려지기 때문에 이렇게 적용하려면 많이 복잡했다. 애초에 기능 구현 전에 설계를 잘 해서 각 구역을 div로 잡았으면 좋았을텐데......
      추후 비슷한걸 진행하게 되면 요일순서대로 그려지게 하고, 각 요일을 div의 class나 id로 잡아서 하면 좋을거같다.
- [x]  ~~API 명세 개선 필요~~
<br>→ GET, POST 요청들이 어떤 object를 주고받는지, 각 필드명과 데이터 타입은 무엇인지 명시하여 개선함

 **<후기>**
첫 프로젝트이자 github을 사용한 첫 협업 경험이었는데, 여러명이 각자 기능을 구현하고 이를 합칠 때 발생할 수 있는 문제를
많이 경험할 수 있어 좋았다. 프로젝트 주제 자체가 희망과목 담기, 수강신청, 시간표 그리기 등의 기능으로 각각의 기능 간에 
데이터를 주고받을 일이 많아 이러한 경험을 하게된 것 같다. 재밌는 경험이었다.


`김석호`
- [x]  ~~로그인 페이지  로그인버튼 /회원가입 버튼 만들기~~
<br>→ html의 태그 기능을 이해하고 onchlick버튼 기능을 사용하여 해결할 수 있었다.
- [x]  ~~회원가입 완료 시 로그인페이지로 이동~~
<br>→ window.location.reload() 를 참고해서 접근
<br>→ window.location.herf(’/이동할 페이지’) 해당 코드를 통해 해결할 수 있었다.
<br>→ 회원가입시 로그인페이지로 이동하는 개념과 if / else 조건문을 참고하여 해결 할 수 있었다.
- [x]  ~~로그인 성공시 알림창 후 다음페이지로 이동/실패시 안내창과 함께 로그인페이지 머무르기~~
<br>→ 회원가입시 로그인페이지로 이동하는 개념과 if / else 조건문을 참고하여 해결 할 수 있었다.
- [ ]  로그인 시 토큰 발생 후 쿠키로 저장
<br>→ 능력 부족으로 인해 구현 못함 공부를 더 해야할 필요가 있다.

`김효환`
- [x]  ~~user_id와 class_list db들간의 연결 → $push 로 해결~~
<br>→ $push로 해결
- [ ]  class_list 속성 추가
- [ ]  사이드바추가 (현재 classes 에만 들어가있음) static에 css,js sidebar 인포트 필요
- [ ]  사이드바에 시계 추가완료  사이드바 인포트 하면서 clock js,css 도 인포트 필요
- [ ]  로그인 회원가입 css추가
- [ ]  회원가입 폼 조건에  따른 에러문구 추가

`신민철`
- [x]  ~~신청 및 삭제 버튼이 작동하지 않음~~
<br>→ temp_html에 ${class_code}로 해결
<br>→ ’${class_code}’의 ‘’로 문자를 string로 해결
- [ ]  체크박스를 체크해서 신청 및 삭제
- [ ]  신청리스트 중복체크

`왕정민`
- [x] ~~enrollment 리스트에서 과목코드를 추출하여 해당 과목의 상세정보를 class_list 컬렉션에서 가져오기~~
<br>→ enrollment가 리스트여서 받아와서 한꺼풀 벗기고 for문을 돌려 해결!
- [x]  ~~myclasspage에서 표 작게 나오는 부분 해결하기~~
<br>→ 관심강의 페이지와 신청과목 페이지의 마크업 구조가 달라서 이 부분을 맞춰줌 (추후 수정)
- [x]  ~~체크박스를 이용하여 여러 개를 한꺼번에 삭제하는 기능 만들기~~
<br>→ 버튼의 name 속성을 같은 이름으로 해야 함 
<br>→ 체크 된 체크박스의 id를 가져와서 each() 메서드를 이용해 리스트에 push()하여 넘김
<br>→ 체크 된 체크박스의 수를 카운트하여 체크하지 않은 상황에 대한 예외 처리를 함
<br>→ <app.py>에서 받은 내용이 리스트가 아니여서 쉽표(,)로 split 하고, 다시 리스트로 만듬
<br>→ user id로 가져온 원래 리스트와 체크 된 리스트 연산(리스트 빼기 연산 가능!)으로 새 리스트를 생성하여 DB를 수정함
<br>→ 참고할 것은 mongoDB update를 할 때 항목에 리스트로 들어있으면 리스트가 그 안으로 들어가는게 아닐까? 생각했는데 아님 ㅋ_ㅋ
<br>→ ['a', 'b', 'c', ...] 가 ['a', 'b', 'c', [new arr], ...] 이렇게 될까 했는데 그렇지 않고, 잘 수정됨
<br>→ 오라클과 달리 mongoDB는 리스트가 데이터로 삽입될 수 있음. 그렇기 때문에 enrollment의 가장 작은 단위가 리스트임.
<br>→ 리스트 안의 내용까지 접근 못하는 것과 마찬가지로 리스트가 그 안으로 삽입되는 것이 아니라 리스트 자체가 잘 수정되었음
- [x]  ~~표 css~~
<br>→ 부트스트랩을 이용해 테이블을 심플하게 디자인 함
- [ ]  사이드바 토글
<br>→ 추후 수정 예정
<br>

## ✨결과물

#### <회원가입>
![이미지 14](https://user-images.githubusercontent.com/36254544/229124821-b8408409-c2fb-4bc1-aa11-0670c89c415d.png)
<br>
#### <로그인>
![이미지 001](https://user-images.githubusercontent.com/36254544/229111205-0d93b11b-174c-44d3-b3c2-e2e653963f0b.png)
<br>
#### <강의목록 조회>
![이미지 002](https://user-images.githubusercontent.com/36254544/229111211-740e2f02-4e79-4986-b58b-485f347a0b54.png)
<br>
#### <강의 검색>
![이미지 13](https://user-images.githubusercontent.com/36254544/229111901-1acf8b52-73b1-4689-811e-fc7322a6a677.png)
<br>
#### <관심과목 조회>
![이미지 005](https://user-images.githubusercontent.com/36254544/229111245-3b91fbd8-8296-4d5f-b563-d5d8a8fb494a.png)
<br>
#### <신청과목 조회>
![이미지 006](https://user-images.githubusercontent.com/36254544/229111253-b0803cd5-fd18-46b2-833a-65fdf0a1b6fa.png)

<br><br>
## 🖥배포 URL
http://sugangpage.eba-iyefhen2.ap-northeast-2.elasticbeanstalk.com/
<br><br><br><br>


