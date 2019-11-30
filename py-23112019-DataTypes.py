#!/usr/bin/env python
# coding: utf-8

# In[3]:


import this


# In[3]:


5 + 8 # Operation
#Operators
    # +, - ,/ ,*, %, ** 
    # =, +=, -=, ?=, *=, %=
    # ==, >, <, >=, <=
# 5, 8 Oprands


# In[4]:


#complex operation
#PEMDAS
5 + 7 - 8 * (2/2) + 200


# In[9]:


a = 8 #shallow copy
b = 8
print (a)
print (b)
print (id(a))
print (id(b))


# In[10]:


a=True
type(a)


# In[11]:


a = "pakistan"
a*2


# In[13]:


'1'+'7'


# In[16]:


int("1") + int('1')
#type casting
#implicit casting
#explicit casting


# In[26]:


#index      0         1       2     3    
names  = ["Ali", "Hamza", "Junaid",200 ]
#index      -4       -3      -2     -1
print(type(names))
print(names)
print(names[-4])
print(names[0])


# In[36]:


#tuple value cannot be update
#index      0         1       2     3    
names  = ("Ali", "Hamza", "Junaid",200 )
#index      -4       -3      -2     -1
print(type(names))
#print names
print(names[-3])


# In[47]:


#set
#index      0         1       2     3    
names  = {"Ali", "Hamza", "Junaid",200,"Badar" }
#index      -4       -3      -2     -1
names = list(names)
#print(names[-3]) error
print(names[0])
print(type(names))


# In[56]:


data={
    #key: value
    'name':"Badar Yousaf",
    'fname': "M Yousaf",
    5 : "Pakistan",
    #['a']: True # list cannot be defined in datatype
    "a": [True, "Pakistan", 20,3.0]
}
data[5]
data['name']
data["a"]


# In[9]:


a="Badar Yousaf"
dir(a)


# In[11]:


a = "bAdarYouSAF"
a.upper()


# In[66]:


a = "bAdar YouSAF"
a.capitalize()


# In[72]:


a = "     bAdar YouSAF    "
print(len(a))
print(a.lstrip())
print(len(a.lstrip()))
print(a.rstrip())
print(len(a.rstrip()))


# In[80]:


b = "       badar    yousaf      "
b.split()


# In[ ]:





# In[83]:


b = "       badar    yousaf      "
b.split()
" ".join(b)


# In[85]:


a =  "we are pakistan we love our country"
a


# In[101]:


#list[start:end:step]
#tuple[start:end:step]
#string[start:end:step]
#a =  "we are pakistan we love our country"
print(a)
print(a[::])
print(a[::-1])
print(a[7:15:1])


# In[108]:


print(a.index("pakistan"))
a[a.index("pakistan"):15:1]


# In[111]:


a="890890asdas98080"
a.join([i for i in a if str.isnumeric(i)])


# In[115]:


#concatenation
card ="""
Bahria University Islamabad
name: Badar Yousaf
FName: M Yousaf

"""
print(card)


# In[150]:


#concatenation
name="badar"
fname="yousaf"
#uni="Bahria"
score=3
card ="""
Bahria University Islamabad
name: %s
FName: %s
score: %d
"""
print(card%(name,fname,score))


# In[125]:


#concatenation
name="badar"
fname="yousaf"
#uni="Bahria"
score=3
card =f"""
Bahria University Islamabad
name: {name}
FName: {fname}
score: {score}
"""
print(card)


# In[128]:


#concatenation
name="badar"
fname="yousaf"
#uni="Bahria"
score=3
card ="""
Bahria University Islamabad
name: {}
FName: {}
score: {}
"""
print(card.format(name,fname,score))


# In[130]:


#concatenation
name="badar"
fname="yousaf"
#uni="Bahria"
score=3
card ="""
Bahria University Islamabad
name: {a}
FName: {b}
score: {c}
"""
print(card.format(a=name,b=fname,c=score))


# In[133]:


#concatenation
name="badar"
fname="yousaf"
#uni="Bahria"
score=3
card ="""
Bahria University Islamabad
name: {2}
FName: {1}
score: {0}
"""
print(card.format(name,fname,score))


# In[135]:


"1" + '1'


# In[5]:


#concatenation
name="badar"
fname="yousaf"
score=3
print("Bahria university Islamabd \nStudent Name:" + name + " " + 
      "\nFather name: " + fname +
     "\nScore: "+ str(score))


# In[8]:


print(a)


# In[15]:


print(a.capitalize())


# In[22]:


s = "Hi This is Badar"
print(s.casefold())


# In[28]:


print(s.center(30))


# In[38]:


s="your name is badar"
print(s.encode())


# In[44]:


s="badaryousaf"
print(s.endswith("dar"))


# In[50]:


s="badar\tyousaf"
print(s.expandtabs(5))


# In[55]:


print(s.find("saf"))


# In[60]:


marks = 40
total=50
line = "My marks are {} out {}"
print(line.format(marks,total))


# In[63]:


print(line.index("marks"))


# In[67]:


s = "sdfas234234"
print(s.isalnum())
a="sdfsdfs"
print(a.isalpha())


# In[72]:


s="asd as# "
print(s.isprintable())


# In[75]:


s="    "
print(s.isspace())


# In[85]:


s="badar yousaf at piaic"
print(s.ljust(40))
print(s.rjust(40))


# In[89]:


print(s.zfill(30))


# In[96]:


x=18 
y=5
print(x%y)


# In[101]:


x=2
y=3
print(x**y)


# In[103]:


x=18 
y=5
print(x//y)


# In[106]:


x=5
y=5
print(x is not y)


# In[108]:


x=5
y=5
print(x is y)


# In[112]:


x=[5,4,5,6]
y=5
print(y not in x)
print(y  in x)


# In[ ]:




