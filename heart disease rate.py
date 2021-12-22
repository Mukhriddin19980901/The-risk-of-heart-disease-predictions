#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import torch
import os
import glob


# In[2]:


data= np.loadtxt(r"C:/Users/USER/datasets2021/heart.csv",delimiter=',',dtype=np.float32)  
data_x = torch.from_numpy(data[:305,:13])
data_y = torch.from_numpy(data[:305,[13]])


# In[6]:


class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(13,11)
        self.linear2 = torch.nn.Linear(11,9)
        self.linear3 = torch.nn.Linear(9,7)
        self.linear4 = torch.nn.Linear(7,5)
        self.linear5 = torch.nn.Linear(5,3)
        self.linear6 = torch.nn.Linear(3,1)
        self.sigmoid = torch.nn.Sigmoid()
    def forward(self,x):
        x = self.linear1(x)
        x = self.linear2(x)
        x = self.linear3(x)
        x = self.linear4(x)
        x = self.linear5(x)
        x = self.linear6(x)
        y_pred = torch.sigmoid(x)
        return y_pred
model = Model()


# In[11]:


criteria = torch.nn.BCELoss(reduction = "mean")
optimizer = torch.optim.Adam(model.parameters(),lr = 0.01)
for epoch in range(50000+1):
    y_bash = model(data_x)
    xato = criteria(y_bash,data_y)
    if epoch % 1000 == 0:
        print(f"Epoch : {epoch} : {xato.item()}")
    optimizer.zero_grad()
    xato.backward()
    optimizer.step()
print(f"Epoch : {epoch} : {xato.item()}")


# In[32]:


x_test = torch.Tensor([40,0,2,110,270,0,1,165,0,1.3,0,2,3])
print(model(x_test))
print(model(x_test)>0.5)
y_test = torch.Tensor([60,0,2,176,210,0,1,145,0,0.3,0,2,3])
print(model(y_test))
print(model(y_test)>0.5)


# In[ ]:





# In[ ]:




