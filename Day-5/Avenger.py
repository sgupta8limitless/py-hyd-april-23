class Avenger:
    def __init__(self,id,name,strength,speed,planet):
        self.__id=id
        self.__name=name 
        self.__strength=strength
        self.__speed=speed 
        self.__planet=planet

    def getId(self):
        return self.__id
    
    def getStrength(self):
        return self.__strength

    def printDetails(self):
        print(str(self.__id)+"\t"+self.__name+"\t"+str(self.__strength)+"\t"+str(self.__speed)+"\t"+self.__planet)


class AvengersCRUD:
    def __init__(self):
        self.avengers=[]

    def createAvenger(self):
        name=input("Enter Avenger Name: ")
        strength=int(input("Enter Avenger Strength: "))
        speed=int(input("Enter Avenger Spped: "))
        planet=input("Enter Avenger Planet: ")
        a=Avenger(name,strength,speed,planet)
        self.avengers.append(a)
        

    def displayAvengers(self):
        for avenger in self.avengers:
            avenger.printDetails()

    def deleteAvenger(self):
        id=int(input("Enter id to delete "))
        for index in range(len(self.avengers)):
            if(self.avengers[index].getId()==id):
                self.avengers.pop(index)
                break

    def sortAvengers(self):
        self.avengers.sort(key=lambda x:x.getStrength())
        self.displayAvengers()

        



    




ac=AvengersCRUD()


while True:
    print("1.Add ")
    print("2.View ")
    print("3.Update ")
    print("4.Delete ")
    print("5.Sort ")
    print("0.Exit ")
    choice=int(input("Select an option "))
    if choice==1:
        ac.createAvenger()
    elif choice==2:
        ac.displayAvengers()
    elif choice==4:
        pass





















