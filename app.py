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


# Task 3 Dispersion 

# 1-Dispersion for frequency

# 1) range for frequency
f_range = f.max()-f.min()
print("the range of frequency is =",f_range)

# 2) variance for frequency
f_var = np.var(f_num)
print("the variance of frequency is +",f_var)

# 3) standard deviation for frequency
f_std = np.std(f_num)
print("the standard deviation of frequency is =",f_std)

# 4) Quartile Deviation
Qf1 = np.quantile(f_num, 0.25) #Q1
Qf3 = np.quantile(f_num, 0.75) #Q3

def f_QuartileDeviation(qf3, qf1): #quartile deviation
    return (qf3 - qf1)/2
print("the quartile deviation of  is =",f_QuartileDeviation(Qf3, Qf1))


# * * * * * * * * * * * * * * * * * * * * * * * #

# 2-Dispersion for alpha

# 1) range for alpha
alpha_range = alpha.max()-alpha.min()
print("the range of alpha is =",alpha_range)

# 2) variance for alpha
alpha_var= np.var(alpha_num)
print("the variance of alpha is =",alpha_var)

# 3) standard deviation for alpha
alpha_std = np.std(alpha_num)
print("the standard deviation of slpha is =",alpha_std)

# 4) Quartile deviation for alpha
Qa1 = np.quantile(alpha_num, 0.25) #Q1
Qa3 = np.quantile(alpha_num, 0.75) #Q3

def alpha_QuartileDeviation(qa3, qa1): #quartile deviation
    return (qa3 - qa1)/2
print("the quartile deviation of alpha is =",alpha_QuartileDeviation(Qa3, Qa1))

# * * * * * * * * * * * * * * * * * * * * * * * #

# 3-Dispersion for c

# 1) range for c
c_range = c.max()-c.min()
print("the range of c is =",c_range)

# 2) variance for c
c_var = np.var(c_num)
print("the variance of c is =",c_var)

# 3) standard deviation for c
c_std = np.std(c_num)
print("the standard deviation is =",c_std)

# 4) Quartile deviation for c
Qc1 = np.quantile(c_num, 0.25) #Q1
Qc3 = np.quantile(c_num, 0.75) #Q3

def c_QuartileDeviation(qc3, qc1): #quartile deviation
    return (qc3 - qc1)/2
print("the quartile deviation of c is =",c_QuartileDeviation(Qc3, Qc1))


# * * * * * * * * * * * * * * * * * * * * * * * #

# 4-Dispersion for u_infinity

# 1) range for u_infinity
u_infinity_range = u_infinity.max()-u_infinity.min()
print("the range of u_infinity is =",u_infinity_range)

# 2) variance for u_infinity
u_infinity_var = np.var(u_infinity_num)
print("the variance of u_infinity is =",u_infinity_var)

# 3) standard deviation for u_infinity
u_infinity_std = np.std(u_infinity_num)
print("the standard deviation of u_infinity is =",u_infinity_std)

# 4) Quartile deviation for u_infinity
Qu1 = np.quantile(u_infinity_num, 0.25) #Q1
Qu3 = np.quantile(u_infinity_num, 0.75) #Q3

def u_infinity_QuartileDeviation(qu3, qu1): #quartile deviation
    return (qu3 - qu1)/2
print("the quartile deviation of u_infinity is =",u_infinity_QuartileDeviation(Qu3, Qu1))

# * * * * * * * * * * * * * * * * * * * * * * * #

# 5-Dispersion for delta

# 1) range for delta
delta_range = delta.max()-delta.min()
print("the range of delta is =",delta_range)

# 2) variance for delta
delta_var = np.var(delta_num)
print("the variance of delta is =",delta_var)

# 3) standard deviation for delta
delta_std = np.std(delta_num)
print("the standard deviation of delta is =",delta_std)

# 4) Quartile deviation for delta
Qd1 = np.quantile(delta_num, 0.25) #Q1
Qd3 = np.quantile(delta_num, 0.75) #Q3

def delta_QuartileDeviation(qd3, qd1): #quartile deviation
    return (qd3 - qd1)/2
print("the quartile deviation of delta is =",delta_QuartileDeviation(Qd3, Qd1))
# * * * * * * * * * * * * * * * * * * * * * * * #

# 6-Dispersion for SSPL

# 1) range for SSPL
sspl_range = sspl.max()-sspl.min()
print("the range of sspl is =",sspl_range)

# 2) variance for SSPL
sspl_var = np.var(sspl_num)
print("the variance of sspl is =",sspl_var)

# 3) standard deviation for SSPL
sspl_std = np.std(sspl_num)
print("the standard deviation of sspl is =",sspl_std)

# 4) Quartile deviation for sspl
Qs1 = np.quantile(sspl_num, 0.25) #Q1
Qs3 = np.quantile(sspl_num, 0.75) #Q3

def sspl_QuartileDeviation(qs3, qs1): #quartile deviation
    return (qs3 - qs1)/2
print("the quartile deviation of sspl is =",sspl_QuartileDeviation(Qs3, Qs1))
# * * * * * * * * * * * * * * * * * * * * * * * #

