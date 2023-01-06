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


epoch=100
y1a_values=[]
y1b_values=[]
y1c_values=[]
y1d_values=[]

y2_values=[]
for number in range(int(epoch)):
    if number!=epoch:
        print("Number of iterations:",number+1),Learning_Algorithm(x1,x2,x3,x4,y1,y2)
        y1a_values.append(y1[0])
        y1b_values.append(y1[1])
        y1c_values.append(y1[2])
        y1d_values.append(y1[3])
        
        y2_values.append(y2[0])
        alpha=alpha*0.5
    else:
        break  

from matplotlib import pyplot as plt 
x=x = np.arange(0, 100)
Y1A=y1a_values
Y1B=y1b_values
Y1C=y1c_values
Y1D=y1d_values

Y2=y2_values

figure, axis = plt.subplots(1,1)

plt.plot(x,Y1A,'c',label="Y1 values")
plt.plot(x,Y1B,'c',label="Y1 values")
plt.plot(x,Y1C,'c',label="Y1 values")
plt.plot(x,Y1D,'c',label="Y1 values")


plt.title("Weight updation") # title on top
plt.ylabel("Weights") # for yaxis
plt.xlabel("Number of epochs") # for x axis

figure, axis = plt.subplots(1,1)

plt.plot(x,Y2,'g',label='Y2 values')
plt.title("Weight updation") # title on top
plt.ylabel("Weights") # for yaxis
plt.xlabel("Number of epochs") # for x axis

plt.show()


