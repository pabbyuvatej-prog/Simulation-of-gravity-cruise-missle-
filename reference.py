import numpy as np
I=np.array([[4.9138e-4,0,-5.1552e-4],[0,4.5830e-3,0],[-5.1552e-4,0,4.5126e-3]])
def gyro_qdot(p):
 w=np.array([p,0.,0.]); return np.linalg.solve(I,-np.cross(w,I@w))[1]
