function auth() {
    let user_info = {}
    $.ajax({
        type: "GET",
        url: "/api/isAuth",
        data: {},
        async: false,
        success: function (response) {
            if (response['result'] == 'success') {
                // 로그인한 사용자면 닉네임을 보여주는 알람을 띄움!
                user_info = response['user_info']

            } else {
                alert(response['msg']) 
                window.location.href = '/login'
            }
        
        }
         
    })
    return user_info
}