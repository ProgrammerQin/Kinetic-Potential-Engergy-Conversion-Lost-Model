# Modeling_Kinetic_Potential_Engergy_Conversion_Lost

Part A: Dropping a Ball!
We all drop the ball occasionally (pun intended)J Let us study how it bounces back though.

The process: Assume that the ball is dropped from a certain height (h) with an initial speed of u m/s. The
ball travels down and as it is acted upon by the gravitational force (g ~ 10m/s2), it hits the ground with a
higher final speed v. This final speed is calculated using the relation v = u+gt. Upon hitting the ground the
ball rebounds. Let us assume that it rebounds without any loss of energy, i.e., it rebounds with the same
speed v. As the ball moves up, it decelerates at the rate of -g (i.e. g ~ -10m/s2) and eventually when it get
back to the original height of h, it stops. It then starts falling back to the ground, emulating the initial fall.
The distance that the ball rises/falls is d = ut + 0.5gt2. (Note: If the initial dropping velocity is 0 m/s then
the ball must rise to the exact same initial height. If the ball it thrown with a certain downward speed,
then it rebounds to a greater height than the initial height.)

Now, write a python program that simulates this process by doing the following: Using the getInput()
function obtain the following values from the user: initial height and initial speed. (Both will be a
positive number). Use the motionSimulator() function to simulate the falling and rising of the ball. In
this you will have to increment time by small steps of 0.04s and determine the precise position of the
ball for these timesteps, plotting it as a function of time. You must print the following data onto the
screen each time the ball reaches the extremum:

1. Position (Top or Bottom indicated by T and B, respectively).
2. The speed at that position
3. Total number of timesteps to be simulated (use 401 timesteps)
4. The time interval needed to make that motion from the previous extremum.
5. The total time that the ball has been bouncing for since the beginning of the simulation.
6. The cumulative number of 0.04s timesteps that have been simulated.
7. A graph showing the bouncing of the ball through the entire duration

import matplotlib.pyplot as plt
plt.plot(time,current_height,'bo')
plt.xlabel('Time [s]')
plt.ylabel('Height [m]')

Use floats for all your variables except the number of timesteps. The output should be printed only
from the main program. Your program output should be in the following format:
Test Case 1: (h=20, u=0)
S. Srinivasan

B: 20.00 2.00 2.00 50
T: 0.00 2.00 4.00 100
B: 20.00 2.00 6.00 150
T: 0.00 2.00 8.00 200
B: 20.00 2.00 10.00 250
T: 0.00 2.00 12.00 300
B: 20.00 2.00 14.00 350
T: 0.00 2.00 16.00 400
Test Case 2: (h=20, u=10)
B: 22.40 1.24 1.24 31
T: 0.00 2.24 3.48 87
B: 22.80 2.28 5.76 144
T: 0.00 2.28 8.04 201
B: 22.80 2.28 10.32 258
T: 0.00 2.28 12.60 315
B: 23.20 2.32 14.92 373


Part B: Energy Loss
There is an unrealistic assumption in part A. The ball will always lose some energy when it hits the ground.
As a result it will not be able to get back to the same height. So, let us fix the problem. Copy and paste the
code from part A since you will need most of it. Use the energyLoss() function that determines the
rebound speed (v) using the principle of conservation of energy. For a given bounce, when the ball is at
the highest point (y), its potential energy is E_potential = mgy, where m is the mass of the ball (not
needed), and g is as in part A. When it hits the ground, this energy converts itself to the kinetic energy
E_kinetic = 0.5mv2, where v is the rebound speed. Assume that the loss of the potential energy is Ep when
the ball hits the ground and calculate the rebound speed (v) in this function. Ep is obtained from the
getInput() function as a decimal value (example, Ep = 0.1 for 10% loss).

As in part A, using the getInput() function obtain the following values from the user: initial height and
initial speed. (Both will be a positive number). Use the motionSimulator() function to simulate the falling
and rising of the ball. In this you will have to increment time by small steps of 0.04s and determine the
precise position of the ball for these timesteps, plotting it as a function of time. You must print the
following data onto the screen each time the ball reaches the extremum:
1. Position (Top or Bottom indicated by T and B, respectively).
2. The speed at that position
3. Total number of timesteps to be simulated (use 401 timesteps)
4. The time interval needed to make that motion from the previous extremum.
5. The total time that the ball has been bouncing for since the beginning of the simulation.
6. The cumulative number of 0.04s timesteps that have been simulated.
7. A graph showing the bouncing of the ball through the entire duration.

The output should be printed only form the main program. Try different combinations of inputs to
understand how the ball bounces. 

program output should be in the following format
Test Case 1: (h=20, u=0, Ep = 0.1)
B: 18.97 2.00 2.00 50
T: 0.00 1.92 3.92 98
B: 18.21 1.92 5.84 146
T: 0.00 1.84 7.68 192
B: 17.46 1.84 9.52 238
T: 0.00 1.76 11.28 282
B: 16.70 1.76 13.04 326
T: 0.00 1.68 14.72 368

Test Case 2: (h=20, u=10, Ep=0.1)
B: 21.25 1.24 1.24 31
T: 0.00 2.16 3.40 85
B: 20.49 2.16 5.56 139
T: 0.00 2.08 7.64 191
B: 19.73 2.08 9.72 243
T: 0.00 2.00 11.72 293
B: 18.97 2.00 13.72 343
T: 0.00 1.92 15.64 391

Test case 3: (h=20,u=20,Ep=0.3)
B: 23.76 0.84 0.84 21
T: 0.00 2.40 3.24 81
B: 20.08 2.40 5.64 141
T: 0.00 2.04 7.68 192
B: 17.07 2.04 9.72 243
T: 0.00 1.72 11.44 286
B: 14.39 1.72 13.16 329
T: 0.00 1.44 14.60 365
Only a screenshot of the program output (see sample of test case results including the figure) is allowed.
