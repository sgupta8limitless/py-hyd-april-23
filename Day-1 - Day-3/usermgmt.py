# add user function 
def addUser():
    user={}

    user['id']=int(input("Enter ID: "))
    user['name']=input("Enter Name: ")
    user['username']=input("Enter Username: ")
    user['password']=input("Enter Password: ")
    user['age']=int(input("Enter Age: "))

    adress={}
    adress['city']=input("Enter City: ")
    adress['country']=input("Enter Country: ")
    adress['pincode']=input("Enter Pincode: ")

    user['adress']=adress
    

    return user

# view user function 

def viewUser(displaylist):
     print("Name\tAge\tUsername\tCity\tCountry\tPincode")

     for user in displaylist:
          print(user['name']+"\t"+str(user["age"])+"\t"+user['username']+"\t"+user['adress']['city']+"\t"+user['adress']['country']+"\t"+user['adress']['pincode'])

     
def deleteUser():
     id=int(input("Enter user id: "))
     
     for i in range(len(users)):
          if(users[i]['id']==id):
               users.pop(i)
               break
          
def updateUser():
     id=int(input("Enter user id: "))
     key=input("Enter the property: ")
     value=input("Enter the new value: ")

     for user in users:
          if user['id']==id:
               user[key]=value
               break
          
def sortList():
     sortedUsers=sorted(users,key=lambda u:u["age"])
     viewUser(sortedUsers)



def filterOpsBase(key,value):
     fusers=filter(lambda u:u[key]==value,users)
     viewUser(fusers)

def filterOpsAddress(key,value):
     fusers=filter(lambda u:u['adress'][key]==value,users)
     viewUser(fusers)


    
users=[
     {'id': 1, 'name': 'Saurabh', 'username': 'sgupta', 'password': 'fg123', 'age': 24, 'adress': {'city': 'Mumbai', 'country': 'India', 'pincode': '345'}},
     {'id': 2, 'name': 'Lokesh', 'username': 'loki', 'password': '1234', 'age': 45, 'adress': {'city': 'Islamabad', 'country': 'Pakistan', 'pincode': '34'}},
     {'id': 3, 'name': 'Prabhu', 'username': 'prab', 'password': 'rg43', 'age': 24, 'adress': {'city': 'California', 'country': 'USA', 'pincode': '678'}},
     {'id': 4, 'name': 'Sarfaraz', 'username': 'dhoka', 'password': 'ght', 'age': 21, 'adress': {'city': 'Mumbai', 'country': 'India', 'pincode': '789'}}
]


while True :
     print("1. Add")
     print("2. View")
     print("3. Delete")
     print("4. Update")
     print("5. Sort")
     print("6. Filter")
     print("0. Exit")
     choice=int(input("Choose an option: "))

     if choice==1:
          u=addUser()
          users.append(u)
     elif choice==2:
         viewUser(users)
     elif choice==3:
          deleteUser()
     elif choice==4:
          updateUser()
     elif choice==5:
          sortList()
     elif choice==6:
          print("1.Filter on Age")
          print("2.Filter on City")
          print("3.Filter on Country")
          fchoice=int(input("Select The filter: "))
          if fchoice==1:
               age=int(input("Enter Age: "))
               filterOpsBase("age",age)
          elif fchoice==2:
               city=input("Enter City: ")
               filterOpsAddress("city",city)
          elif fchoice==3:
               country=input("Enter Country: ")
               filterOpsAddress("country",country)
     elif choice==0:
          break

    