import pymongo

connection = pymongo.MongoClient("mongodb://localhost:27017/")
db=connection['odev']
UsersCollection=db['Users']

users= [
    {"name":"John","age":30,"job":"kaldırım mühendisi","Description ": 1},
    {"name":"Can","age":34,"job":"pc mühendisi","Description ": 1},
    {"name":"Oguzhan","age":23,"job":"kale mühendisi","Description ": 1},
    {"name":"Cemal","age":25,"job":"hidrolik mühendisi","Description ": 1},
    {"name":"Elif","age":29,"job":"işletme mühendisi","Description ": 1},
    {"name":"Gülşen","age":33,"job":"istatistik mühendisi","Description ": 1 },
    {"name":"Hakan","age":35,"job":"ekonomi mühendisi","Description ": 1},
    {"name":"İlker","age":37,"job":"sosyal medya mühendisi","Description ": 1},
    {"name":"Bilal","age":43,"job":"meteoroloji mühendisi","Description ": 1},
    {"name":"Derya","age":27,"job":"pazarlama mühendisi","Description ": 1},
    {"name":"Kaan","age":39,"job":"yazılım mühendisi","Description ": 1},
    {"name":"Leman","age":41,"job":"veri mühendisi","Description ": 1},
    {"name":"Mert","age":43,"job":"robotik mühendisi","Description ": 1},
    {"name":"Nihal","age":45,"job":"yapay zeka mühendisi","Description ": 1},
    {"name":"Orhan","age":47,"job":"siber güvenlik mühendisi","Description ": 1},
    {"name":"Pınar","age":49,"job":"bilgi işlem mühendisi","Description ": 1},
    {"name":"Rabia","age":23,"job":"ağ mühendisi","Description ": 1},
    {"name":"Sait","age":25,"job":"donanım mühendisi","Description ": 1},
    {"name":"Tahir","age":27,"job":"sistem mühendisi","Description ": 1},
    {"name":"Ulaş","age":29,"job":"uygulama mühendisi","Description ": 1},
    {"name":"Vedat","age":31,"job":"mobil mühendisi","Description ": 1},
    {"name":"Yakup","age":33,"job":"web mühendisi","Description ": 1},
    {"name":"Zehra","age":35,"job":"oyun mühendisi","Description ": 1},
    {"name":"Adnan","age":37,"job":"grafik mühendisi","Description ": 1},
    {"name":"Berk","age":39,"job":"arayüz mühendisi","Description ": 1},
    {"name":"Ceren","age":41,"job":"kullanıcı deneyimi mühendisi","Description ": 1},
    {"name":"Deniz","age":43,"job":"veritabanı mühendisi","Description ": 1},
    {"name":"Emrah","age":45,"job":"bulut mühendisi","Description ": 1},
    {"name":"Fikret","age":47,"job":"yazılım test mühendisi","Description ": 1},
    {"name":"Gizem","age":49,"job":"sistem analisti","Description ": 1},
    {"name":"Halil","age":23,"job":"veri analisti","Description ": 1},
    {"name":"İpek","age":25,"job":"veri bilimci","Description ": 1},
    {"name":"Kadir","age":27,"job":"yapay öğrenme mühendisi","Description ": 1},
    {"name":"Lale","age":29,"job":"derin öğrenme mühendisi","Description ": 1},
    {"name":"Musa","age":31,"job":"makine öğrenmesi mühendisi","Description ": 1},
    {"name":"Nur","age":33,"job":"doğal dil işleme mühendisi","Description ": 1},
    {"name":"Orkun","age":35,"job":"görüntü işleme mühendisi","Description ": 1},
    {"name":"Pınar","age":37,"job":"konuşma işleme mühendisi","Description ": 1},
    {"name":"Rengin","age":39,"job":"robotik öğrenme mühendisi","Description ": 1},
    {"name":"Selin","age":41,"job":"tavsiye sistemleri mühendisi","Description ": 1},
    {"name":"Taylan","age":43,"job":"veri madenciliği mühendisi","Description ": 1},
    {"name":"Utku","age":45,"job":"veri görselleştirme mühendisi","Description ": 1},
    {"name":"Vedat","age":47,"job":"veri yönetimi mühendisi","Description ": 1},
    {"name":"Yasemin","age":49,"job":"veri güvenliği mühendisi","Description ": 1},
    {"name":"Zafer","age":23,"job":"veri depolama mühendisi","Description ": 1},
    {"name":"Adem","age":25,"job":"veri entegrasyonu mühendisi","Description ": 1},
    {"name":"Berk","age":27,"job":"veri kalitesi mühendisi","Description ": 1},
    {"name":"Ceren","age":29,"job":"veri modelleme mühendisi","Description ": 1},
    {"name":"Deniz","age":31,"job":"veri iş zekası mühendisi","Description ": 1},
    {"name":"Emrah","age":33,"job":"veri analitiği mühendisi","Description ": 1},
    {"name":"Fikret","age":35,"job":"veri yönetişimi mühendisi","Description ": 1},
    {"name":"Gizem","age":37,"job":"veri mimarisi mühendisi","Description ": 1},

]