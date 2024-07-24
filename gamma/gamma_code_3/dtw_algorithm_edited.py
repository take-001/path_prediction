import numpy as np
from math import dist
import numpy as np

def Distance_star(a,b):

    M_ab=(np.linalg.norm(a)+np.linalg.norm(b))
    d=np.linalg.norm(a-b)
    d_=float((M_ab/2)/d)*d
    D_star=(M_ab-d)/M_ab
    
    return D_star

def dtw_pathcost_normalized(s, t):
  
    n, m = len(s), len(t)

    # Initialize the DTW matrix
    dtw = np.zeros((n+1, m+1))

    # Fill the first row and column with large values
    dtw[:,0] = np.inf
    dtw[0,:] = np.inf
    dtw[0,0] = 0

    # Compute the DTW matrix
    for i in range(1, n+1):
        for j in range(1, m+1):
            
            dist = Distance_star(np.array(s[i-1]), np.array(t[j-1]))
            dtw[i,j] = dist + min(dtw[i-1,j], dtw[i,j-1], dtw[i-1,j-1])

    # Return the DTW distance
    return dtw[n,m]