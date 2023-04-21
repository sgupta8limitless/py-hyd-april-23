from flask import Flask,jsonify,request
import mysql.connector
import json


conn=mysql.connector.connect(host="localhost",port="3307",user="root",password="thorabh8",database="apitest")
cursor=conn.cursor(dictionary=True)


app = Flask(__name__)

# creation of product 
@app.route("/",methods=["POST"])
def create():
    product=json.loads(request.data)
    query="insert into products(name,price,category,quantity) values(%s,%s,%s,%s)"
    values=(product['name'],product['price'],product['category'],product['quantity'])
    try:
        cursor.execute(query,values)
        conn.commit()
        return jsonify({"message":"Product Inserted"}),201
    except Exception as e:
        print(e)
    
    return jsonify({"message":"Some problem while creating the product"}),409

# to delete 
@app.route("/<int:id>",methods=["DELETE"])
def delete(id):
    query="delete from products where id = %s"
    values=(id,)
    try:
        cursor.execute(query,values)
        conn.commit()
        return jsonify({"message":"Product Deleted"}),202
    except Exception as e:
        print(e)
    
    return jsonify({"message":"Some problem while deleting the product"}),409

# to update 
@app.route("/<int:id>",methods=['PUT'])
def update(id):
    product=json.loads(request.data)
    query="update products set name=%s,price=%s,category=%s,quantity=%s where id = %s"
    values=(product['name'],product['price'],product['category'],product['quantity'],id)
    try:
        cursor.execute(query,values)
        conn.commit()
        return jsonify({"message":"Product Updated"})
    except Exception as e:
        print(e)
    
    return jsonify({"message":"Some problem while update the product"}),400


@app.route("/")
def products():
    query="select * from products"
    cursor.execute(query)
    products=cursor.fetchall()
    return jsonify(products)

@app.route("/<int:id>")
def product(id):
    query="select * from products where id=%s"
    values=(id,)
    cursor.execute(query,values)
    product=cursor.fetchone()
    return jsonify(product)


@app.route("/name/<string:name>")
def nameProduct(name):
    query="select * from products where name = %s"
    values=(name,)
    cursor.execute(query,values)
    products=cursor.fetchall()
    return jsonify(products)


@app.route("/category/<string:category>")
def catProduct(category):
    query="select * from products where category = %s"
    values=(category,)
    cursor.execute(query,values)
    products=cursor.fetchall()
    return jsonify(products)
    


    




    






# app.run(debug=True)

if __name__== '__main__':
    app.run(
        host="127.0.0.1",
        port="8000",
        debug=True
    )