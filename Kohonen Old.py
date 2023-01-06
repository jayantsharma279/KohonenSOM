import numpy as np 
    
alpha=0.6 #learning rate


x1= np.array([1,1,0,0])
x2= np.array([0,0,0,1])
x3= np.array([1,0,0,0])
x4= np.array([0,0,1,1])

y1= np.array([0.2,0.6,0.5,0.9])
y2= np.array([0.8,0.4,0.7,0.3])

def Distance(x,y):  #Calculates the distance between the arrays input in arguments x,y
    sum=0
    for i in range(len(x1)):
        sum=sum+np.square(y[i]-x[i])
    return(sum)



def Learning_Algorithm(x1,x2,x3,x4,y1,y2):


    arr=[]                             #Stores the distances calculated in each iteration
    for x in [x1,x2,x3,x4]:
        for y in [y1,y2]:
            
            arr.insert(0,Distance(x,y))
            
            if len(arr)%2==0:              #Enters loop only when both the distances are comparable
                if arr[0]<arr[1]:
                    for s in range(len(y2)):             #Weights of y2 get updated
                        wnew=y2[s]+alpha*(x[s]-y2[s])
                        y2[s]=wnew
                elif arr[1]<arr[0]:                       #Weights of y1 get updated
                    for s in range(len(y2)):
                        wnew=y1[s]+alpha*(x[s]-y1[s])
                        y1[s]=wnew 
            else:
                continue
    print(y1)                      #Final Y1 weights
    print(y2)                      #Final Y2 weights



epoch=1000
 
for number in range(int(epoch)):
    if number!=epoch:
        print("Number of iterations:",number+1),Learning_Algorithm(x1,x2,x3,x4,y1,y2)
        alpha=alpha*0.5
    else:
        break  
