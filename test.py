import json

from flask import request

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/processUserInfo/<string:userInfo>',methods = ['POST'])
def processUserInfo(userInfo):
    userInfo = json.loads(userInfo)
    print()
    print('USER LOADED')
    print('-----------')
    print(f"UserName: {userInfo['name']}")
    print(f"UserName: {userInfo['type']}")
    print()
    return userInfo
    
if __name__ =="__main__":
    app.run(debug = True)

