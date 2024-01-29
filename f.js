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

    // 使用Fetch API發送POST請求到後端
    fetch(' http://127.0.0.1:5000/back', {
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

document.getElementById('ab').addEventListener('click', function() {
    // 获取所有具有 data-marker="setTo87" 的输入字段
    const inputFields = document.querySelectorAll('.score-input');

    // 将这些输入字段的值设置为87
    inputFields.forEach(function(input) {
        input.value = '87';
    });
});
function sub(){
    const page=document.body;
    page.classList.remove('loginpage');
    page.classList.add('d-page');
    document.getElementById('out').style.display = "none";
    document.getElementById('in').style.display = "block";
}
document.getElementById('save').addEventListener('click',function(){
    const inputsorce =confirm('是否要儲存?');
    if(inputsorce){
        alert('登入成功！');
        sub();
    }
})

function updateTime() {
    var now = new Date();
    var hours = now.getHours();
    var minutes = now.getMinutes();
    var seconds = now.getSeconds();
    document.getElementById('currentTime').innerText = hours + ':' + minutes + ':' + seconds;
}

// 在页面加载时更新时间，并且每秒更新一次
updateTime();
setInterval(updateTime, 1000);

// 显示新增项目对话框
function showAddItemDialog() {
    var title = prompt('请输入标题:');
    var content = prompt('请输入内容:');
    if (title && content) {
        // 创建新的项目
        var newItem = document.createElement('div');
        newItem.innerHTML = '<strong>' + title + '</strong><br>' + content;
        document.body.appendChild(newItem);
    }
}

// 登出操作，这里只是简单地提示信息
function sm(){
    const it=confirm('是否要送出?');
    if(it){
        fetch(' http://127.0.0.1:5000/s', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data.captcha)
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