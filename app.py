import numpy as np
import pandas as pd
import matplotlib as plt

# Read Data from csv
data = pd.read_csv("AirfoilSelfNoise.csv")

# Separate each column to work with
f= data['f']
alpha = data['alpha']
c = data['c']
u_infinity = data['U_infinity']
delta = data['delta']
sspl = data['SSPL']

# Turn them into numpy arrays
f_num = np.array(f)
alpha_num=np.array(alpha)
c_num = np.array(c)
u_infinity_num = np.array(u_infinity)
delta_num = np.array(delta)
sspl_num = np.array(sspl)

# Mean for All Data
f_mean = f.mean()
alpha_mean = alpha.mean()
c_mean = c.mean()
u_infinity_mean = u_infinity.mean()
delta_mean = delta.mean()
sspl_mean = sspl.mean()

# Median for All Data
f_median = f.median()
alpha_median = alpha.median()
c_median = c.median()
u_infinity_median = u_infinity.median()
delta_median = delta.median()
sspl_median = sspl.median()

# Mode for All Data
f_mode = f.mode()
alpha_mode = alpha.mode()
c_mode = c.mode()
u_infinity_mode = u_infinity.mode()
delta_mode = delta.mode()
sspl_mode = sspl.mode()
