from os import access


accessPoints = 3
dev1 = 3
dev2 = 2
dev3 = 1
dev4 = 2
dev5 = 1
dev6 = 1
devicesCount = 6        
connections = []
print("1")
for i in range(accessPoints):
    connections.append(0)
for device in range(devicesCount):
    devName = "dev"+str(device+1)
    #print(locals()[devName])
    connections[locals()[devName]-1] = connections[locals()[devName]-1]+1
print(connections)

sum = 0
squareSum = 0
for i in range(accessPoints):
    sum+=connections[i]
    squareSum += connections[i]*connections[i]
print(abs(1-sum/(accessPoints*squareSum)**0.5))