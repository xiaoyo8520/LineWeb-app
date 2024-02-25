let userId = null;
function initializeLiff(myLiffId) {
            liff.init({ 
                　liffId: myLiffId
            }) .then(() => { 
             if (!liff.isLoggedIn()) { 
               alert("使用者未登入"); 
               liff.login(); 
              } else { 
               alert("使用者已登入"); 
               liff.getProfile() 
               .then(profile => { 
                const name = profile.displayName 
                userId = profile.userId;
               }) 
               .catch((err) => { 
                console.log('error', err) ; 
               });
               } 
            } 
            ).catch((err) => { 
            console.log('初始化失敗') 
})};

initializeLiff('2003304114-bdgVMe9K');
function slm() {
    // 獲取輸入值
    var username = document.getElementById('username').value;
    var password = document.getElementById('password').value;

    // 構建要發送的資料
    var data = {
        username: username,
        password: password
    };
     if (1) {
            alert('登入成功！');  // 這裡可以改為跳轉畫面等操作
            const page=document.body;
            document.getElementById('in').style.display = "none";
            
            document.getElementById('out').style.display = "block";
        } else {
            alert('登入失敗，請檢查帳號、密碼和驗證碼。');
       }
}

function sub(){
    const page=document.body;
    page.classList.remove('loginpage');
    page.classList.add('d-page');
    document.getElementById('out').style.display = "none";
    document.getElementById('in').style.display = "block";
}
// 登出操作，这里只是简单地提示信息
function goback(){
    const it=confirm('是否要送出?');
    if(it){
                var dat={uid : userId}
                fetch('https://b03b-114-33-4-188.ngrok-free.app/back', {
                body: JSON.stringify(dat),
                cache: 'no-cache',
                headers: {
                    'user-agent': 'Mozilla/4.0 MDN Example',
                    'content-type': 'application/json'
                },
                method: 'POST',
                mode: 'cors',
                })
                .then(response => response.json()) // 輸出成 json
                
    }
}    
function sm(){
    const it=confirm('是否要送出?');
    if(it){
            liff.sendMessages([
      {
            type: 'text',
            text: '已完成'
      }
    ])
      .then(() => {
        console.log('message sent');
      })
      .catch((err) => {
        console.log('error', err);
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
