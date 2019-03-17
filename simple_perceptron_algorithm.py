''' This is the implementation of simple perceptron algorithm
credits:smm

'''



import numpy as np
import matplotlib.pyplot as plt


#paste your data below
rows = [[]]

x = []
y = []


for row in rows:
    
    x.append(row[0])
    y.append(row[1])


    


for i in range(0,len(rows)):
    if (int(rows[i][2])==1):
        plt.scatter(x[i],y[i],color = "blue")
    else:
        plt.scatter(x[i],y[i],color = "red")






W = np.random.rand(1,2)
bias = 0.1
print(W)
print(1)
print("after applying perceptron algorithm")

learning_rate = 0.001

no_of_cycles = 100

def step_function(inp):
    if inp>0:
        return 1
    return 0


for i in range(0,no_of_cycles):
    
    for row in rows:
        #print("row in rows ran")
        y = row[2]
        y_hat = np.matmul(W,np.array([row[0],row[1]]).T)[0]+bias
        
        value = step_function(y_hat) - y
			
        if value ==1:
            
            for i in range(0,2):
                W[0][i]-=row[i]*learning_rate
                

            bias-=learning_rate


        elif value == -1:
            
            for i in range(0,2):
                W[0][i]+=row[i]*learning_rate
                
            bias+=learning_rate




print(W)
print(bias)




x_1 = np.array(range(2))

abc = -bias-W[0][0]*x_1

y = abc/W[0][1]

# Create the plot
plt.plot(x_1,y)




plt.show()


