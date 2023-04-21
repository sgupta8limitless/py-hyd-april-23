import traceback
print("before")



try:
    num=int(input("Enter Number: "))
    print(num)
except NameError:
    print("Your are using a variable that is not defined")
except ValueError:
    # traceback.print_exc()
    print("Integer was expected you gave string")
except:
    print("Something happened")
else:
    print()
finally:


print("after")


