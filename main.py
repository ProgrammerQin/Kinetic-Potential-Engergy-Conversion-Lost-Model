import matplotlib.pyplot as plt


def get_input():
    h = float(input("Please provide Object Initial height , h\n"))
    while h < 0 or h == 0:
        h = float(input("Initial height should be positive number; Please input again, v\n"))

    u = float(input("Please provide Object Initial speed, v\n"))
    while u < 0 or u == 0:
        u = float(input("Initial speed should be positive number; Please input again, v\n"))
    h = 20
    u = 1
    motion_simulator(h, u)


def motion_simulator(h, u):
    #  assign constants
    g = 10
    n_total = 401

    #  assign initial states
    n = 0
    t_top = 0
    t_bottom = 0
    v = u

    while n < n_total:
        while v >= 0:  # Ball is dropping down
            n = n + 1
            t = 0.04 * n
            t_cycle = t - t_top
            v = u + g * t_cycle
            d = u * t_cycle + 0.5 * g * t_cycle ** 2
            h_current = h - d
            print("1", format(h_current, ".2f"), d)
            print("2", format(v, ".2f"), n_total, format(t_cycle, ".2f"), format(t, ".2f"), n)
            plt.plot(t, h_current, 'bo')
            if h_current <= 0:
                p = "B"
                t_bottom = t
                print("3", format(h_current, ".2f"))
                print("4", p, format(v, ".2f"), n_total, format(t_cycle, ".2f"), format(t, ".2f"), n)
                v = (-1) * v
                u = v
                plt.plot(t, h_current, 'bo')
        while v < 0:  # Ball is bouncing back
            n = n + 1
            t = 0.04 * n
            t_cycle = t - t_bottom
            v = u + g * t_cycle
            d = u * t_cycle+0.5*g*t_cycle**2
            h_current = (-1) * d
            print("5", format(h_current, ".2f"), format(u, ".2f"), format(t_cycle, ".2f"))
            print("6", format(v, ".2f"), n_total, format(t_cycle, ".2f"), format(t, ".2f"), n)
            plt.plot(t, h_current, 'bo')
            if v >= 0:
                p = "T"
                t_top = t
                print("7", format(h_current, ".2f"))
                print("8", p, format(v, ".2f"), n_total, format(t_cycle, ".2f"), format(t, ".2f"), n)
                u = v
                h = h_current
                plt.plot(t, h_current, 'bo')

# p, Position (Top or Bottom indicated by T and B, respectively)
# v, The speed at that position
# n_total, Total number of time steps to be simulated (use 401 time steps)
# t_cycle, The time interval needed to make that motion from the previous extreme.
# t, The total time that the ball has been bouncing for since the beginning of the simulation.
# n, The cumulative number of 0.04s time steps that have been simulated


get_input()
plt.xlabel('Time [s]')
plt.ylabel('Height [m]')
plt.show()
