# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 09:30:01 2015

@author: marlon
"""

import pandas
import numpy
import seaborn
import scipy
import matplotlib.pyplot as plt

data = pandas.read_csv('/Users/utpl/Documents/DataAnalysisTools/project3_DataAnalysisTools/gapminder.csv', low_memory=False)

#setting variables you will be working with to numeric

"""
data['internetuserate']=data['internetuserate'].replace(' ', numpy.nan)
data['internetuserate'] = pandas.to_numeric(data['internetuserate']);
data['urbanrate']=data['urbanrate'].replace(' ', numpy.nan)
data['urbanrate'] = pandas.to_numeric(data['urbanrate']);
data['incomeperperson']=data['incomeperperson'].replace(' ', numpy.nan)
data['incomeperperson'] = pandas.to_numeric(data['incomeperperson']);
"""


data['hivrate']=data['hivrate'].replace(' ', numpy.nan)
data['hivrate'] = pandas.to_numeric(data['hivrate']);

data['lifeexpectancy']=data['lifeexpectancy'].replace(' ', numpy.nan)
data['lifeexpectancy'] = pandas.to_numeric(data['lifeexpectancy']);


"""
scat1 = seaborn.regplot(x="urbanrate", y="internetuserate", fit_reg=True, data=data)
plt.xlabel('Urban Rate')
plt.ylabel('Internet Use Rate')
plt.title('Scatterplot for the Association Between Urban Rate and Internet Use Rate')

scat2 = seaborn.regplot(x="incomeperperson", y="internetuserate", fit_reg=True, data=data)
plt.xlabel('Income per Person')
plt.ylabel('Internet Use Rate')
plt.title('Scatterplot for the Association Between Income per Person and Internet Use Rate')
"""


scat1 = seaborn.regplot(x="hivrate", y="lifeexpectancy", fit_reg=True, data=data)
plt.xlabel('HIV Rate')
plt.ylabel('Life Expectancy')
plt.title('Scatterplot for the Association Between HIV Rate and Life Expectancy')

data_clean=data.dropna()

print ('association between HIV rate and lifeexpectancy')
print (scipy.stats.pearsonr(data_clean['hivrate'], data_clean['lifeexpectancy']))


"""
print ('association between incomeperperson and internetuserate')
print (scipy.stats.pearsonr(data_clean['incomeperperson'], data_clean['internetuserate']))
"""