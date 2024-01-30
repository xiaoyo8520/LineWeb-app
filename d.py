from flask import Flask, request, jsonify
from flask_cors import CORS
import json,requests
app = Flask(__name__)
CORS(app)
un='user123'
pw='pass123'
tk=[]
tk.append('0')
ch=''
# 假設這是一個用於處理登入請求的端點
@app.route('/back', methods=['POST'])
def login():
    # 從前端請求中獲取用戶名、密碼和驗證碼
    data = request.json
    username = data.get('username')
    password = data.get('password')
    captcha = data.get('captcha')
    # 在這裡添加你的驗證邏輯，例如檢查用戶名、密碼和驗證碼是否正確
    # 在實際應用中，這可能包括查詢數據庫、使用加密函數檢查密碼等

    # 假設通過驗證，返回成功的回應
    
    if username == un and password == pw and captcha in tk:
        ch=captcha
        return jsonify({'success': True, 'message': 'Login successful'})
    else:
        return jsonify({'success': False, 'message': 'Invalid credentials or captcha'})

@app.route('/sd', methods=['POST'])
def save_data():
    try:
        data = request.get_json()
        tk.append(data.token)
        return jsonify({'success': True, 'message': 'Data saved successfully'})
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)})

@app.route('/s',methods=['POST'])
def s():
    try:
        data=request.get_json()
        if data == ch :
            responee=request.post('https://line-web-app.vercel.app/b.py/bot',da={'ch':ch})
        return jsonify({'success': True, 'message': 'Data saved successfully'})
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)})
if __name__ == '__main__':
    app.run()
