# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 08:57:08 2020

@author: crich
"""

# In[ REGEX: remove items from list ]
import re
full = ['webb', 'ellis', '(sportswear)']
regex = re.compile(r'(.*\)$')
filtered = [i for i in full if not regex.match(i)]
print(filtered)


# In[ ]


# In[ ]



# In[ ]



# In[ ]