import numpy as np
import matplotlib.pyplot as plt
# Parameters
m=1.0   #mass (kg)
c=0.5   #damping (Ns/m)
k= 4.0  #Stiffness (N/m)
F=0     #External force (N)
    #Components of Analytical Formula
zeta = c/(2*np.sqrt(m*k)) #Damping ratio
w_n = np.sqrt(k/m) #Natural frequency (rad/s)
w_d= w_n*np.sqrt(1-zeta**2) #Damped frequency (rad/s)
x0= 1   #Initial displacement (m)
v0= 0   #Initial velocity (m/s)
A = x0  # Initial Position
B = (v0 + zeta*w_n*A)/w_d # Initial Velocity
t_end = 10.0 #End time (s)
dt = 0.01 #Time step (s)
t= np.arange(0,t_end,dt)  #time step
x= np.zeros (len(t)) #displacement
v = np.zeros (len(t)) #velocity 
# Initial conditions
x[0]= x0    
v[0]= v0
      # Euler's loop for numerical integration
# Time integration using Euler's method
for i in range(1, len(t)):
    a= (F - c*v[i-1] - k*x[i-1])/m  #accelerations
    v[i]= v[i-1] + a*dt  #velocity update
    x[i]= x[i-1] + v[i-1]*dt  #displacement update
    # Analytical solution for comparison
x_analytical = np.exp(-zeta*w_n*t) * (A*np.cos(w_d*t) + B*np.sin(w_d*t))
      # Error 
error = np.abs(x - x_analytical)
    # 'Plot code block
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))

ax1.plot(t, x, color='steelblue', label='Numerical (Euler)')
ax1.plot(t, x_analytical, color='red', linestyle='--', label='Analytical')
ax1.set_title('MSD: Numerical vs Analytical')
ax1.set_xlabel('Time (s)')
ax1.set_ylabel('Displacement (m)')
ax1.legend()
ax1.grid(True)

ax2.plot(t, error, color='red')
ax2.set_title('Numerical Error (Euler, dt=0.01)')
ax2.set_xlabel('Time (s)')
ax2.set_ylabel('Absolute Error (m)')
ax2.grid(True)

plt.tight_layout()
plt.show()

