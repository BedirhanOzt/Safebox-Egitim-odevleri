#Tüm verileri getiren sorgu
UsersCollection.insert_many(users)

#Bir tane şeç
for i in users:
   UsersCollection.insert_one(i)

#Fikret ismini değiştir.Güncelle
query={"name":"Fikret"}
new_values={"$set":{"name":"Fikoo"}}
update_Fikret= UsersCollection.update_one(query,new_values)


#20 yaşından büyükleri getiren sorgu
query = {"age": {"$gt": 20}}
users = UsersCollection.find(query)
for user in users:
    print(user)



#Yaşı 25'den fazla olanların description'ı 0 olan sorgu
query = {"age": {"$gt": 25}}  
update = {"$set": {"description": 0}}  

UsersCollection.update_many(query, update)



#Yaşı 45-48 yaş aralığında olan kişileri silen sorgu
query= {"age":{"$gte":45 , "$lte":48}}
remove_data= UsersCollection.delete_many(query)

