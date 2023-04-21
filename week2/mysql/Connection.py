import mysql.connector

class Connection:
    def __init__(self):
        self.__conn=mysql.connector.connect(
            host="localhost",
            port="3307",
            user="root",
            password="thorabh8",
            database="empmgmt"
            )
        
    def getConnection(self):
        return self.__conn
        