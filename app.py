import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


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



'''
1-1 Histogram 
'''

plt.title('Histogram For F ')
plt.hist(f,bins=10)
plt.show()

plt.title('Histogram For alpha ')
plt.hist(alpha,bins=10)
plt.show()

plt.title('Histogram For C ')
plt.hist(c,bins=10)
plt.show()

plt.title('Histogram For u_infinity ')
plt.hist(u_infinity,bins=10)
plt.show()

plt.title('Histogram For delta ')
plt.hist(delta,bins=10)
plt.show()

plt.title('Histogram For sspl ')
plt.hist(sspl,bins=10)
plt.show()


'''
1-2 Density Plot 
'''
plt.title('Density Plot For f ')
f.plot.kde()
plt.show()

plt.title('Density Plot For alpha ')
alpha.plot.kde()
plt.show()

plt.title('Density Plot For c ')
c.plot.kde()
plt.show()

plt.title('Density Plot For u_infinity ')
u_infinity.plot.kde()
plt.show()

plt.title('Density Plot For delta ')
delta.plot.kde()
plt.show()

plt.title('Density Plot For sspl ')
sspl.plot.kde()
plt.show()

'''
1-3 BoxPlot
'''

plt.title('boxplot Plot For f ')
plt.boxplot(f, showmeans=True)
plt.show()

plt.title('boxplot Plot For alpha ')
plt.boxplot(alpha, showmeans=True)
plt.show()

plt.title('boxplot Plot For c ')
plt.boxplot(c, showmeans=True)
plt.show()

plt.title('boxplot Plot For u_infinity ')
plt.boxplot(u_infinity, showmeans=True)
plt.show()

plt.title('boxplot Plot For delta ')
plt.boxplot(delta, showmeans=True)
plt.show()

plt.title('boxplot Plot For sspl ')
plt.boxplot(sspl, showmeans=True)
plt.show()


# Task 3 Dispersion 

def QuartileDeviation(qf3, qf1): #quartile deviation
    return (qf3 - qf1)/2

# 1-Dispersion for frequency

# 1) range for frequency
f_range = f.max()-f.min()
print("the range of frequency is =",f_range)

# 2) variance for frequency
f_var = np.var(f_num)
print("the variance of frequency is +",f_var)

# 3) standard deviation for frequency
f_std = np.std(f_num)
print(f_std)

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
print(alpha_std)

# * * * * * * * * * * * * * * * * * * * * * * * #

# 3-Dispersion for c

# 1) range for c
c_range = c.max()-c.min()
print(c_range)

# 2) variance for c
c_var = np.var(c_num)
print(c_var)

# 3) standard deviation for c
c_std = np.std(c_num)
print(c_std)

# * * * * * * * * * * * * * * * * * * * * * * * #

# 4-Dispersion for u_infinity

# 1) range for u_infinity
u_infinity_range = u_infinity.max()-u_infinity.min()
print(u_infinity_range)

# 2) variance for u_infinity
u_infinity_var = np.var(u_infinity_num)
print(u_infinity_var)

# 3) standard deviation for u_infinity
u_infinity_std = np.std(u_infinity_num)
print(u_infinity_std)

# * * * * * * * * * * * * * * * * * * * * * * * #

# 5-Dispersion for delta

# 1) range for delta
delta_range = delta.max()-delta.min()
print(delta_range)

# 2) variance for delta
delta_var = np.var(delta_num)
print(delta_var)

# 3) standard deviation for delta
delta_std = np.std(delta_num)
print(delta_std)

# * * * * * * * * * * * * * * * * * * * * * * * #

# 6-Dispersion for SSPL

# 1) range for SSPL
sspl_range = sspl.max()-sspl.min()
print(sspl_range)

# 2) variance for SSPL
sspl_var = np.var(sspl_num)
print(sspl_var)

# 3) standard deviation for SSPL
sspl_std = np.std(sspl_num)
print(sspl_std)

# * * * * * * * * * * * * * * * * * * * * * * * #

'''
4-1 Correlation Coefficient
'''
# correlation coeffiction between f, sspl
corr_coefficient = f.corr(sspl)
print("The Correlation Coefficient of the f and sspl are: ",corr_coefficient)

# correlation coeffiction between alpha, sspl
corr_coefficient= alpha.corr(sspl)
print("The Correlation Coefficient of the alpha and sspl are: ",corr_coefficient)

# correlation coeffiction between c, sspl
corr_coefficient = c.corr(sspl)
print("The Correlation Coefficient of the c and sspl are: ",corr_coefficient)

# correlation coeffiction between u_infinity, sspl
corr_coefficient = u_infinity.corr(sspl)
print("The Correlation Coefficient of the u_infinity and sspl are: ",corr_coefficient)

# correlation coeffiction between delta, sspl
corr_coefficient = delta.corr(sspl)
print("The Correlation Coefficient of the delta and sspl are: ",corr_coefficient)

'''
End 4-1 Correlation Coefficient
'''

'''
4-2 Correlation Coefficient
'''

###################Drawing Correlation between f , sspl###################

# adds the title
plt.title('Correlation between f & sspl')


#plotting the data
plt.scatter(f, sspl)
 
# This will fit the best line into the graph (linear regression)
plt.plot(np.unique(f), np.poly1d(np.polyfit(f, sspl, 1))
         (np.unique(f)), color='red')
 
# Labelling axes
plt.xlabel('Frequency')
plt.ylabel('Scaled Sound Pressure Level')

plt.show()

###################Drawing Correlation between alpha , sspl###################

# adds the title
plt.title('Correlation between alpha & sspl')

#plotting the data
plt.scatter(alpha, sspl)
 
# This will fit the best line into the graph (linear regression)
plt.plot(np.unique(alpha), np.poly1d(np.polyfit( alpha, sspl, 1))
         (np.unique(alpha)), color='green')

# Labelling axes
plt.xlabel('Angle of attack(alpha)')
plt.ylabel('Scaled Sound Pressure Level')

plt.show()

###################Drawing Correlation between c , sspl###################

# adds the title
plt.title('Correlation between c & sspl')

#plotting the dat
plt.scatter(c, sspl)
 
# This will fit the best line into the graph (linear regression)
plt.plot(np.unique(c), np.poly1d(np.polyfit(c, sspl, 1))
         (np.unique(c)), color='gray')

# Labelling axes
plt.xlabel('Chord length(c)')
plt.ylabel('Scaled Sound Pressure Level')

plt.show()

###################Drawing Correlation between u_infinity , sspl###################

# adds the title
plt.title('Correlation between u_infinity  & sspl')

#plotting the data
plt.scatter(u_infinity, sspl)
 
# This will fit the best line into the graph  (linear regression)
plt.plot(np.unique(u_infinity), np.poly1d(np.polyfit(u_infinity, sspl, 1))
         (np.unique(u_infinity)), color='orange')

# Labelling axes
plt.xlabel('Free-stream velocity( u_infinity)')
plt.ylabel('Scaled Sound Pressure Level')

plt.show()

###################Drawing Correlation between delta , sspl###################

# adds the title
plt.title('Correlation between delta  & sspl')

#plotting the data
plt.scatter(delta, sspl)
 
# This will fit the best line into the graph (linear regression)
plt.plot(np.unique(delta), np.poly1d(np.polyfit(delta, sspl, 1))
         (np.unique(delta)), color='yellow')

# Labelling axes
plt.xlabel('Suction side displacement thickness(delta)')
plt.ylabel('Scaled Sound Pressure Level')

plt.show()

'''
End 4-2 Correlation Coefficient
'''


