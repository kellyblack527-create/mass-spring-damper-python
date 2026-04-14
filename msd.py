import numpy as np
import matplotlib.pyplot as plt
m=1.0   #mass (kg)
c=0.5   #damping (Ns/m)
k= 4.0  #Stiffness (N/m)
F=0     #External force (N)
x0= 1   #Initial displacement (m)
v0= 0   #Initial velocity (m/s)
t_end = 10.0 #End time (s)
dt = 0.01 #Time step (s)
t= np.arange(0,t_end,dt)  #time step
x= np.zeros (len(t)) #displacement
v = np.zeros (len(t)) #velocity
# Initial conditions
x[0]= x0    
v[0]= v0
# Time integration using Euler's method
for i in range(1, len(t)):
    a= (F - c*v[i-1] - k*x[i-1])/m  #accelerations v[i]= v[i-1] + a*dt  #velocity update
    x[i]= x[i-1] + v[i]*dt  #displacement update
    #Plot code block
plt.figure(figsize=(10,5))
plt.plot(t, x, color='steelblue')
plt.title('Mass-Spring-Damper Response')
plt.xlabel('Time (s)')
plt.ylabel('Displacement (m)')
plt.grid(True)
plt.tight_layout()
plt.show()
