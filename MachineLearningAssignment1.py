#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Question1#
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]


# In[2]:


ages


# In[3]:


ages.sort()#the sort funtion is  built in function used to sort the elements of the list#
ages


# In[4]:


print(min(ages))#the min is used to find the minimum element of the list


# In[5]:


print(max(ages))#the max is used to find the maximum element of the list


# In[6]:


ages.append(min(ages))#the append function is used to add data to the the list by calculating the minimum  age as argument#
ages.append(max(ages))#the append function is used to add data to the the list by calculating the maximum  age as argument#
ages


# In[7]:


import numpy as npy #this is to import the numpy package#


# In[9]:


npy.median(ages)#The median is built in function used to calculate the median of the list data#


# In[11]:


npy.average(ages)# the average is built in function used to calculate the average of the list data#


# In[12]:


ages_range_value=range(min(ages),max(ages)) #the range function is used to find ranges of given list#
ages_range_value


# In[13]:


#Question2#
dog={} #Dictionaries are optimized to retrieve values when the key is known#
dog['name']='sambo'#created dictionary with dog name#
dog['color']='white'#created dictionary with dog color#
dog['breed']='pitbull'#created dictionary with dog breed#
dog['legs']='four'#created dictionary with dog legs#
dog['age']='eight moths'#created dictionary with dog age#
dog


# In[14]:


student={} #created dictionary with name student#
student['first_name']='siva'#added first_name to student dictionary#
student['last_name']='reddy'#added last_name to student dictionary#
student['gender']='Male'#added gender to student dictionary#
student['age']=26 #added first age to student dictionary#
student['marital_status']='single'#added marital_status to student dictionary#
student['skills']=['Java Programmer','python programmer']#added skills to student dictionary#
student['city']='Kurnool'#added city to student dictionary#
student['address']='kallapari'#added address to student dictionary#
student


# In[15]:


len(student) # length function is used find the length of dictionary#


# In[16]:


print(student['skills']) # print student skills#
print(type(student['skills']))# print the Type of student skills#


# In[17]:


student['skills'].append('C++ Programmer') #adding another more skill to skills list#
student


# In[18]:


student.keys() #we can access the keys using keys() method#


# In[19]:


student.values() #we can access the Values using keys() method#


# In[20]:


#Question3#
sister=('Aparna','Reddy')# The tuple is added with the values#
brother=('Venkatesh','Reddy')
print(sister)
print(brother)


# In[21]:


siblings=sister+brother #added siblings to tuple#
siblings


# In[22]:


len(siblings) #length is a bulit in  function used to find  length of  the tuple#


# In[23]:


family_members=siblings+('Yella','Uma')# Modify the siblings tuple and add the name of your father and mother and assign it to
family_members


# In[43]:


#Question4#
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]


# In[44]:


len(it_companies)#The length function is used find the length of set#


# In[45]:


it_companies.add('Twitter')#The twitter is added by using add function#
it_companies


# In[46]:


it_companies.update(['HCL','Wipro'])#the update method is used to update the set#.
it_companies


# In[47]:


it_companies.remove('HCL')#The remove method is remove the HCL#

it_companies


# In[48]:


A.union(B)#The union function is used to combine two sets#


# In[49]:


A.intersection(B)#The Intersection function is used to find common of two sets#


# In[50]:


A.issubset(B) #The issubset to find the  whether the A is subset of B #


# In[51]:


A.isdisjoint(B)#The issubset to find the  whether the A is isdisjoint of B #


# In[52]:


A.union(B) and B.union(A)#The and operation is used to find the union of two sets#


# In[53]:


A.union(B) and B.union(A)


# In[54]:


A.symmetric_difference(B)#Here, I found the symmetric difference between A and B.


# In[55]:


del A #Here, I have deleted sets completely.
del B


# In[56]:


age_set=set(age)#Here, I Converted the ages to a set and compare the length of the list and the set.
age_set


# In[57]:


#Question5#
radius=input('Enter radius : ')#to find the area of circle
radius=int(radius)
_area_of_circle_=(3.14)*(radius**2)
_area_of_circle_


# In[58]:


radius=input('Enter radius : ')#to find the circumference of circle
radius=int(radius)
_circum_of_circle_=2*3.14*radius
_circum_of_circle_


# In[59]:


#Question6#
l1="I am a teacher and I love to inspire and teach people"#the split methods and set to get the unique words
list_1=l1.split(' ')
set_1=set(list_1)
set_1
len(set_1)


# In[60]:


#Question7#
print('Name    Age    Country   City')#the tab escape sequence to get the following lines.


print('Asabeneh  250   Finlan   Helsinki')


# In[61]:


#Question8#
radius=10 #area of circle
area=3.14*radius**2
print('The area of circle with radius',radius,'is',area,'meter square')


# In[62]:


#Question9#
num_list=[] # program to convert weights from kgs to lbs.  
weights_kgs=[]
count=int(input('Enter no.of elements :'))
for i in range(0,count):
    num_list.append(int(input()))
for i in num_list:
    weights_kgs.append(i*0.45359237)#conversion formula
weights_kgs


# In[ ]:




