from math import dist
import numpy as np

def Distance_star(a,b):
    M_ab=(np.linalg.norm(a)+np.linalg.norm(b))
    D_star=(M_ab-np.linalg.norm(a-b))/M_ab
    return D_star