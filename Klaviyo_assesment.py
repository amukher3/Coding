# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 14:27:28 2019

@author: amukher3
"""

import pandas as pd

df=pd.read_csv("C:/Users/amukher3/Downloads/screening_exercise_orders_v201810.csv")

df['order_count'] = df.customer_id.map(df.customer_id.value_counts())

df_prime=[]
most_recent_dates=[]
gender=[]
order_count=[]

#Customer IDs
Unique_ids=list(set(df['customer_id']))

for i in range(len(Unique_ids)):
    
   df_prime= df.loc[df['customer_id']==Unique_ids[i]]
   
   df_prime['date'] = pd.to_datetime(df_prime['date'])
   
   #most recent order date
   most_recent_dates.append(str(df_prime['date'].max()))
   
   df_Prime_to_list=df_prime['gender'].values[0]
   
   #Gender
   gender.append(df_Prime_to_list)
   
   #Order count
   tempOrderCount=df_prime['order_count'].values[0]
   order_count.append(tempOrderCount)
   
#Final DataFrame
Data_Frame=pd.DataFrame({'customer_id':Unique_ids,
                            'gender':gender,
                            'most_recent_order_date':most_recent_dates,
                            'order_count': order_count})
    
#sorting the data frame
Data_Frame=Data_Frame.sort_values('customer_id')    

#Displaying the first 10 rows
Data_Frame.head(10)

############################### Part B ########################################

from datetime import timedelta
import matplotlib.pyplot as plt

#Changing the string to date-time object(Time stamps)
df['date'] = pd.to_datetime(df['date'])

#Sorting the Time Stamps in ascending order
df=df.sort_values('date')

OrderSum=[]
NumSecWeek=604800
stPos=0
temp=0
tempPrime=0

for i in range(len(df['date'])-1):
    
    TimeDiff= df['date'][stPos]-df['date'][i+1]
    TimeDiffSecs= TimeDiff/ timedelta(seconds=1)
    
    if abs(TimeDiffSecs)<=NumSecWeek:
        temp=df['order_count'][i]
        tempPrime=temp+tempPrime
        
        
    else:
        
        OrderSum.append(tempPrime) 
        
        stPos=i        
        tempPrime=0
       
plt.plot(OrderSum)   

################################### Part C ####################################
import statistics

#For gender '0'
df_gender= df.loc[df['gender']==0]

GenVals=df_gender['value'].tolist()
meanVal_0=statistics.mean(GenVals)


#For gender '1'
df_gender= df.loc[df['gender']==1]

GenVals=df_gender['value'].tolist()
meanVal_1=statistics.mean(GenVals)



    