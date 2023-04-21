
class CollegePerson:
  def __init__(self,name,age):
    self.__name=name
    self.__age=age

  def printBasicDetails(self):
    print("Name: "+self.__name)
    print("Age: "+str(self.__age))



# student class  

class Student(CollegePerson):
   
   def __init__(self,name,age,marksl):
     super().__init__(name,age)
     self.__marksl=marksl

   
     
   def printDetails(self):
     self.printBasicDetails()
     print(self.__marksl)
   
   

   
      



# teacher class 

class Teacher(CollegePerson):
  def __init__(self,name,age,subt):
    super().__init__(name,age)
    self.__subt=subt

  def printDetails(self):
    self.printBasicDetails()
    print(self.__subt)



s=Student("Saurabh",26,[14,56,78,34,90])
t=Teacher("Lokesh",34,["EVS","Drawing","PT"])

s.printDetails()
t.printDetails()










        