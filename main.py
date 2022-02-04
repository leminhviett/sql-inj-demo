from UserModel import UserModel
from flask import Flask, request, session
from flask_cors import CORS

app = Flask(__name__, static_url_path='', static_folder='../storage')
app.config["SECRET_KEY"] = "1234"
CORS(app)

@app.route('/auth')
def auth():
    userModel = UserModel()

    username, pw = request.headers.get('username'), request.headers.get('pw')
    print( {"un" : username, "pw" : pw})
    try:
        res = userModel.getUser(username, pw)
        print(res)
    except Exception as e:
        return {"error" : str(e)}
    
    userModel.close()
    return {"info" : res}

@app.route('/')
def test():
    return "Hello"

if __name__== "__main__":
    userModel = UserModel()
    userModel.addUser("viet009", "1234", 7000)
    userModel.addUser("viet010", "1235", 2000)
    userModel.addUser("viet020", "1236", 5500)
    userModel.close()

    app.run(port=8000, debug=True, host="0.0.0.0")
