from flask import Flask,request

# 載入 json 標準函式庫，處理回傳的資料格式
import json,requests,secrets
# 載入 LINE Message API 相關函式庫
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage ,BubbleContainer,FlexSendMessage,MessageAction, ConfirmTemplate,TemplateSendMessage
from linebot.models import *
app = Flask(__name__)
access_token = '09jENteDSOLgDfu2rEoPaWHQRMfy7wmGCy0Y7TQk8K4dipgK8zHrM3EiQmLC5z7uFZ4Ajzc5BUftTqfQBrYGKYvUUo2M+UBM2VCnaxrVrdSUYkDGDLAxr+9v8ezFaZ4zbtkvbiG6hEs0W/we6FXqTwdB04t89/1O/w1cDnyilFU='
secret = '8645aa92607c0344527de1406dc434bf'
line_bot_api = LineBotApi(access_token)              # 確認 token 是否正確
handler = WebhookHandler(secret)                     # 確認 secret 是否正確
k=[]
lineweb={}
#接收
@app.route("/", methods=['POST'])
def linebot():
    body = request.get_data(as_text=True)                    # 取得收到的訊息內容
    try:
        json_data = json.loads(body)                         # json 格式化訊息內容
        signature = request.headers['X-Line-Signature']      # 加入回傳的 headers
        handler.handle(body,signature)                      # 綁定訊息回傳的相關資訊
        tk = json_data['events'][0]['replyToken']            # 取得回傳訊息的 Token
        type = json_data['events'][0]['message']['type']     # 取得 LINe 收到的訊息類型
        if type=='text':
            msg = json_data['events'][0]['message']['text']  # 取得 LINE 收到的文字訊息
            print(msg)                                       # 印出內容
            reply = msg
        else:
            reply = '你傳的不是文字呦～'
        print(reply)
        line_bot_api.reply_message(tk,TextSendMessage(reply))# 回傳訊息
        headers = {'Authorization':'Bearer 09jENteDSOLgDfu2rEoPaWHQRMfy7wmGCy0Y7TQk8K4dipgK8zHrM3EiQmLC5z7uFZ4Ajzc5BUftTqfQBrYGKYvUUo2M+UBM2VCnaxrVrdSUYkDGDLAxr+9v8ezFaZ4zbtkvbiG6hEs0W/we6FXqTwdB04t89/1O/w1cDnyilFU','Content-Type':'application/json'}
        boday = {
            'to':json_data['events'][0]['source']['userId'],
            'messages':[{
                    'type': 'text',
                    'text': 'abac'
            }]
        }
        req = requests.request('POST', 'https://api.line.me/v2/bot/message/push', headers=headers,data=json.dumps(boday).encode('utf-8'))
    except:
        print(body)                                          # 如果發生錯誤，印出收到的內容
    return 'OK'                                              # 驗證 Webhook 使用，不能省略

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    input_text = event.message.text
    if input_text== '驗證碼':
          key=generate_token()
          k.append(key)
          lineweb[key]=event.source.user_id
          data={'token':key}
          req=requests.post('https://line-web-app.vercel.app/d.py/sd',json=data)
          line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=key))
             
    elif input_text == '1':
        bm=TemplateSendMessage(
            alt_text='777',
            template=ButtonsTemplate(
                thumbnail_image_url='https://img95.699pic.com/photo/40250/3647.jpg_wh300.jpg',
                title='歡迎使用此服務!',
                text='007',
                actions=[
                    MessageAction(
                        label='驗證碼',
                        text='驗證碼'
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token,bm)
def generate_token():
    # 生成一个随机token，可以根据需要指定token长度
    random_token = secrets.token_hex(3)
    return random_token  
@app.route('/bot',methods=['POST'])
def ait():
    da=request.json
    if da in k:
        headers = {'Authorization':'Bearer 09jENteDSOLgDfu2rEoPaWHQRMfy7wmGCy0Y7TQk8K4dipgK8zHrM3EiQmLC5z7uFZ4Ajzc5BUftTqfQBrYGKYvUUo2M+UBM2VCnaxrVrdSUYkDGDLAxr+9v8ezFaZ4zbtkvbiG6hEs0W/we6FXqTwdB04t89/1O/w1cDnyilFU','Content-Type':'application/json'}
        boday = {
            'to':lineweb[da],
            'messages':[{
                    'type': 'text',
                    'text': '已完成'
            }]
        }
        req = requests.request('POST', 'https://api.line.me/v2/bot/message/push', headers=headers,data=json.dumps(boday).encode('utf-8'))
