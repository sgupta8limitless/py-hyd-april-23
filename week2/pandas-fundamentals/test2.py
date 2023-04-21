import nmap as np

start=20
end=99

ps=np.PortScanner()

result=ps.scan("127.0.0.1",arguments="-O")

print(result)

# for i in range(start,end+1):

#     result=ps.scan("127.0.0.1",str(i))

#     status=result["scan"]["127.0.0.1"]["tcp"][i]["state"]

#     print(f"The Port {i} is {status}")



# name="dfgfsd"

# print(f"The name is {name} ")