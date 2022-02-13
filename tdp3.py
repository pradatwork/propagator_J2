from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
import standard_const as stdc

def plot(r, r2, r3):

    fig = plt.figure(figsize=(10, 10))
    ax = fig.add_subplot(111, projection='3d')

    ax.plot(r[:, 0], r[:, 1], r[:, 2], 'r')
    ax.plot(r2[:, 0], r2[:, 1], r2[:, 2], 'k')
    ax.plot(r3[:, 0], r3[:, 1], r3[:, 2], 'b')
    ax.plot([r[0, 0]], [r[0, 1]], [r[0, 2]], 'ko')
    ax.plot([r2[0, 0]], [r2[0, 1]], [r2[0, 2]], 'ko')
    ax.plot([r3[0, 0]], [r3[0, 1]], [r3[0, 2]], 'bo')

    r_plot = stdc.Re * 2 / 3

    _u, _v = np.mgrid[0: 2*np.pi: 20j, 0: np.pi: 10j]
    _x = r_plot*np.cos(_u)*np.sin(_v)
    _y = r_plot*np.sin(_u)*np.sin(_v)
    _z = r_plot*np.cos(_v)
    ax.plot_surface(_x, _y, _z, cmap= 'Blues')

    max_val = stdc.Re*1.25

    ax.set_xlim([-max_val, max_val])
    ax.set_ylim([-max_val, max_val])
    ax.set_zlim([-max_val, max_val])
    ax.set_xlabel('X (km)')
    ax.set_ylabel('Y (km)')
    ax.set_zlabel('Z (km)')
    ax.set_aspect('auto')

    plt.legend(['Initial Orbit', 'Transfer Trajectory ', 'Final Orbit', 'Start point',
                'Firing point', 'Final Orbit Insertion'])

    plt.show()



