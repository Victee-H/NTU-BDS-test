import numpy as np
import matplotlib.pyplot as plt

total_time = 100000
Y = np.zeros((total_time,4))
print(Y.shape)
# from 0 to 3 are the inital value of E S ES P
Y[0,0] = 1.0
Y[0,1] = 10.0
Y[0,2] = 0.0
Y[0,3] = 0.0

# Reaction rate constant
k1 = 100.0
k2 = 600.0
k3 = 150.0

# Time step for each RK, unit min
delta_t = 0.000005

# Intermediate derivatives, four rows, four K's, four columns with respect to E, S, ES, P
K = np.zeros((4,4))
Y_int = np.zeros((4,4))

current_time = 0

while current_time<total_time-1:


    #Calculate K[0,:]
    K[0,0] = -k1*Y[current_time,0]*Y[current_time,1] + (k2+k3)*Y[current_time,2]
    K[0,1] = -k1*Y[current_time,0]*Y[current_time,1] + k2*Y[current_time,2]
    K[0,2] = k1*Y[current_time,0]*Y[current_time,1] - (k2+k3)*Y[current_time,2]
    K[0,3] = k3*Y[current_time,2]
    # print(K[0,:])
    #Calculate the intermediate result Y[0,:]
    Y_int[0,:] = K[0,:] * 0.5 * delta_t + Y[current_time,:]

    # Calculate K[1,:]
    K[1, 0] = -k1 * Y_int[0,0]*Y_int[0,1] + (k2+k3)*Y_int[0,2]
    K[1, 1] = -k1 * Y_int[0,0]*Y_int[0,1] + k2*Y_int[0,2]
    K[1, 2] = k1 * Y_int[0,0]*Y_int[0,1] - (k2+k3)*Y_int[0,2]
    K[1, 3] = k3 * Y_int[0,2]

    # Calculate the intermediate result Y[1,:]
    Y_int[1, :] = K[1, :] * 0.5 * delta_t + Y[current_time,:]

    # Calculate K[2,:]
    K[2, 0] = -k1 * Y_int[1, 0] * Y_int[1, 1] + (k2 + k3) * Y_int[1,2]
    K[2, 1] = -k1 * Y_int[1, 0] * Y_int[1, 1] + k2 * Y_int[1,2]
    K[2, 2] = k1 * Y_int[1, 0] * Y_int[1, 1] - (k2 + k3) * Y_int[1,2]
    K[2, 3] = k3 * Y_int[1, 2]

    # Calculate the intermediate result Y[2,:]
    Y_int[2, :] = K[2, :] * 0.5 * delta_t + Y[current_time, :]

    # Calculate K[3,:]
    K[3, 0] = -k1 * Y_int[2, 0] * Y_int[2, 1] + (k2 + k3) * Y_int[2,2]
    K[3, 1] = -k1 * Y_int[2, 0] * Y_int[2, 1] + k2 * Y_int[2,2]
    K[3, 2] = k1 * Y_int[2, 0] * Y_int[2, 1] - (k2 + k3) * Y_int[2,2]
    K[3, 3] = k3 * Y_int[2, 2]

    # Calculate the intermediate result Y[3,:]
    Y_int[3, :] = Y[current_time,:] + delta_t/6.0 *(K[0,:]+2.0*K[1,:]+2.0*K[2,:]+K[3,:])

    #Copy back to the result array

    Y[current_time+1,:] = Y_int[3,:]
    current_time += 1
print(Y)
plt.plot(range(1,current_time+2),Y[:,0],label="E")
plt.plot(range(1,current_time+2),Y[:,1],label="S")
plt.plot(range(1,current_time+2),Y[:,2],label="ES")
plt.plot(range(1,current_time+2),Y[:,3],label="P")
plt.legend()
plt.show()