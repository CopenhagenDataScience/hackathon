import numpy as np


np.random.random()

def v(t):
     val = np.sqrt(t)

     if t == 1015:
          val = val*1.1
     eps = np.random.normal(0, val*0.1)

     return val*np.sqrt(t)*0.1 + eps


def createseries():
    out = []
    for t in range(1000,1100):
         out.append('({},{})'.format(t, v(t)))

    return '\n'.join(out)



print(createseries())
