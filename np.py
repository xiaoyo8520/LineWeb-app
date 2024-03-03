import requests
from flask import Flask, request

app = Flask(__name__)
@app.route('/', methods=['POST', 'GET'])
def hello_world():
    authorizeCode = request.args.get('code')
    token = getNotifyToken(authorizeCode)
    print(token)
    lineNotifyMessage(token, "恭喜你連動")
    return "aaaa"

@app.route('/ac/<name>/<msg>',methods=['POST','GET'])
def hello_wor(name,msg):
    token=f'{name}'
    lineNotifyMessage(token, f'{msg}')
    return f'acbc'

def getNotifyToken(AuthorizeCode): #運用網址'code'參數和相關資訊，生成oauth_token
    body = {
        "grant_type": "authorization_code",
        "code": AuthorizeCode,
        "redirect_uri": 'https://line-web-app.vercel.app/np.py',
        "client_id": '9BhYhKzGtasty5jOlfsPGK',
        "client_secret": 'j0KmCm6UHc14lyD0qQeQqf3NTER2K2p8vFpIsjlJRD5'
    }
    r=requests.post("https://notify-bot.line.me/oauth/token", data=body)
    return r.json()["access_token"]

def lineNotifyMessage(token, msg): #根據token，向notify發出post，發送msg
    headers = {
        "Authorization": "Bearer " + token,
        "Content-Type": "application/x-www-form-urlencoded"
    }
    payload = {'message': msg}
    r = requests.post("https://notify-api.line.me/api/notify", headers=headers, data=payload)
    return r.status_code

if __name__ == '__main__':
    app.run()
