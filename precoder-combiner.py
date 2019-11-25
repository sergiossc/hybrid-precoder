import numpy as np


Ns = 4 # number of datastreams
Nrf = 4 # number of RF chains
Nbs = 10 # number of antennas in BS
Nms = 5 # number of antennas in MS

#s = np.zeros((Ns, 1)) # datastream vector. s is a Nsx1 vector of tramsmitted symbols
s = np.array([[1+1j], [-1+1j], [-1-1j], [1-1j]]) # datastream vector. s is a Nsx1 vector of tramsmitted symbols

Fbb = np.zeros((Nrf,Ns)) # Fbb is a precoder baseband matrix on BS
Frf = np.zeros((Nbs, Nrf)) # Frf is a precoder rf matrix on BS

Ft = np.matmul(Frf, Fbb) # Tf is the combined matrix of precoding from Frf x Fbb

x = np.matmul(Ft, s) #  x is the discrete-time tramsmitted signal

#my_frf = np.random.randint(0, 100)

print (Fbb)
print (Frf)
print (Ft)
print (s)
print (x)
