# assignment 1 
# finding elements in list 

# planets=["Mercury","Venus","Earth","Mars","Earth","Jupiter"]
# planet_in=input("Enter a planet Name: ")
# ind=[]

# for i in range(len(planets)):

#     if(planet_in==planets[i]):
#         ind.append(i)

# if(len(ind)==0):
#     print("The element was not found")
# else:
#     print("it was found on these ",ind)

# dictionaries 

# ["a","b","c"]

# ele={
#     "name":"Saurabh",
#     "age":26,
#    "hobbies":["Cricket","Volleyball","Singing"],
#     "address":{
#          "city":"Mumbai",
#          "state":"Maharashtra",
#          "pincode":49067
#     }
# }

# print(ele['address']['city'])

# adding element 
# ele['planet']="Earth"
# ele.update({"planet":"Earth"})


# ele.popitem()

# print(ele)


# print(ele.values())

# accessing element 
# print(ele['city'])
# print(ele.get("age"))

# print(ele['hobbies'])

# for i in ele['hobbies']:
#     print(i)

# for i in ele:
#     print(ele.get(i))


# assignment 2 
# menu driven list crud 

# names=[]


# while True:
#     print("1. Add")
#     print("2. View")
#     print("3. Delete")
#     print("4. Update")
#     print("5. Exit")
#     choice=int(input("Choose an option: "))
#     if choice==1:
#         name=input("Enter new name: ")
#         if name in names:
#             print("Already exist")
#         else:
#             names.append(name)
#     elif choice==2:
#         print(names)
#     elif choice==5:
#         break



# tuples 

# tp1=(23,45,67,78,45)
# tp2=(34,56)

# tp3=tp1+tp2

# print(tp3)

# print(list(tp1))

# print(tp1.index(45))


# print(tp[3])

# for i in tp:
#     print(i)

# print(tp.count(45))


# array / list of dictionaries 

# students=[
#     {
#         "name":"Lokesh",
#         "age":22
#     },
#     {
#         "name":"Loki",
#         "age":1200
#     },
#     {
#         "name":"Saurabh",
#         "age":78
#     }
# ]

# for data in students:
#     print(data['name'])



# sqr=lambda num1,num2 : num1*num2

# print(sqr(3,6))

# map 
# filter
# reduce

# def mtwo(n):
#     return n['age']*2

# users=[
#     {"name":"Saurabh","age":26},
#     {"name":"Lokesh","age":99},
#     {"name":"Shreya","age":26},
#     {"name":"Prabhu","age":21},
#     {"name":"Moumita","age":26}
#     ]

# def filterUsers(u):
#     return u['age']==26
        

# filter 

# newusers=filter(filterUsers,users)

# for i in newusers:
#     print(i)

# newusers=[]

# for u in users:
#     if u['age']==26:
#         newusers.append(u)

# newlist=map(lambda n: n['age']*2,users)

# for e in newlist:
#     print(e)




# reduce 

from functools import reduce

def some(e1,e2):
    return e1+e2

ans=reduce(lambda e1,e2:e1+e2,[2,5,6,7,9])

print(ans)


from mod import doSomething

doSomething()














