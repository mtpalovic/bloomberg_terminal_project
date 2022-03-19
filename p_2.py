#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np
from scipy import linspace, polyval, polyfit, sqrt, stats, randn, optimize

import pandas as pd
import matplotlib.pyplot as plt

import csv

import scipy
from sklearn.linear_model import LinearRegression

import matplotlib as plt
get_ipython().run_line_magic('matplotlib', 'inline')

import sphinx


# In[ ]:


class lr(object):
    """
    Class constructor.
    """
    def __init__(self,x0,y0,l,iter_):
        """
        Constructor method.
        """
        
        self.x0 = x0
        self.y0 = y0
        
        self.l = float(l)
        #forces to be float or init, otherwise error raised
        assert (type(l)==float or type(l)==int or type(x0)==None)
        
        
        self.iter_ = iter_
        self.n = len(self.x0)
        
        #weight,bias, not part of init
        self.a = 0
        self.b = 0
        
        self.h = np.zeros(self.iter_)
        
    def c(self,y_):
        """
        Cost function
        :param y_: init method
        :type y_: init method
        
        :return:
        :rtype: 
        
        """
        c = np.sum(np.square(self.y0 - y_))/(2*self.n)
        return c 
    
    def f(self):
        """
        Fit function
        :param y_: init method
        :type y_: init method
        
        :return:
        :rtype: 
        
        """
        for e in range(0,len(self.iters_),1):
            
            y_ = self.b*self.X + self.a
            
            dv_a = (-2/self.n)*(self.y0 - y_)
            
            dv_b = (-2/self.n)*(self.x0*(self.y0 - y_))
            
            
            self.a = self.a - dv_a*self.l
            self.b = self.b - dv_b*self.l
            
            self.history[e] = self.c(y_)
            self.mse = self.mean_se(y_,self.y0)
        
        return self.mse
    
    
    def mean_se(self,y_p,y)
        """
        Mean squared error.
        :param y_: init method
        :type y_: init method
        
        :return:
        :rtype: 
        
        """
        er = y - y_p
        mse = np.sum(np.square(er))/self.n
        
        return mse

