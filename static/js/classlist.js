const btn = document.getElementById('showBtn')

$(document).ready(function () {

    show_comment()
    hideClassComment()
    search()
});


function hideClassComment() {
    $('#hideContainer').hide()
}

function search(keyword) {
    $('#searchForm').keyup(function () {
        keyword = $(this).val()
        // $("#class_table > #column > tr").hide()
        console.log('키보드 입력데이터 :', keyword)

        let formData = new FormData()
        formData.append("keyword", keyword)

        fetch('/api/searchlist', { method: 'POST', body: formData }).then((response) => response.json()).then((data) => {
            let searchKeyWord = data['keyword']
            console.log(searchKeyWord)
            $('#column').empty()
            searchKeyWord.forEach((a) => {
                let class_name = a['class_name']
                let instructor = a['instructor']
                let class_code = a['class_code']
                let class_day = a['class_time'][0]['day']

                let class_stime = a['class_time'][0]['start_time']
                let class_etime = a['class_time'][0]['end_time']
                
                // let class_time = class_stime.substr(0, 2) + ":" + class_stime.substr(2, 2) + "-" + class_etime.substr(0, 2) + ":" + class_etime.substr(2, 2)

                let temp_html = `<tr>
                                    <td>${class_code}</td>
                                    <td>${class_name}</td>
                                    <td>${instructor}</td>
                                    <td>${class_day}</td>
                                    <td>${class_stime} - ${class_etime}</td>
                                    <td><button type="button" onclick="shoppingBasket('${class_code}')" class="showBtn">장바구니담기</button></td>
                                </tr>`
                $('#column').append(temp_html)
            })

        })

    })
}


function show_comment() {
    fetch('/api/classlist').then((res) => res.json()).then((data) => {
        let rows = data['result']
        $('#column').empty()

        rows.forEach((a) => {
            let class_name = a['class_name']
            let instructor = a['instructor']
            let class_code = a['class_code']
            let class_day = a['class_time'][0]['day']
            let class_stime = a['class_time'][0]['start_time']
            let class_etime = a['class_time'][0]['end_time']

            let temp_html = `<tr>
                                    <td>${class_code}</td>
                                    <td>${class_name}</td>
                                    <td>${instructor}</td>
                                    <td>${class_day}</td>
                                    <td>${class_stime} - ${class_etime} </td>
                                    <td><button type="button" onclick="shoppingBasket('${class_code}')" class="showBtn">장바구니담기</button></td>
                            </tr>`
            $('#column').append(temp_html)
        })
    })

}




function shoppingBasket(class_code){
    // alert('장바구니 연결')
    let formData = new FormData();
    formData.append("wishlist", class_code);

    fetch('/wish_button', { method: "POST", body: formData, }).then((res) => res.json()).then((data) => {
      alert(data["msg"]);
      console.log(data)
      
    })
}

// function preview() {
//     $('#hideContainer').show()

//     let formData = new FormData()
//     formData.append("keyword", keyword)

//     fetch('/searchlist', { method: 'POST', body: formData }).then((response) => response.json()).then((data) => {
//         let searchKeyWord = data['keyword']
//         console.log(searchKeyWord)
        
//         rows.forEach((a) => {
//             let class_name = a['class_name']
//             let instructor = a['instructor']
//             let class_code = a['class_code']
//             let class_day = a['class_time'][0]['day']
//             let class_stime = a['class_time'][0]['start_time']
//             let class_etime = a['class_time'][0]['end_time']

//         })
        
//     })

// }



