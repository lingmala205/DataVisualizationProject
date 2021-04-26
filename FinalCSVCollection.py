#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np


# In[3]:


kaggle1 = pd.read_csv("https://raw.githubusercontent.com/lingmala205/DataVisualizationProject/main/Kaggle1.csv")
kaggle2 = pd.read_csv("https://raw.githubusercontent.com/lingmala205/DataVisualizationProject/main/Kaggle2.csv")
kaggle3 = pd.read_csv("https://raw.githubusercontent.com/lingmala205/DataVisualizationProject/main/Kaggle3.csv")
kaggle4 = pd.read_csv("https://raw.githubusercontent.com/lingmala205/DataVisualizationProject/main/Kaggle4.csv")
kaggle5 = pd.read_csv("https://raw.githubusercontent.com/lingmala205/DataVisualizationProject/main/Kaggle5.csv")
kaggle6 = pd.read_csv("https://raw.githubusercontent.com/lingmala205/DataVisualizationProject/main/Kaggle6.csv")
kaggle7 = pd.read_csv("https://raw.githubusercontent.com/lingmala205/DataVisualizationProject/main/Kaggle7.csv")
kaggle8 = pd.read_csv("https://raw.githubusercontent.com/lingmala205/DataVisualizationProject/main/Kaggle8.csv")
kaggle9 = pd.read_csv("https://raw.githubusercontent.com/lingmala205/DataVisualizationProject/main/Kaggle9.csv")


# In[4]:


df1= kaggle1[154935:158163]                           # Alabama
df2= kaggle1.loc[kaggle1['County'] == 'Maricopa']     # Arizona
df3= kaggle1.loc[kaggle1['County'] == 'Pulaski']      # Arkansas
df4= kaggle1.loc[kaggle1['County'] == 'Los Angeles']  # California
df5= kaggle4.loc[kaggle4['County'] == 'Denver']       # Colorado
df6= kaggle4.loc[kaggle4['County'] == 'Fairfield']    # Connecticut
df7= kaggle3.loc[kaggle3['County'] == 'New Castle']   # Delaware
df8= kaggle4.loc[kaggle4['County'] == 'Miami-Dade']   # Florida
df9= kaggle3.loc[kaggle3['County'] == 'Wake']         # North Carolina
df10=kaggle3.loc[kaggle3['County'] == 'Ada']          # Idaho
df11=kaggle1.loc[kaggle1['County'] == 'Cook']         # Illinois
df12=kaggle4[417960:421379]                           # Indiana
df13=kaggle1.loc[kaggle1['County'] == 'Polk']         # Iowa
df14=kaggle5[68962:71463]                             # Kansas
df15=kaggle4[636847:640620]                           # Kentucky
df16=kaggle1[9119:12475]                              # Louisiana
df17=kaggle1[257445:260859]                           # Maine
df18=kaggle4.loc[kaggle4['County'] == 'Middlesex']    # Massachusetts
df19=kaggle4.loc[kaggle4['County'] == 'Wayne']        # Michigan
df20=kaggle1.loc[kaggle1['County'] == 'Hennepin']     # Minnesota
df21=kaggle8.loc[kaggle8['County'] == 'Hinds']        # Mississippi
df22=kaggle1.loc[kaggle1['County'] == 'Cooper']       # Missouri
df23=kaggle7.loc[kaggle7['County'] == 'Yellowstone']  # Montana
df24=kaggle3[87418:90758]                             # Nebraska
df25=kaggle1.loc[kaggle1['County'] == 'Clark']        # Nevada
df26=kaggle5.loc[kaggle5['County'] == 'Hillsborough'] # New Hampshire
df27=kaggle6.loc[kaggle6['County'] == 'Bergen']       # New Jersey
df28=kaggle2.loc[kaggle2['County'] == 'Bernalillo']   # New Mexico
df29=kaggle1.loc[kaggle1['City'] == 'New York']       # New York
df30=kaggle6.loc[kaggle6['County'] == 'Cass']         # North Dakota      
df31=kaggle2[388615:392070]                           # Ohio
df32=kaggle5.loc[kaggle5['County'] == 'Oklahoma']     # Oklahoma
df33=kaggle1.loc[kaggle1['County'] == 'Multnomah']    # Oregon
df34=kaggle2.loc[kaggle2['County'] == 'Philadelphia'] # Pennsylvania
df35=kaggle7.loc[kaggle7['County'] == 'Providence']   # Rhode Island
df36=kaggle4.loc[kaggle4['County'] == 'Greenville']   # South Carolina
df37=kaggle6.loc[kaggle6['County'] == 'Minnehaha']    # South Dakota
df38=kaggle6.loc[kaggle6['County'] == 'Shelby']       # Tennessee
df39=kaggle2.loc[kaggle2['County'] == 'Harris']       # Texas
df40=kaggle3.loc[kaggle3['County'] == 'Salt Lake']    # Utah
df41=kaggle5.loc[kaggle5['County'] == 'Chittenden']   # Vermont
df42=kaggle8[529904:532993]                           # Virginia
df43=kaggle4.loc[kaggle4['County'] == 'King']         # Washington
df44=kaggle5.loc[kaggle5['County'] == 'Kanawha']      # West Virginia
df45=kaggle1.loc[kaggle1['County'] == 'Milwaukee']    # Wisconsin
df46=kaggle1[303284:306166]                           # Wyoming
df47=kaggle1.loc[kaggle1['County'] == 'Fayette']      # Georgia
df48=kaggle1[737737:740244]                           # Maryland


