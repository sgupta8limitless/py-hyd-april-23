class Demo:

    i=1

    def printDetails(self):
        print(Demo.i)



d=Demo()
d.printDetails()
Demo.i=5

d1=Demo()
d1.printDetails()