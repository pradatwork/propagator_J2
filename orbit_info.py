# this program calculates the orbital elements from initial state vector [x,y,z,vx,vy,vz]
import numpy as np
import standard_const as stdc

def sv_to_oe(r, v):

    mu = stdc.mu_e

    h = np.cross(r, v)
    norm_h = np.linalg.norm(h)

    norm_r = np.linalg.norm(r)
    norm_v = np.linalg.norm(v)

    vec_e = np.cross(v, h)/mu - r/norm_r
    e = np.linalg.norm(vec_e)

    vec_n = np.array([-h[1], h[0], 0])
    norm_n = np.linalg.norm(vec_n)

    theta = np.arccos(np.dot(vec_e, r)/(e*norm_r))
    if np.dot(r, v) < 0:
        theta = 2*np.pi-theta
    i = np.arccos(h[2]/norm_h)
    if e != 1:
        E = 2*np.arctan2(np.tan(theta/2), np.sqrt((1+e)/(1-e)))
    else: E = theta

    Omega = np.arccos(vec_n[0]/norm_n)
    if vec_n[1] < 0:
        Omega = 2*np.pi-Omega
    omega = np.arccos(np.dot(vec_n, vec_e)/ norm_n /e)
    if vec_e[2] < 0:
        omega = 2*np.pi-omega
    M = E-e*np.sin(E)
    a = norm_r/(2 - norm_r * norm_v**2/mu)

    time_period = 2*np.pi* (a)**1.5 / (stdc.mu_e)**0.5

    r_a = a*(1+e)
    r_p = a*(1-e)

    # Ranges:
    # i = [0,180°]
    # omega (ARGP) = [0,360°]
    # Omega (RAAN) = [0,360°]
    # M = [0,360°]

    return np.array(['Semi-Major Axis = ', a, 'Eccentricity=', e,
                     'Inclination=', i*180/np.pi, 'RAAN= ', Omega*180/np.pi,
                     'Argument of Perigee=', omega*180/np.pi,
                     'True Anomaly =', theta*180/np.pi,
                     'Time period (s)=', time_period, '= (in minutes)', time_period/60,
                    'Apogee distance =', r_a, 'Perigee distance =', r_p])
