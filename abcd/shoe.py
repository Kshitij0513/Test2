ct = []
fine = []
result = []
temp=[]
fans = []
Output= []
#no. of test cases
m = 0
n = 0
x=0
nobjects = int(input("Enter total no. of shoes : "))
for i in range(nobjects) :
               m = int(input("Enter completion time: "))
               ct.append(m)
               n = int(input("Enter Fine: "))
               fine.append(n)
for i in ct :
               for j in fine :
                             #if(i==j) :
                                           x = i / j
                                           temp.append(x)
#print(temp)
if(nobjects==3) :
              x1 = temp[0]
              x2 = temp[4]
              x3 = temp[8]
elif(nobjects==4) :
              x1 = temp[0]
              x2 = temp[5]
              x3 = temp[10]
              x4 = temp[15]
elif(nobjects==5) :
              x1 = temp[0]
              x2 = temp[6]
              x3 = temp[12]
              x4 = temp[18]
              x5 = temp[24]

if(nobjects==3) :
             result.append(x1)
             result.append(x2)
             result.append(x3)
elif(nobjects==4) :
              result.append(x1)
              result.append(x2)
              result.append(x3)
              result.append(x4)
elif(nobjects==5) :
              result.append(x1)
              result.append(x2)
              result.append(x3)
              result.append(x4)
              result.append(x5)

print(result)

fans = result.copy()
fans.sort()
#print(fans)

for x in fans: 
    for y in result: 
        if x == y: 
            Output.append(result.index(y)+1)
print(Output) 
  




              
