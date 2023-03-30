function setClock(){
    const dateInfo = new Date(); 
    const hour = modifyNumber(dateInfo.getHours());
    const min = modifyNumber(dateInfo.getMinutes());
    const sec = modifyNumber(dateInfo.getSeconds());
    const year = dateInfo.getFullYear();
    const month = dateInfo.getMonth()+1; //monthIndex를 반환해주기 때문에 1을 더해준다.
    const date = dateInfo.getDate();
    document.getElementById("time").innerHTML = hour + ":" + min  + ":" + sec;
    document.getElementById("date").innerHTML = year + "년 " + month + "월 " + date + "일";
}
function modifyNumber(time){
    if(parseInt(time)<10){
        return "0"+ time;
    }
    else
        return time;
}
window.onload = function(){
    setClock();
    setInterval(setClock,1000); //1초마다 setClock 함수 실행
}
