from pymongo import MongoClient
from flask import Flask, request


# 連線 sever
client = MongoClient(host='127.0.0.1', port=27017)
# 連接資料庫
db = client['mydb']
# 指定集合
collection = db['member']

app = Flask(__name__)

@app.route("/member-management/members", methods=['POST'])
def add_member():
    name = request.form.get("name")
    age = request.form.get("age")
    email = request.form.get("email")
    
    result = db.member.insert_one({'name': name, 'age': age, 'email': email})
    return str(result.inserted_id)

if __name__ == "__main__":
    app.run()