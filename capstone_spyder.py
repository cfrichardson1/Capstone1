# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 20:03:14 2020

@author: crich
"""

# In[ Dependencies & Data Load ]

import pandas as pd
import os
import re

os.chdir(r'C:\Users\crich\Google Drive\Colab Notebooks\Thinkful\Capstone 1')
os.getcwd()
#os.listdir()


df = pd.read_csv('LoanStats_securev1_2020Q1.csv', sep=',')
Lending_Club_Dictionary = pd.read_excel('LCDataDictionary.xlsx')


# In[  ]

sorted(df.columns)
# In[  ]

df.columns

# In[  ]

df['LoanStatus'].unique()



# In[  ]

sorted(current_listing.columns)


# In[  ]
# 
column_list= ['id', 'member_id', 'loan_amnt', 'funded_amnt', 'funded_amnt_inv',
       'term', 'int_rate', 'installment', 'grade', 'sub_grade','emp_length', 'home_ownership', 'grade', 'sub_grade'

df = current_listing[column_list]
del(current_listing)

# In[  ]

regex_list = [r'all\d*$',r'ale\d*$', r'bac\d*$', r'bnk\d*$', r'cap\d*$', r'fil\d*$',r'cv\d*.*$', r'hi\d*.*$', r'hi\d*.*$', r'in\d*.*$',
               r'hi\d*.*$', r'mt\d*.*$', r'rt\d*.*$', r'rev\d*$', r'rtr\d*$',]
    
# In[  ]
columns_ = current_listing.columns
len(columns_)
# In[  ]

for reg in regex_list:
    columns_ = columns_[~columns_.str.contains(reg ,regex=True)]
    

for col in columns_:
    print(col)

len(columns_)


# In[  ]


# In[  ]


# In[  ]





# In[  ]


# In[  ]


# In[  ]


# In[  ]





# In[  ]


# In[  ]


# In[  ]


# In[  ]





