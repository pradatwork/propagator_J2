import numpy as np
import standard_const as stdc

def ecc(r, v):

    mu = stdc.mu_e

    h = np.cross(r, v)
    norm_h = np.linalg.norm(h)

    norm_r = np.linalg.norm(r)
    norm_v = np.linalg.norm(v)

    vec_e = np.cross(v, h)/mu - r/norm_r
    e = np.linalg.norm(vec_e)

    return vec_e