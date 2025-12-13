import json
import boto3
import mysql.connector
from botocore.exceptions import ClientError

def get_db_credentials():
    secret_name = "flaskapp/db/credentials"

    client = boto3.client("secretsmanager")

    try:
        response = client.get_secret_value(SecretId=secret_name)
    except ClientError as e:
        raise RuntimeError("Unable to fetch DB secret") from e

    return json.loads(response["SecretString"])

secret = get_db_credentials()

mydb = mysql.connector.connect(
    host="flaskapp-mydb-jgnwcizrvrqa.cruqqgmqsn5d.ap-south-1.rds.amazonaws.com",      
    user=secret["username"],
    password=secret["password"],
    database=secret["dbname"]
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
