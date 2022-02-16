wt1 = 3
wt2 = 2
wt3 = 7
wt4 = 8
wt5 = 4
wt6 = 5
wt7 = 6
wt8 = 7
wt9 = 8
wt10 = 9


ap1 = [3,6,8]
ap2 = [2,5]
ap3 = [1,9]
ap4 = [4,10]
accessPoints = 4
#Create an array of size 4 and store the sum of wts in it
totalExecTime = []
devicesCount = 10
for i in range(accessPoints):
    totalExecTime.append(0)
for device in range(devicesCount):
    devName = "wt"+str(device+1)
    #print(locals()[devName])
    print(devName)
    totalExecTime[device] = totalExecTime[device]+globals()[devName] #Add the value of time_required
print(totalExecTime)
print(sum(totalExecTime))