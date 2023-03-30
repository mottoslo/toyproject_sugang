const form = document.getElementById('form')
const id = document.getElementById('user_id')
const passWord = document.getElementById('user_pw')
const rePassword = document.getElementById('re_pw')
const username = document.getElementById('user_name')

// 정규식
// id, pw
const regIdPw = /^[a-zA-Z0-9]{4,12}$/;
// 이름
const regName = /^[가-힣a-zA-Z]{2,15}$/;
// 이메일
const regMail = /^([\w-]+(?:\.[\w-]+)*)@((?:[\w-]+\.)*\w[\w-]{0,66})\.([a-z]{2,6}(?:\.[a-z]{2})?)$/;
// 년도
const regYear = /^[1-2]{1}[0-9]{0,4}$/;


//실패 small 라벨, input 색 바꿔주는 처리
function showError(input, message) {
    const formControl = input.parentElement;
    formControl.className = 'form-control error';
    const small = formControl.querySelector('small');
    small.innerText = message;
}

//성공시 small 라벨, input 색 바꿔주는 처리
function showSuccess(input) {
    const formControl = input.parentElement;
    formControl.className = 'form-control success';
    const small = formControl.querySelector('small');
    // small.innerText = message;
}

//form 이벤트 처리
form.addEventListener('keyup',function(e) {
    e.preventDefault()
    // console.log('click')

    if(username.value === '' ){
        showError(username, '필수 항목입니다')
    }else if(username.value.length < 2){
        showError(username, '이름은 2글자 이상이여야 합니다')
    }else{
        showSuccess(username)
    }

    if(id.value === ''){
        showError(id, '필수 항목입니다')
    }else if(id.value.length < 5){
        showError(id, '아이디는 5글자 이상이여야 합니다')
    }else{
        showSuccess(id)
    }

    if(passWord.value === ''){
        showError(passWord, '필수 항목입니다')
    }else if(passWord.value.length < 5){
        showError(passWord, '비밀번호는 5글자 이상이여야 합니다.')
    }else{
        showSuccess(passWord)
    }

    if(rePassword.value === ''){
        showError(rePassword, '필수 항목입니다')
    }else if(rePassword.value !== passWord.value){
        showError(rePassword, '비밀번호가 일치하지 않습니다.')
    }else{
        showSuccess(rePassword)
    }

})






