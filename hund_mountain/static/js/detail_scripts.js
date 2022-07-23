
// html 특수문자를 치환하는 함수
function unescapeHtml(str){
    if(str == null){return "";}else{
    return str
        .replace('&lt;', '<')
        .replace('&gt;', '>')
        .replace('&nbsp;', ' ')
    }
}

// 개관 내용에 대해 <, > 바꿔주기 위해 실행
window.onload=function(){
    var overview = document.getElementById("overview_con");
    var overview_text = overview.textContent
    overview.textContent = unescapeHtml(overview_text)


    var details = document.getElementById("details_con");
    var details_text = details.textContent
    details.textContent = unescapeHtml(details_text)
}