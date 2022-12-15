import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
'''
Presented By Team:
1- Abdelazez Mohamed
2- Beshoy Mark
3- Fatma Tarek
4- Hager Ashraf
5- Nabil Mohamed
6- Sohila Abdallah
'''

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


# Task 2 Central Tendency

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
print("\nMode of f = ",f_mode," \n Mode of alpha = ",alpha_mode,"\n Mode of c = ",c_mode, "\n Mode of u_infinity = ",u_infinity_mode, "\n Mode of Delta =" ,delta_mode, "\n Mode of sspl = " ,sspl_mode)
print("\nMedian of f = ",f_median, "\n Median of alpha = ",alpha_median, "\n Median of c = ",c_median, "\n Median of u_infinity = ",u_infinity_median,"\n Median of Delta = ",delta_median, "\n Median of sspl = ",sspl_median)
print("\nGeometric Mean of f =",f_gmean,"\n Geometric Mean of alpha = ",alpha_gmean,"\n Geometric Mean of c = ",c_gmean ,"\n Geometric Mean of u_infinity = ",u_infinity_gmean,"\n Geometric Mean of Delta = ",delta_gmean,"\n Geometric Mean of sspl = ",sspl_gmean)
print("\nHarmonic Mean of f =",f_hmean,"\n Harmonic Mean of alpha = ",alpha_hmean,"\n Harmonic Mean of c = ",c_hmean ,"\n Harmonic Mean of u_infinity = ",u_infinity_hmean,"\n Harmonic Mean of Delta = ",delta_hmean,"\n Harmonic Mean of sspl = ",sspl_hmean)





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
print("the standard deviation of frequency is =",f_std)

# 4) Quartile Deviation
Qf1 = np.quantile(f_num, 0.25) #Q1
Qf3 = np.quantile(f_num, 0.75) #Q3


print("the quartile deviation of  is =",QuartileDeviation(Qf3, Qf1))


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


print("the quartile deviation of alpha is =",QuartileDeviation(Qa3, Qa1))

# * * * * * * * * * * * * * * * * * * * * * * * #

# 3-Dispersion for c

# 1) range for c
c_range = c.max()-c.min()
print("the range of c is = ",c_range)

# 2) variance for c
c_var = np.var(c_num)
print("the variance of c is = ",c_var)

# 3) standard deviation for c
c_std = np.std(c_num)
print("the standard deviation is = ",c_std)

# 4) Quartile deviation for c
Qc1 = np.quantile(c_num, 0.25) #Q1
Qc3 = np.quantile(c_num, 0.75) #Q3


print("the quartile deviation of c is = ",QuartileDeviation(Qc3, Qc1))


# * * * * * * * * * * * * * * * * * * * * * * * #

# 4-Dispersion for u_infinity

# 1) range for u_infinity
u_infinity_range = u_infinity.max()-u_infinity.min()
print("the range of u_infinity is = ",u_infinity_range)

# 2) variance for u_infinity
u_infinity_var = np.var(u_infinity_num)
print("the variance of u_infinity is = ",u_infinity_var)

# 3) standard deviation for u_infinity
u_infinity_std = np.std(u_infinity_num)
print("the standard deviation of u_infinity is = ",u_infinity_std)

# 4) Quartile deviation for u_infinity
Qu1 = np.quantile(u_infinity_num, 0.25) #Q1
Qu3 = np.quantile(u_infinity_num, 0.75) #Q3

print("the quartile deviation of u_infinity is = ",QuartileDeviation(Qu3, Qu1))

# * * * * * * * * * * * * * * * * * * * * * * * #

# 5-Dispersion for delta

# 1) range for delta
delta_range = delta.max()-delta.min()
print("the range of delta is = ",delta_range)

# 2) variance for delta
delta_var = np.var(delta_num)
print("the variance of delta is = ",delta_var)

# 3) standard deviation for delta
delta_std = np.std(delta_num)
print("the standard deviation of delta is = ",delta_std)

# 4) Quartile deviation for delta
Qd1 = np.quantile(delta_num, 0.25) #Q1
Qd3 = np.quantile(delta_num, 0.75) #Q3


print("the quartile deviation of delta is = ",QuartileDeviation(Qd3, Qd1))
# * * * * * * * * * * * * * * * * * * * * * * * #

# 6-Dispersion for SSPL

# 1) range for SSPL
sspl_range = sspl.max()-sspl.min()
print("the range of sspl is = ",sspl_range)

