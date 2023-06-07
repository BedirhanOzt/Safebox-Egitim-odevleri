from flask import Flask,render_template,request,redirect
import pymongo

app=Flask(__name__)

connection = pymongo.MongoClient("mongodb://localhost:27017/")
db=connection['odev']
UsersCollection=db['Users']

#Kullanıcı ekleme
@app.route('/add',methods=['POST'])
def add():
    name=request.form['name']
    age=request.form['age']
    job=request.form['job']
    user={
        "name":name,
        "age":age,
        "job":job
    }
    UsersCollection.insert_one(user)

    return {'message':"Başarılı bir şekilde kullanıcı eklenmiştir"}

#Yaşı 25 den büyükleri olanları döndürme
@app.route('/25', methods=['GET'])
def get_users_over_25():
    filtered_users = list(filter(lambda user: user['age'] > 25, users))
    return jsonify(filtered_users)


#Verdiğimiz id'ye göre kullanıcıyı silme
@app.route('/deleteuser', methods=['DELETE'])
def delete_user():
    data = request.get_json()
    user_id = data.get('id')

    for user in users:
        if user['id'] == user_id:
            users.remove(user)


if __name__=='__main__':

    app.run(host='0.0.0.0',port=5000,debug=True)