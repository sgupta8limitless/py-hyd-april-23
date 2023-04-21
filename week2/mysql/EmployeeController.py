import re
from EmployeeGateway import EmployeeGateway

class EmployeeController:

    def __init__(self) :
        self.__employeeGateway=EmployeeGateway()
        

    def createEmployee(self):
        name=input("Enter Name: ")
        salary=input("Enter Salary: ")
        did=int(input("Enter Depratment ID: "))

        vmsgs=[]

        if(re.match("([a-zA-Z]){2,}\s?(([a-zA-Z]){1,})?$",name)==None):
            vmsgs.append("Name Should no include number")

        if(re.match("[0-9]{2,}$",salary)==None):
            vmsgs.append("Salary Should be a number")


        if(len(vmsgs)==0):
            res=self.__employeeGateway.create(name,float(salary),did)
            if(res==True):
                print("Employee Created Successfully")
            else:
                print("There was some problem creating employee")
        else:
            for msg in vmsgs:
                print(msg)





    def deleteEmployee(self):
        id=int(input("Enter ID: "))
        self.__employeeGateway.delete(id)


    def updateEmployee(self):
        id=int(input("Enter ID: "))
        column=input("Enter Column to update: ")
        newval=input("Enter New Value: ")

        if(column=="salary"):
            newval=float(newval)

        self.__employeeGateway.update(column,newval,id)

    def viewEmpployees(self):
        employees=self.__employeeGateway.index()
        print(employees)


   



    