# 2) variance for SSPL
sspl_var = np.var(sspl_num)
print("the variance of sspl is = ",sspl_var)

# 3) standard deviation for SSPL
sspl_std = np.std(sspl_num)
print("the standard deviation of sspl is = ",sspl_std)

# 4) Quartile deviation for sspl
Qs1 = np.quantile(sspl_num, 0.25) #Q1
Qs3 = np.quantile(sspl_num, 0.75) #Q3


print("the quartile deviation of sspl is = ",QuartileDeviation(Qs3, Qs1))
# * * * * * * * * * * * * * * * * * * * * * * * #

'''
4-1 Correlation Coefficient
'''
# correlation coeffiction between f, sspl
corr_coefficient = f.corr(sspl)
print("\nThe Correlation Coefficient of the f and sspl are: ",corr_coefficient)

# check the type of correlation between f, sspl
if(corr_coefficient<=-0.01 and corr_coefficient>=-0.49):
    print("Negative Weak")  
elif(corr_coefficient<=-0.5 and corr_coefficient>=-0.69):
    print("Negative Moderate")  
elif(corr_coefficient<=-0.7 and corr_coefficient>=-0.99):
    print("Negative Strong")     
elif(corr_coefficient==-1):
    print("Negative Perfect") 
elif(corr_coefficient==0):
    print("No Linear Correlation") 
elif(corr_coefficient==1):
    print("Positive Perfect") 
elif(corr_coefficient>=0.01 and corr_coefficient<=0.49):
    print("Positive Weak")  
elif(corr_coefficient>=0.5 and corr_coefficient<=0.69):
    print("Positive Moderate")  
elif(corr_coefficient>=0.7 and corr_coefficient<=0.99):
    print("Positive Strong")

# correlation coeffiction between alpha, sspl
corr_coefficient= alpha.corr(sspl)
print("\nThe Correlation Coefficient of the alpha and sspl are: ",corr_coefficient)

# check the type of correlation between f, sspl
if(corr_coefficient<=-0.01 and corr_coefficient>=-0.49):
    print("Negative Weak")  
elif(corr_coefficient<=-0.5 and corr_coefficient>=-0.69):
    print("Negative Moderate")  
elif(corr_coefficient<=-0.7 and corr_coefficient>=-0.99):
    print("Negative Strong")     
elif(corr_coefficient==-1):
    print("Negative Perfect") 
elif(corr_coefficient==0):
    print("No Linear Correlation") 
elif(corr_coefficient==1):
    print("Positive Perfect") 
elif(corr_coefficient>=0.01 and corr_coefficient<=0.49):
    print("Positive Weak")  
elif(corr_coefficient>=0.5 and corr_coefficient<=0.69):
    print("Positive Moderate")  
elif(corr_coefficient>=0.7 and corr_coefficient<=0.99):
    print("Positive Strong")

# correlation coeffiction between c, sspl
corr_coefficient = c.corr(sspl)
print("\nThe Correlation Coefficient of the c and sspl are: ",corr_coefficient)

# check the type of correlation between f, sspl
if(corr_coefficient<=-0.01 and corr_coefficient>=-0.49):
    print("Negative Weak")  
elif(corr_coefficient<=-0.5 and corr_coefficient>=-0.69):
    print("Negative Moderate")  
elif(corr_coefficient<=-0.7 and corr_coefficient>=-0.99):
    print("Negative Strong")     
elif(corr_coefficient==-1):
    print("Negative Perfect") 
elif(corr_coefficient==0):
    print("No Linear Correlation") 
elif(corr_coefficient==1):
    print("Positive Perfect") 
elif(corr_coefficient>=0.01 and corr_coefficient<=0.49):
    print("Positive Weak")  
elif(corr_coefficient>=0.5 and corr_coefficient<=0.69):
    print("Positive Moderate")  
elif(corr_coefficient>=0.7 and corr_coefficient<=0.99):
    print("Positive Strong")

# correlation coeffiction between u_infinity, sspl
corr_coefficient = u_infinity.corr(sspl)
print("\nThe Correlation Coefficient of the u_infinity and sspl are: ",corr_coefficient)

# check the type of correlation between f, sspl
if(corr_coefficient<=-0.01 and corr_coefficient>=-0.49):
    print("Negative Weak")  
elif(corr_coefficient<=-0.5 and corr_coefficient>=-0.69):
    print("Negative Moderate")  
elif(corr_coefficient<=-0.7 and corr_coefficient>=-0.99):
    print("Negative Strong")     
