import numpy as np
import matplotlib.pyplot as plt

def Rz(theta):
    return np.array([[  np.cos(theta), -np.sin(theta), 0 ],
                      [ np.sin(theta),  np.cos(theta), 0 ],
                      [ 0            ,  0            , 1 ]])

R_1_0 = Rz(np.deg2rad(45))
p1 = [2, 2, 0]
p0 = R_1_0 @ p1
print(p0)