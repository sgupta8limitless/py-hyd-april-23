import mysql.connector.errors as err
from handlers import printSQLException
from Connection import Connection

class EmployeeGateway:
    def __init__(self):
        connection=Connection()
        self.__conn=connection.getConnection()
        self.__cursor=self.__conn.cursor()

    def create(self,name,salary,did):
        query="insert into employees(name,salary,did) values(%s,%s,%s)"
        values=(name,salary,did)
        try:
            self.__cursor.execute(query,values)
            self.__conn.commit()
            return True
        except err.Error as e:
            printSQLException(e)
        return False
    
    def checkIfEmpExist(self,id):
        query="select * from employees where id=%s"
        value=(id,)

        self.__cursor.execute(query,value)
        employee=self.__cursor.fetchone()

        if(employee!=None):
            return True
        
        return False


    def delete(self,id):

        if self.checkIfEmpExist(id)==True:

            query="delete from employees where id=%s"
            values=(id,)
            self.__cursor.execute(query,values)
            self.__conn.commit()
            return True
        
        return False
      


    def update(self,column,newval,id):
        query="update employees set "+column+"= %s where id = %s"
        values=(newval,id)
        self.__cursor.execute(query,values)
        self.__conn.commit()

    def index(self):
        query="select * from employees"
        self.__cursor.execute(query)
        employees=self.__cursor.fetchall()
        return employees


