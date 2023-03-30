function drawtable(class_list) {
    let num_hrs = 10;
    $('#timetableid').css('opacity', 1);
    $('#timetableid').css('width', '1000px');
    $('#timetableid').css('height', '800px');
    
    $('#timetableid').append(
        `<tr>
                <th class = 'timeth'></th>
                <th class = 'timeth'>월</th>
                <th class = 'timeth'>화</th>
                <th class = 'timeth'>수</th>
                <th class = 'timeth'>목</th>
                <th class = 'timeth'>금</th>
                <th class = 'timeth'>토</th>
            </tr>`
    )
    for (var i = 1; i < num_hrs + 1; i++) {
        $('#timetableid').append(
            `<tr>
                <th class = 'timeth' rowspan = '4'>${i + 8}</th>
                <td class = 'timetd' id = 'p${i}1'></th>
                <td class = 'timetd' id = 'p${i + 10}1'></td>
                <td class = 'timetd' id = 'p${i + 20}1'></td>
                <td class = 'timetd' id = 'p${i + 30}1'></td>
                <td class = 'timetd' id = 'p${i + 40}1'></td>
                <td class = 'timetd' id = 'p${i + 50}1'></td>
            </tr>`
        )


        for (var j = 2; j < 5; j++) {
            $('#timetableid').append(
                `<tr>
                <td class = 'timetd' id = 'p${i}${j}'></td>
                <td class = 'timetd' id = 'p${i + 10}${j}'></td>
                <td class = 'timetd' id = 'p${i + 20}${j}'></td>
                <td class = 'timetd' id = 'p${i + 30}${j}'></td>
                <td class = 'timetd' id = 'p${i + 40}${j}'></td>
                <td class = 'timetd' id = 'p${i + 50}${j}'></td>
            </tr>`
            )
        }
    }

    let formData = new FormData();
    formData.append('code_list_len', class_list.length)
    for (var i = 0; i < class_list.length; i++) {
        formData.append(`code_list${i}`, class_list[i])
    }
    fetch('api/get_table_position', { method: "POST", body: formData }).then((res) => res.json()).then((data) => {
        let draw_info = data['result']
        draw_info.forEach((elem) => {
            positions = elem['class_pos']
            color = elem['class_color']

            positions.forEach((onetime_pos) => {
                onetime_pos.forEach((pos) => {
                            $(`#p${pos}`).css('background-color', color)
                })
            })
        })
    })

    let btn = document.querySelector('#drawbutton')
    btn.textContent = '시간표 지우기'
    btn.setAttribute('onClick', 'deletetable()')

    // temp_poslist.forEach((elem) => {
    //     $(`#p${elem}`).css('background-color', 'green')
    // })
}

function deletetable() {
    $('#timetableid').hide()
    let btn = document.querySelector('#drawbutton')
    btn.setAttribute('onClick', 'showtable()')
    btn.textContent = '시간표 그리기'
}
function showtable() {
    $('#timetableid').show()
    let btn = document.querySelector('#drawbutton')
    btn.setAttribute('onClick', 'deletetable()')
    btn.textContent = '시간표 지우기'
}
