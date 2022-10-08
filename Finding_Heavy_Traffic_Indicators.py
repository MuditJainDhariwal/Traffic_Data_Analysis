#!/usr/bin/env python
# coding: utf-8

# # Finding Heavy Traffic Indicators
# 
# The project is about analysing traffic data on a dataset of I-94 interstate highway. The goal is to determine a few likelihoods of heavy traffic on the highways.

# In[1]:


import pandas as pd

traffic = pd.read_csv('Metro_Interstate_Traffic_Volume.csv')
print(traffic.head(5))
print("\n")
print(traffic.tail(5))


# In[2]:


traffic.info()


# In[5]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

traffic['traffic_volume'].hist()
plt.show()
traffic['traffic_volume'].describe()


# In[7]:


traffic['date_time'] = pd.to_datetime(traffic['date_time'])
traffic['date_time'].head(10)


# In[24]:


daytime_data = traffic[traffic['date_time'].dt.hour.between(7,18)]
nighttime_data = traffic[~traffic['date_time'].dt.hour.between(7,18)]


# In[20]:



daytime_data.shape


# In[22]:



nighttime_data.shape


# In[32]:


plt.figure(figsize=(10,5))
plt.subplot(1,2,1)
daytime_data['traffic_volume'].hist()
plt.title("Daytime Traffic Volume")
plt.xlabel('Traffic Volume')
plt.ylabel('Frequency')
plt.xlim([0,8000])
plt.ylim([0,8000])

plt.subplot(1,2,2)
nighttime_data['traffic_volume'].hist()
plt.title("Nightime Traffic Volume")
plt.xlabel('Traffic Volume')
plt.ylabel('Frequency')
plt.xlim([0,8000])
plt.ylim([0,8000])

plt.show()


# In[34]:


daytime_data['traffic_volume'].describe()


# In[35]:


nighttime_data['traffic_volume'].describe()


# In[39]:


daytime_data['month'] = daytime_data['date_time'].dt.month
by_month = daytime_data.groupby('month').mean()
by_month['traffic_volume']


# In[40]:


by_month['traffic_volume'].plot()
plt.show()


# In[42]:


daytime_data['dayofweek'] = daytime_data['date_time'].dt.dayofweek
by_dayofweek = daytime_data.groupby('dayofweek').mean()
# 0 is Monday, 6 is Sunday

by_dayofweek['traffic_volume'].plot()
plt.show()


# In[43]:


daytime_data['hour'] = daytime_data['date_time'].dt.hour
business_days = daytime_data[daytime_data['dayofweek'] <= 4]
weekends = daytime_data[daytime_data['dayofweek'] > 4]

by_hour_business = business_days.groupby('hour').mean()
by_hour_weekends = weekends.groupby('hour').mean()

print(by_hour_business['traffic_volume'])
print(by_hour_weekends['traffic_volume'])


# In[46]:


plt.figure(figsize=(12,5))
plt.subplot(1,2,1)
by_hour_business['traffic_volume'].plot()
plt.title('Traffic on Business Days')
plt.xlim([5,20])
plt.ylim([0,8000])

plt.subplot(1,2,2)
by_hour_weekends['traffic_volume'].plot()
plt.title('Traffic on Weekends Days')
plt.xlim([5,20])
plt.ylim([0,8000])

plt.show()


# In[50]:


daytime_data.corr()['traffic_volume']


# In[51]:


plt.scatter(x=daytime_data['dayofweek'], y=daytime_data['traffic_volume'])
plt.show()


# In[53]:


by_weather_main = daytime_data.groupby('weather_main').mean()
by_weather_description = daytime_data.groupby('weather_description').mean()


# In[55]:


by_weather_main['traffic_volume'].plot.barh()


# In[56]:


by_weather_description['traffic_volume']


# In[61]:


by_weather_description['traffic_volume'].plot.barh(figsize=(7,10))
plt.show()


# In[ ]:




