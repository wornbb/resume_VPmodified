
import numpy as np
p = np.loadtxt("power_grid.test")
t = np.loadtxt("trans.gridIR")
step_percycle = 5
size = t.shape
t = np.repeat(t, np.ones(size[0],dtype=int)*step_percycle,axis=0)
o = np.divide(p, t)
print(o.shape)
np.savetxt("current_grid.test", o, delimiter='  ')

