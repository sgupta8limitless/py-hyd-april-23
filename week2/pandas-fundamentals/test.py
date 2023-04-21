import nmap  

starting = 70  
closing = 90  

targetHost = '127.0.0.1'  

portScanner = nmap.PortScanner()  
 
# for j in range(starting, closing + 1):  
    
resultant = portScanner.scan(targetHost, arguments="-O")  
print(resultant)
    # resultant = resultant['scan'][targetHost]['tcp'][j]['state']  
     
    # print(f'The port {j} number from the range is {resultant}.')  2