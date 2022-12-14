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

def g_mean(x):
    a = np.log(x)
    return np.exp(a.mean())
#Geometric mean for all data
f_gmean = g_mean(f)
alpha_gmean = g_mean(alpha)
c_gmean = g_mean(c)
u_infinity_gmean = g_mean(u_infinity)
delta_gmean = g_mean(delta)
sspl_gmean = g_mean(sspl)

#harmonic mean
f_hmean = 1 / f_mean
alpha_hmean = 1 / alpha_mean
c_hmean = 1 / c_mean
u_infinity_hmean = 1 / u_infinity_mean
delta_hmean = 1 / delta_mean
sspl_hmean = 1 / sspl_mean

print("Mean of f =",f_mean,"\n Mean of alpha = ",alpha_mean,"\n Mean of c = ",c_mean ,"\n Mean of u_infinity = ",u_infinity_mean,"\n Mean of Delta = ",delta_mean,"\n Mean of sspl = ",sspl_mean)
print("Mode of f = ",f_mode," \n Mode of alpha = ",alpha_mode,"\n Mode of c = ",c_mode, "\n Mode of u_infinity = ",u_infinity_mode, "\n Mode of Delta =" ,delta_mode, "\n Mode of sspl =" ,sspl_mode)
print("Median of f = ",f_median, "\n Median of alpha = ",alpha_median, "\n Median of c = ",c_median, "\n Median of u_infinity = ",u_infinity_median,"\n Median of Delta = ",delta_median, "\n Median of sspl = ",sspl_median)
print("Geometric Mean of f =",f_gmean,"\n Geometric Mean of alpha = ",alpha_gmean,"\n Geometric Mean of c = ",c_gmean ,"\n Geometric Mean of u_infinity = ",u_infinity_gmean,"\n Geometric Mean of Delta = ",delta_gmean,"\n Geometric Mean of sspl = ",sspl_gmean)
print("Harmonic Mean of f =",f_hmean,"\n Harmonic Mean of alpha = ",alpha_hmean,"\n Harmonic Mean of c = ",c_hmean ,"\n Harmonic Mean of u_infinity = ",u_infinity_hmean,"\n Harmonic Mean of Delta = ",delta_hmean,"\n Harmonic Mean of sspl = ",sspl_hmean)