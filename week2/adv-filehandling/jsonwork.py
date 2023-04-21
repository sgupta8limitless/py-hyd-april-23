import json 

# with open("superheroes.json","r") as fr:
#     data=json.load(fr)

#     print(data[0])


# a="""

#     [
#         {
#             "name":"Saurabh",
#             "age":22
#         },
#         {
#             "name":"Lokesh",
#             "age":768
#         }
#     ]


# """

# print(json.loads(a))


data=[
    {
        "country":"India",
        "capital":"New Delhi",
        "pop":22
    },
    {
        "country":"Australia",
        "capital":"Canberra",
        "pop":1
    }
]


with open("dummy.json","w") as fw:
    json.dump(data,fw)


