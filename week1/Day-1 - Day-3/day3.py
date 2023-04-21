
# reading 
# f=open("dummy.txt","r")

# print(f.read())
# print(f.readline())
# print(f.readline())
# print(f.read(5))
# f.seek(0)
# print(f.read())
# print(f.readlines())

# f.close()

# writing 

# fw=open("data.txt","w")

# # fw.write("loki\nthanos")

# fw.writelines(["Hi line 1\n","hello line 2"])

# fw.close()

# fa=open("data.txt","a")
# fa.write("\n something new")
# fa.close()



# with open("dummy.txt","r") as f:
#     print(f.read())
#     f.close()

# with open("n.py","w") as f:
    
#     f.write("print('hello')")
#     f.close()



# import pickle
# import os





# if os.path.isfile('data.dat')==False:
#     fwb=open("data.dat","wb")
#     pickle.dump([],fwb)
#     fwb.close()


# frb=open("data.dat","rb")
# users=pickle.load(frb)
# print(users,"before new insert")
# frb.close()

# u={}
# u['name']=input("Enter name ")
# u['username']=input("Enter username ")

# users.append(u)

# fwb=open("data.dat","wb")
# pickle.dump(users,fwb)
# fwb.close()






# fb=open("data.dat","rb")
# print(pickle.load(fb))
# fb.close()
# pickle.dump(users,fb)


# math functions 

import math

# print(min(34,56,78,12,67))
# print(max(34,56,78,12,67))
# print(abs(-34))

# print(round(2.9))

# print(math.sqrt(49))
# print(math.ceil(1.1))
# print(math.floor(1.9))

# print(math.sin(90))

# print(math.pi)

# print(math.cbrt(8))

# print(pow(2,4))

# print(math.tan(90))

# print(math.degrees(6.5))



# for i in ml :
#     if i%2==0:
#         el.append(i)


a=1
b=1
c=2

ls=[[i,j,k] for i in range(a+1) for j in range(b+1) for k in range(c+1) if i+j+k!=2]


# for i in range(a+1):
#     for j in range(b+1):
#         ls.append([i,j])



# print(ls)


def rotateList(ls,r):
    l=len(ls)

    if r>l:
        r=r%l

    ls1=ls[l-r:]
    ls2=ls[:l-r]
    rl=ls1+ls2
    return rl




# rotateList(,2)

lis=input("Enter list elements in spaces: ")
print(lis.split(" "))


# n="Hello.hi.bye.h"

# print(n.split("."))
















