function submitLoginForm() {
    // 獲取輸入值
    var username = document.getElementById('username').value;
    var password = document.getElementById('password').value;
    var captcha = document.getElementById('captcha').value;

    // 構建要發送的資料
    var data = {
        username: username,
        password: password,
        captcha: captcha
    };
    cc=data.captcha
    // 使用Fetch API發送POST請求到後端
    fetch('http://192.168.1.117:5000/back', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(result => {
        // 根據後端回應處理前端行為
        if (result.success) {
            alert('登入成功！');  // 這裡可以改為跳轉畫面等操作
            const page=document.body;
            document.getElementById('in').style.display = "none";
            
            document.getElementById('out').style.display = "block";
        } else {
            alert('登入失敗，請檢查帳號、密碼和驗證碼。');
        }
    });
}

function sub(){
    const page=document.body;
    page.classList.remove('loginpage');
    page.classList.add('d-page');
    document.getElementById('out').style.display = "none";
    document.getElementById('in').style.display = "block";
}
// 登出操作，这里只是简单地提示信息
function sm(){
    const it=confirm('是否要送出?');
    if(it){
        fetch('http://192.168.1.117:5000/s', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            }
        })
        .then(response => response.json())
        .then(result => {
            // 根據後端回應處理前端行為
            if (result.success) alert('送出成功！');
        });
    }
}
function logout() {
    const ix=confirm('是否要登出?');
    if(ix){
        document.getElementById('out').style.display = "none";
        document.getElementById('in').style.display = "block";
    }
}