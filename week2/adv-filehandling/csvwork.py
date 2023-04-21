import csv

# f=open("organisation.csv","r")

# csvr=csv.reader(f)



# headers=next(csvr)

# row1=next(csvr)

# print(row1)

# for row in csvr:
#     print(row)


headers=["Name","Age","City"]


data=[]

data.append(input("Enter Name: "))
data.append(int(input("Enter Age: ")))
data.append(input("Enter city: "))


with open("demo.csv","r+") as fw:

    content=fw.read()
    csvw=csv.writer(fw)

    if(len(content)==0):
        csvw.writerow(headers)

    csvw.writerow(data)

    fw.close()