# In[5]:


dfPart1=df1.append(df2)
dfPart2=dfPart1.append(df3)
dfPart3=dfPart2.append(df4)
dfPart4=dfPart3.append(df5)
dfPart5=dfPart4.append(df6)
dfPart6=dfPart5.append(df7)
dfPart7=dfPart6.append(df8)
dfPart8=dfPart7.append(df9)
dfPart9=dfPart8.append(df10)
dfPart10=dfPart9.append(df11)
dfPart11=dfPart10.append(df12)
dfPart12=dfPart11.append(df13)
dfPart13=dfPart12.append(df14)
dfPart14=dfPart13.append(df15)
dfPart15=dfPart14.append(df16)
dfPart16=dfPart15.append(df17)
dfPart17=dfPart16.append(df18)
dfPart18=dfPart17.append(df19)
dfPart19=dfPart18.append(df20)
dfPart20=dfPart19.append(df21)
dfPart21=dfPart20.append(df22)
dfPart22=dfPart21.append(df23)
dfPart23=dfPart22.append(df24)
dfPart24=dfPart23.append(df25)
dfPart25=dfPart24.append(df26)
dfPart26=dfPart25.append(df27)
dfPart27=dfPart26.append(df28)
dfPart28=dfPart27.append(df29)
dfPart29=dfPart28.append(df30)
dfPart30=dfPart29.append(df31)
dfPart31=dfPart30.append(df32)
dfPart32=dfPart31.append(df33)
dfPart33=dfPart32.append(df34)
dfPart34=dfPart33.append(df35)
dfPart35=dfPart34.append(df36)
dfPart36=dfPart35.append(df37)
dfPart37=dfPart36.append(df38)
dfPart38=dfPart37.append(df39)
dfPart39=dfPart38.append(df40)
dfPart40=dfPart39.append(df41)
dfPart41=dfPart40.append(df42)
dfPart42=dfPart41.append(df43)
dfPart43=dfPart42.append(df44)
dfPart44=dfPart43.append(df45)
dfPart45=dfPart44.append(df46)
dfPart46=dfPart45.append(df47)
dfPart47=dfPart46.append(df48)


# In[6]:


dfPart47.to_csv("FinalCollectedData.csv")


# In[ ]:





# In[ ]:




