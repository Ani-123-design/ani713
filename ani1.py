#!/usr/bin/env python
# coding: utf-8

# In[64]:


import pandas as pd
x=pd.read_csv(r"C:\Users\Administrator\Downloads\422ceab9-b775-4f4a-8a04-066006bf204b_83d04ac6-cb74-4a96-a06a-e0d5442aa126_transactions.csv")
y=pd.read_csv(r"C:\Users\Administrator\Downloads\419f8355-6271-44cc-a20b-fea8bd241428_83d04ac6-cb74-4a96-a06a-e0d5442aa126_orders.csv")
z=pd.read_csv(r"C:\Users\Administrator\Downloads\156c0733-d225-4b76-a984-3ed5e19eb16d_83d04ac6-cb74-4a96-a06a-e0d5442aa126_customers.csv")
(x)


# In[65]:


y


# In[66]:


z


# In[67]:


x.isna().sum().sum()


# In[68]:


y.isna().sum().sum()


# In[69]:


z.isna().sum().sum()


# In[70]:


x.isna().sum()


# In[71]:


y.isna().sum()


# In[72]:


z.isna().sum()


# In[73]:


x["payment_type"]


# In[74]:


x["payment_type"].fillna("None",inplace=True)


# In[75]:


x["payment_type"]


# In[76]:


y[["ship_mode","order_approved_at","order_delivered_carrier_date","order_delivered_customer_date"]]


# In[82]:


y["ship_mode"].fillna("None",inplace=True)


# In[83]:


y["ship_mode"].head(100)


# In[84]:


y["order_approved_at"].fillna(0,inplace=True)


# In[85]:


y["order_delivered_carrier_date"].fillna(0,inplace=True)


# In[86]:


y["order_delivered_customer_date"].fillna(0,inplace=True)


# In[87]:


x.isna().sum().sum()


# In[88]:


y.isna().sum().sum()


# In[89]:


y3=pd.merge(x,y,left_on='order_id',right_on='order_id',how='left')
y3


# In[91]:


y4=pd.merge(y3,z,left_on="customer_id",right_on="customer_id")
y4


# In[95]:


y5=y4[y4["sales"]>150]
y5


# In[96]:


y5["order_id"]


# In[103]:


y6=y5["customer_name"].unique()
y6


# In[104]:


pd.DataFrame(y6)


# In[ ]:




