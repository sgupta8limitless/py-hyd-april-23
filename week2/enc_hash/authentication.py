import mysql.connector
import hashlib

conn=mysql.connector.connect(
    host="localhost",
    port="3307",
    user="root", 
    password="thorabh8" ,
    database="auth"
    )

cursor=conn.cursor()



def registerUser():
    name=input("Enter Name: ")
    username=input("Enter Username: ")
    password=hashlib.sha1(input("Enter Password: ").encode()).hexdigest()

    query="insert into user(name,username,password) values(%s,%s,%s)"
    values=(name,username,password)




    cursor.execute(query,values)
    conn.commit()


def loginUser():
    username=input("Enter Username: ")
    password=hashlib.sha1(input("Enter Password: ").encode()).hexdigest()

    query="select * from user where username=%s and password=%s"
    values=(username,password)

    cursor.execute(query,values)

    user=cursor.fetchone()

    if(user==None):
        print("Wrong username or password")
    else:
        print("Welcome")




loginUser()
# registerUser()

    


# t1="something"

# print(hashlib.sha1(t1.encode()).hexdigest())



