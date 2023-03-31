<aside>
💡 온보딩 11조 프로젝트 수강신청 사이트입니다. 로그인, 회원가입 기능, 강의목록 표시 및 검색, 관심과목 등록 및 삭제, 수강신청 및 신청목록 삭제, 시간표 그리기 등 기능이 있습니다.
</aside>
<br><br>

## 🗓프로젝트 기간

2023년 03월 27일 (월) 15:00 ~ 2023년 03월 30일 (목) 09:00
발표 2023년 03월 30일 (목) 09:00 ~ 09:10
<br><br>

## 👪팀원
모두가 얼떨결에 Full-stack 개발

- `강재형` - 시간표 로직 구현, JWT토큰
- `김석호` - 회원가입, 로그인, JWT토큰
- `김효환` - 강의목록, 검색기능, 사이드바, JWT토큰
- `신민철` - 관심과목, JWT토큰
- `왕정민` - 신청내역, JWT토큰
<br><br>

## 기술스택 & 툴
SKILL
<br>
<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=Python&logoColor=white"> <img src="https://img.shields.io/badge/CSS-1572B6?style=for-the-badge&logo=CSS&logoColor=white"> <img src="https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jQuery&logoColor=white"> <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=JavaScript&logoColor=white"> <img src="https://img.shields.io/badge/HTML-E34F26?style=for-the-badge&logo=HTML&logoColor=white"> <img src="https://img.shields.io/badge/MongoDB-47A248?style=for-the-badge&logo=MongoDB&logoColor=white"> <img src="https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=Flask&logoColor=white">

TOOL
<br>
<img src="https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=Git&logoColor=white"> <img src="https://img.shields.io/badge/Visual Studio Code-007ACC?style=for-the-badge&logo=Visual Studio Code&logoColor=white"> <img src="https://img.shields.io/badge/Sourcetree-0052CC?style=for-the-badge&logo=Sourcetree&logoColor=white"> <img src="https://img.shields.io/badge/Amazon AWS-232F3E?style=for-the-badge&logo=Amazon AWS&logoColor=white"> <img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=GitHub&logoColor=white">
<br><br>

## 초안 API명세
우리 초기버전 사진 넣기
<br><br>

## API 명세
이미지 첨부
<br><br>

## 데이터 명세
```
수업시간 변수 : [{'day' : '요일',
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


## API 구현 기능
- 회원가입 기능
- 로그인 기능
- 로그인 인증 기능
- 강의목록 호출 기능
- 강의목록 검색 기능
- 관심과목 담기 기능
- 관심과목 호출 기능
- 관심과목 삭제 기능
- 수강신청 기능
- 신청내역 호출 기능
- 신청내역 삭제 기능
- 시간표 그리기 기능
<br><br>

## 트러블슈팅
`강재형`
- [x]  ~~ormData의 body에 리스트를 태울 수 없는 문제 발생~~
<br>→반복문으로 해결
- [x]  ~~myclasspage에서 표 작게나오는 문제~~
<br>→
- [x]  ~~시간표 한번 더 누르면 hide~~
<br>→ 

`김석호`
- [x]  ~~로그인 페이지  로그인버튼 /회원가입 버튼 만들기~~
- [x]  ~~회원가입 완료 시 로그인페이지로 이동~~
- [x]  ~~로그인 성공시 알림창 후 다음페이지로 이동/실패시 안내창과 함께 로그인페이지 머무르기~~
<br>→ 능력 부족으로 인해 구현 못함 공부를 더 해야할 필요가 있다.
- [ ]  로그인 시 토큰 발생 후 쿠키로 저장
<br>→ 능력 부족으로 인해 구현 못함 공부를 더 해야할 필요가 있다.

`김효환`
- [x]  ~~user_id와 class_list db들간의 연결 → $push 로 해결~~
<br>→$push로 해결
- [ ]  class_list 속성 추가
- [ ]  사이드바추가 (현재 classes 에만 들어가있음) static에 css,js sidebar 인포트 필요
- [ ]  사이드바에 시계 추가완료  사이드바 인포트 하면서 clock js,css 도 인포트 필요
- [ ]  로그인 회원가입 css추가
- [ ]  회원가입 폼 조건에  따른 에러문구 추가

`신민철`
- [x]  ~~신청 및 삭제 버튼이 작동하지 않음~~
<br>→temp_html에 ${class_code}로 해결
<br>→’${class_code}’의 ‘’로 문자를 string로 해결
- [ ]  체크박스를 체크해서 신청 및 삭제
- [ ]  신청리스트 중복체크

`왕정민`
- [x]  ~~myclasspage에서 표 작게 나오는거 해결
<br>→
- [x]  ~~체크박스 체크해서 여러개 삭제하는 기능~~
<br>→
- [x]  ~~표 css~~
<br>→
- [ ]  사이드바 토글
<br>→
<br>

## 결과물

<로그인>
![이미지 001](https://user-images.githubusercontent.com/36254544/229111205-0d93b11b-174c-44d3-b3c2-e2e653963f0b.png)
<br><강의목록 조회>
![이미지 002](https://user-images.githubusercontent.com/36254544/229111211-740e2f02-4e79-4986-b58b-485f347a0b54.png)
<br><강의 검색>
![이미지 13](https://user-images.githubusercontent.com/36254544/229111901-1acf8b52-73b1-4689-811e-fc7322a6a677.png)
<br><관심과목 조회>
![이미지 005](https://user-images.githubusercontent.com/36254544/229111245-3b91fbd8-8296-4d5f-b563-d5d8a8fb494a.png)
<br><신청과목 조회
![이미지 006](https://user-images.githubusercontent.com/36254544/229111253-b0803cd5-fd18-46b2-833a-65fdf0a1b6fa.png)


## 배포 URL
http://sugangpage.eba-iyefhen2.ap-northeast-2.elasticbeanstalk.com/
<br><br><br><br>


