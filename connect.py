import mysql.connector
import os
DB_HOST = os.environ.get("DB_HOST")
DB_USER = os.environ.get("DB_USER")
DB_PASSWORD = os.environ.get("DB_PASSWORD")
DB_NAME = os.environ.get("DB_NAME")

# Create a global DB connection
mydb = mysql.connector.connect(
    host=DB_HOST,
    user=DB_USER,
    password=DB_PASSWORD,
    database=DB_NAME
)
mycursor = mydb.cursor()

def addition(name,price):
  sql="INSERT INTO conversion (input,output) values (%s, %s)"
  val=(name,price)
  mycursor.execute(sql,val)
  mydb.commit()
  mycursor.execute("SELECT * FROM conversion")
  return mycursor

def delete(n):
  sql="DELETE FROM conversion WHERE id=%s"
  mycursor.execute(sql,(n,))
  mydb.commit()
  mycursor.execute("SELECT * FROM conversion")
  return mycursor


# def addition(name,price):
#   sql="INSERT INTO Products (name,price) values (%s, %s)"
#   val=(name,price)
#   mycursor.execute(sql,val)
#   mydb.commit()
#   mycursor.execute("SELECT * FROM Products")
#   for i in mycursor:
#    print(i)

# sql="INSERT INTO emp values (%s, %s, %s)"
# val=(6,"new",4)
# mycursor.execute(sql,val)
# mydb.commit()
# addition("car",45)

# mycursor.execute("SELECT * FROM Products")

# mycursor.execute("create table conversion (id int NOT NULL AUTO_INCREMENT PRIMARY KEY, input int, output varchar(255))")
# result=mycursor.fetchall()


# for result in result:
#  print(f"ID:{result[0]} Name: {result[1]} price: {result[2]}" )
