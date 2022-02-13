import numpy
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import orbit_info as oi
import tdp1
import tdp3
import standard_const as stdc
import ecc

def orbit_prop(vec_sv, t):
    rx, ry, rz, vx, vy, vz = vec_sv
    r = np.array([rx, ry, rz])
    v = np.array([vx, vy, vz])
    norm_r = np.linalg.norm(r)
    norm_v = np.linalg.norm(v)
    ax, ay, az = -r * stdc.earth_mu / norm_r ** 3
    a = np.array([ax, ay, az])

    # J2 Perturbations:
    z1_2 = r[2] ** 2
    r_2 = norm_r ** 2
    jx = r[0] / norm_r * (5 * z1_2 / r_2 - 1)
    jy = r[1] / norm_r * (5 * z1_2 / r_2 - 1)
    jz = r[2] / norm_r * (5 * z1_2 / r_2 - 3)
    j2 = 1.5 * stdc.const_J2 * stdc.earth_mu * (stdc.Re ** 2) / (norm_r ** 4) * np.array([jx, jy, jz])
    a += j2
    dydt = [vx, vy, vz, a[0], a[1], a[2]]
    return dydt

if __name__ == '__main__':

    #r1, r2, r3 = [float(x) for x in input("Enter Position Co-ordinates :").split()]
    #v1, v2, v3 = [float(x) for x in input("Enter velocity components :").split()]
    r1, r2, r3 = -2384.46, 5729.01, 3050.46
    r0 = np.array([r1, r2, r3])
    modr = np.linalg.norm(r0)
    v1, v2, v3 = -7.36138, -2.98997, 1.64354
    v0 = np.array([v1, v2, v3])

    print(r0, v0)
    orbit = oi.sv_to_oe(r0, v0)
    print(orbit)

    tspan = float(orbit[13])* 40 # propagating to 40 orbital time periods
    #tspan = 20 * 60 * 60  #secs
    dt = 10  # secs
    n_steps = int(np.ceil(tspan / dt))
    # print(tspan)

    v_sv_op = numpy.append(r0, v0)
    path1 = np.zeros((n_steps, 6))
    t1 = np.linspace(0, tspan, n_steps)
    path1 = odeint(orbit_prop, v_sv_op, t1)

    x_t1 = path1[:, 0]
    y_t1 = path1[:, 1]
    z_t1 = path1[:, 2]
    vx_t1 = path1[:, 3]
    vy_t1 = path1[:, 4]
    vz_t1 = path1[:, 5]

    print(path1)
    """
    plt.plot(t1, vx_t1)

    plt.plot(t1, vy_t1)
    plt.plot(t1, vz_t1)
    plt.show()

    """

    v_net = (vx_t1**2 + vy_t1**2 + vz_t1**2)**0.5/ np.linalg.norm(v0)
    #plt.plot(t1, v_net)
    #plt.show()
    tdp1.plot(path1)