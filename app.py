import numpy as np
import pandas as pd
#import matplotlib as plt
#import math
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
4-1 Correlation Coefficient
'''

# correlation coeffiction between f, sspl
corr_coefficient = f.corr(sspl)
print("The Correlation Coefficient of the f and sspl are: ",corr_coefficient)   

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
print("The Correlation Coefficient of the alpha and sspl are: ",corr_coefficient)      

# check the type of correlation between alpha, sspl
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
print("The Correlation Coefficient of the c and sspl are: ",corr_coefficient)

# check the type of correlation between c, sspl
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
print("The Correlation Coefficient of the u_infinity and sspl are: ",corr_coefficient)  

# check the type of correlation between u_infinity, sspl
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
print("The Correlation Coefficient of the delta and sspl are: ",corr_coefficient)
     
# check the type of correlation between delta, sspl
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
 
# This will fit the best line into the graph
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
 
# This will fit the best line into the graph
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
 
# This will fit the best line into the graph
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
 
# This will fit the best line into the graph
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
 
# This will fit the best line into the graph
plt.plot(np.unique(delta), np.poly1d(np.polyfit(delta, sspl, 1))
         (np.unique(delta)), color='yellow')

# Labelling axes
plt.xlabel('Suction side displacement thickness(delta)')
plt.ylabel('Scaled Sound Pressure Level')

plt.show()

'''
End 4-2 Correlation Coefficient
'''