elif(corr_coefficient==-1):
    print("Negative Perfect") 
elif(corr_coefficient==0):
    print("No Linear Correlation") 
elif(corr_coefficient==1):
    print("Positive Perfect") 
elif(corr_coefficient>=0.01 and corr_coefficient<=0.49):
    print("Positive Weak")  
elif(corr_coefficient>=0.5 and corr_coefficient<=0.69):
    print("Positive Moderate")  
elif(corr_coefficient>=0.7 and corr_coefficient<=0.99):
    print("Positive Strong")

# correlation coeffiction between delta, sspl
corr_coefficient = delta.corr(sspl)
print("\nThe Correlation Coefficient of the delta and sspl are: ",corr_coefficient)

# check the type of correlation between f, sspl
if(corr_coefficient<=-0.01 and corr_coefficient>=-0.49):
    print("Negative Weak")  
elif(corr_coefficient<=-0.5 and corr_coefficient>=-0.69):
    print("Negative Moderate")  
elif(corr_coefficient<=-0.7 and corr_coefficient>=-0.99):
    print("Negative Strong")     
elif(corr_coefficient==-1):
    print("Negative Perfect") 
elif(corr_coefficient==0):
    print("No Linear Correlation") 
elif(corr_coefficient==1):
    print("Positive Perfect") 
elif(corr_coefficient>=0.01 and corr_coefficient<=0.49):
    print("Positive Weak")  
elif(corr_coefficient>=0.5 and corr_coefficient<=0.69):
    print("Positive Moderate")  
elif(corr_coefficient>=0.7 and corr_coefficient<=0.99):
    print("Positive Strong")



'''
4-2 Correlation Drawing & Linear Regression Drawing
'''

################### Drawing Correlation between f , sspl ###################

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

################### Drawing Correlation between alpha , sspl ###################

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

################### Drawing Correlation between c , sspl ###################

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

################### Drawing Correlation between u_infinity , sspl ###################

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

################### Drawing Correlation between delta , sspl ###################

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
5- Linear Regression (Rx/y)
'''

# Regression for f & sspl
n= np.size(f_num)
sxy = np.sum(f_num*sspl_num)
nXmYm= n*f_mean*sspl_mean
sX2 = np.sum(f_num*f_num)
sXm2= n-f_mean*f_mean

b = (sxy-nXmYm)/(sX2-n*sXm2)
a = f_mean -b*sspl_mean

print(f"Regression for f & sspl\nX = {a} + {b} Y")


# Regression for c & sspl
n= np.size(c_num)
sxy = np.sum(c_num*sspl_num)
nXmYm= n*c_mean*sspl_mean
sX2 = np.sum(c_num*c_num)
sXm2= n-c_mean*c_mean

b = (sxy-nXmYm)/(sX2-n*sXm2)
a = c_mean -b*sspl_mean

print(f"\n\nRegression for C & sspl\nX = {a} + {b} Y")


# Regression for alpha & sspl
n= np.size(alpha_num)
sxy = np.sum(alpha_num*sspl_num)
nXmYm= n*alpha_mean*sspl_mean
sX2 = np.sum(alpha_num*alpha_num)
sXm2= n-alpha_mean*alpha_mean

b = (sxy-nXmYm)/(sX2-n*sXm2)
a = alpha_mean -b*sspl_mean

print(f"\n\nRegression for Alpha & sspl\nX = {a} + {b} Y")


# Regression for delta & sspl
n= np.size(delta_num)
sxy = np.sum(delta_num*sspl_num)
nXmYm= n*delta_mean*sspl_mean
sX2 = np.sum(delta_num*delta_num)
sXm2= n-delta_mean*delta_mean

b = (sxy-nXmYm)/(sX2-n*sXm2)
a = delta_mean -b*sspl_mean

print(f"\n\nRegression for Delta & sspl\nX = {a} + {b} Y")


# Regression for U_infinty & sspl
n= np.size(u_infinity_num)
sxy = np.sum(u_infinity_num*sspl_num)
nXmYm= n*u_infinity_mean*sspl_mean
sX2 = np.sum(u_infinity_num*u_infinity_num)
sXm2= n-u_infinity_mean*u_infinity_mean

b = (sxy-nXmYm)/(sX2-n*sXm2)
a = u_infinity_mean -b*sspl_mean

print(f"\n\nRegression for U_infinty & sspl\nX = {a} + {b} Y")