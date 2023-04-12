
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

path = 'https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv'
tips=pd.read_csv(path)

st.write(""" 
## Tips analysis
""")
st.write(""" 
### based on Seaborn standard dataset
""")

st.write("""Histogram of total bills""")
fig, ax = plt.subplots()
ax=sns.histplot(data=tips,x='total_bill',color='orange', edgecolor='yellow')
plt.xlabel('Total bill')
st.pyplot(fig)

st.write(""" Connection between total bill and tips """)
fig, ax = plt.subplots()
ax=sns.scatterplot(data=tips,x='total_bill',y='tip')
plt.xlabel('Total bill')
st.pyplot(fig)

st.write(""" Connection between total bill, tips and size """)
fig, ax = plt.subplots()
ax=sns.scatterplot(data=tips,x='total_bill',y='tip',size='size',c=tips['size'])
plt.xlabel('Total bill')
st.pyplot(fig)

st.write(""" Connection between days of week and total bill""")
fig, ax = plt.subplots()
mean_bill=tips.groupby('day')['total_bill'].mean().astype(int).sort_values().reset_index()
ax=sns.barplot(data=mean_bill,x='day',y='total_bill',palette='crest')
plt.title('Average bill per day')
plt.ylabel('Total bill')
for i in ax.containers:
    ax.bar_label(i,fontsize=9)
st.pyplot(fig)

st.write(""" Scatter of tips by day of the week paid by Male/Female """)
fig, ax = plt.subplots()
ax=sns.scatterplot(data=tips,x='tip',y='day',hue=tips['sex'],palette='colorblind');
plt.legend(bbox_to_anchor=(1.2,1),fontsize=7)
st.pyplot(fig)

st.write(""" 
Boxplot of daily bills split between Lunch and Dinner 
""")
fig, ax = plt.subplots()
ax=sns.boxplot(data=tips,y='total_bill',x='day',hue='time')
st.pyplot(fig)

z1=tips.loc[tips['time']=='Dinner','tip']
z2=tips.loc[tips['time']!='Dinner','tip']
st.write(""" 
Histogram of tips (Lunch and Dinner)
""")
fig, ax = plt.subplots()
plt.subplot(1, 2, 1)
sns.histplot(data=z1);
plt.title('Tips in Dinner');
plt.ylabel('USD');
plt.subplot(1, 2, 2)
sns.histplot(data=z2,color='r');
plt.title('Tips in Lunch');
plt.ylabel('USD');
st.pyplot(fig)

bool_sex1=tips['sex']=='Female'
bool_sex2=tips['sex']!='Female'
w=tips.loc[bool_sex1,['total_bill','tip','smoker']]
m=tips.loc[bool_sex2,['total_bill','tip','smoker']]
st.write(""" 
Scatter of tips and total bill (Male/Female + Smoker/Non-Smoker)
""")
fig, ax = plt.subplots()
plt.subplot(1, 2, 1)
sns.scatterplot(data=w,x='total_bill',y='tip',hue='smoker',legend=None);
plt.title('Tips from women');
plt.ylabel('Tips');
plt.subplot(1, 2, 2)
sns.scatterplot(data=m,x='total_bill',y='tip',hue='smoker');
plt.title('Tips from men');
plt.ylabel('Tips');
plt.legend(title='Smoker?',bbox_to_anchor=(1.05,1),fontsize=8);
st.pyplot(fig)

bool_men=tips['sex']=='Male'
new_1=tips.loc[bool_men,:]
new_1['%']=(new_1['tip']/new_1['total_bill'])*100
m_tips=new_1.groupby('day')['%'].mean().reset_index()


bool_women=tips['sex']=='Female'
new_2=tips.loc[bool_women,:]
new_2['%']=(new_2['tip']/new_2['total_bill'])*100
w_tips=new_2.groupby('day')['%'].mean().reset_index()

st.write(""" 
Average daily tips ***(percent of total bill)*** paid by Male/Female
""")

fig,ax=plt.subplots(figsize = (7,2), dpi = 200)
plt.subplot(1, 2, 1)
plt.xticks(rotation=60,fontsize=7)
plt.yticks(fontsize=5)
plt.xlabel('Day',fontsize=7)
a1=sns.barplot(data=m_tips,x='day',y='%',palette='crest');
plt.title('Tips from men',fontsize=7);
for container in a1.containers:
    a1.bar_label(container,label_type='center',fontsize=6)
  
plt.subplot(1, 2, 2)
plt.xticks(rotation=60,fontsize=7)
plt.xlabel('Day',fontsize=7)
plt.yticks(fontsize=5)
a2=sns.barplot(data=w_tips,x='day',y='%',palette='crest');
for container in a2.containers:
    a2.bar_label(container,label_type='center',fontsize=6)
plt.title('Tips from woman',fontsize=7);
st.pyplot(fig)