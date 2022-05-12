#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pymongo


# In[2]:


from pymongo import MongoClient
client = MongoClient("mongodb://localhost:27017/")


# In[59]:


db.list_collection_names()


# In[25]:


mydb=client['Employee']


# In[26]:


information=mydb.employeeinformation


# In[27]:


record={
      "name":"santosh",
       "phone_no":8431703346,
        "email":"santosh@gmail.com"
}


# In[28]:


information.insert_one(record)


# In[29]:


db=client['Telephone']


# In[30]:


details=db.telephonedirectory


# In[32]:


record=[{

      "name": "akshay",
      "mob_no": 7869587561,
      "place": "ankali",
      "email": "aksahy25@gmail.com"
},

{
     "name": "manisha",
     "mob_no": 7019458321,
     "place": "kadapur",
     "email": "manu28@gmail.com"
},
{
     "name": "santosh",
     "mob_no": 8431607010,
     "place": "kadapur",
     "email": "santosh28@gmail.com"
},
{
     "name": "priya",
     "mob_no": 8431704456,
     "place": "pune",
     "email": "priya24@gmail.com"
},
{
     "name": "anisha",
     "mob_no": 7849585610,
     "place": "sangli",
     "email": "anisha22@gmail.com"

},
{
     "name": "anil",
     "mob_no": 7849581058,
     "place": "kadapur", 
     "email": "anil22@gmail.com"

}
]


# In[34]:


details.insert_many(record)


# In[36]:


details.find_one()


# In[38]:


details.find()


# In[39]:


doc=details.find().sort("name",-1)
for x in doc:
    print(x)


# In[41]:


doc=details.find().sort("place",-1)
for x in doc:
    print(x)


# In[42]:


doc={"place":"ankali"}
details.delete_one(doc)


# In[43]:


doc=details.find().sort("place",-1)
for x in doc:
    print(x)


# In[44]:


doc={"place":"sangli"}

newdoc={"$set":{"place":"Ashta"}}
details.update_one(doc,newdoc)
for x in details.find():
    print(x)


# In[45]:


doc={"place":{"$regex":"^k"}}
newdoc={"$set":{"name":"Rahul"}}
x=details.update_many(doc,newdoc)
print(x.modified_count,"documents updated.")


# In[46]:


myresult=details.find().limit(5)
for x in myresult:
    print(x)


# CRUD Operation

# In[52]:


record={
      "name":"Rutuja",
       "mob_no":8431334645,
       "place":"sangli",
       "email":"rutuja7@gmailcom"
}


# In[53]:


details.insert_one(record)


# In[54]:


details.find_one({"name":"Rutuja"})


# In[55]:


details.update_one({"name":"Rahul"},{"$set":{"place":"belgaum"}})


# In[57]:


details.delete_one({"name":"Rahul"})


# In[58]:


details.find_one({"name":"Rahul"})


# In[61]:


myresult=details.find().limit(5)
for x in myresult:
    print(x)


# In[ ]:




