# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 14:27:28 2019

@author: amukher3
"""

import pandas as pd

df=pd.read_csv("C:/Users/amukher3/Downloads/screening_exercise_orders_v201810.csv")

df['order_count'] = df.customer_id.map(df.customer_id.value_counts())

#df['date'] = pd.to_datetime(df['date'])
#most_recent_date = df['date'].max()


df_prime=[]
most_recent_dates=[]
gender=[]


Unique_ids=list(set(df['customer_id']))

for i in range(len(Unique_ids)):
    
   df_prime= df.loc[df['customer_id']==Unique_ids[i]]
   
   df_prime['date'] = pd.to_datetime(df_prime['date'])
   most_recent_dates.append(str(df_prime['date'].max()))
   
   temp = list(df_prime['gender'])
   gender.append(temp[0])