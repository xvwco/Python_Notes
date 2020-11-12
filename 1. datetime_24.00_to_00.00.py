#!/usr/bin/env python
# coding: utf-8

# In[10]:
# XVWCO

from datetime import date
stringdata = '01-01-2020 17:00'


# In[28]:


# Change format to date time

#  datetime.strptime(date_string, format)

stringdata = '01-01-2020'
newdate = datetime.datetime.strptime(stringdata, '%d-%m-%Y')
print(newdate)
print("-------------")
print('Day:', newdate.day)
print('Month:', newdate.month)
print('Year:', newdate.year)


# In[29]:


# ESPAÑOL
# Cambiar de una cadena de texto a un tipo de dato fecha

#datetime.strptime(cadena_de_texto, formato_fecha)

cadenatexto = '01-01-2020'
nuevafecha = datetime.datetime.strptime(cadenatexto, '%d-%m-%Y')
print(nuevafecha)
print("-------------")
print('Day:', nuevafecha.day)
print('Month:', nuevafecha.month)
print('Year:', nuevafecha.year)


# In[30]:


# My time
x = datetime.datetime.now()
print(x)


# In[33]:


# Problems with format
stringdata2 = '01-01-2020 24:00'

newdate = datetime.datetime.strptime(stringdata2, '%d-%m-%Y %H:%M')
print(newdate)


# In[34]:


# Solution: Change 24:00 with 00:00

# Problems with format
stringdata2 = '01-01-2020 00:00'

newdate = datetime.datetime.strptime(stringdata2, '%d-%m-%Y %H:%M')
print(newdate)
