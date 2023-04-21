import requests

def getUsers():

    response=requests.get("https://jsonplaceholder.typicode.com/users")
    # print(response.json())
    print(response.status_code)
    print(response.headers)

def getUser():
    response=requests.get("https://jsonplaceholder.typicode.com/users/1")
    print(response.json())

def createUser():
    user={"name":"Thor","email":"skjjfhsjkfhsk"}
    response=requests.post(
        "https://jsonplaceholder.typicode.com/users",
        json=user,
       )
    
    
    print(response.json())
    print(response.status_code)

def deleteUser():
    response=requests.delete("https://jsonplaceholder.typicode.com/users/1")
    print(response.json())


def updateUser():
    upuser={"name":"Lokesh"}
    response=requests.patch("https://jsonplaceholder.typicode.com/users/1",json=upuser)
    print(response.json())


def getWeather():
    city=input("Enter City: ")
    response=requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=36559a71711c2de96006b82e149d99a1")
    data=response.json()

    print(str(float(data['main']['temp'])-273.15)+"deg Celcius")



getWeather()