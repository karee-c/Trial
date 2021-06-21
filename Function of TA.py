#!/usr/bin/env python
# coding: utf-8

# In[ ]:


pre1 = input("Enter value for first note of preceding chord: ")
pre2 = input("Enter value for second note of preceding chord: ")
pre3 = input("Enter value for third note of preceding chord: ")

suc1 = input("Enter value for first note of succeeding chord: ")
suc2 = input("Enter value for second note of succeeding chord: ")
suc3 = input("Enter value for third note of succeeding chord: ")

pree= numpy.array([pre1,pre2,pre3])
suce= numpy.array([suc1,suc2,suc3])

pre=pree.astype(int)
suc=suce.astype(int)

def ta(pre,suc): 
    return pre*suc

print(ta(pre,suc))


# In[ ]:





# In[ ]:




