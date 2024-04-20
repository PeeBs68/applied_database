import mysql.connector
from config import config as cfg

db = mysql.connector.connect(
    host=cfg["host"],
    user = cfg["user"],
    password = cfg["password"],
    database = cfg["database"]
)
print("Connected")

cursor = db.cursor()

sql = "select * from student here id = %s"
values = (1,)

cursor.execute(sql, values)
result = cursor.fetchall()
for x in result:
    print(x)

cursor.close()
db.close()

print("Connection Closed")