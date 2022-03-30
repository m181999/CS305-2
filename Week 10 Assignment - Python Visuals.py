#!/usr/bin/env python
# coding: utf-8

# In[75]:


import plotly.graph_objects as go
import pandas as pd


# In[76]:


tslastockdf = pd.read_csv(
    "https://raw.githubusercontent.com/plotly/datasets/master/tesla-stock-price.csv")

tslastockdf.head()

tslastockdf.drop ('close', axis=1, inplace=True)
tslastockdf.drop ('high', axis=1, inplace=True)
tslastockdf.drop ('low', axis=1, inplace=True)
tslastockdf.drop ('volume', axis=1, inplace=True)
tslastockdf = tslastockdf.drop(index=0)


tslastockdf.dtypes

tslastockdf['date'] = pd.to_datetime(tslastockdf['date'], format='%Y/%m/%d')


# In[79]:


fig = go.Figure()

fig.add_trace(
    go.Scatter(x=list(tslastockdf.date), y=list(tslastockdf.open)))

fig.update_layout(
    title_text="Tesla Stock From 2015-2018"
)

#removed YTD - not current data - past data. 

fig.update_layout(
    xaxis=dict(
        rangeselector=dict(
            buttons=list([
                dict(count=1,
                     label="1m",
                     step="month",
                     stepmode="backward"),
                dict(count=6,
                     label="6m",
                     step="month",
                     stepmode="backward"),
                dict(count=1,
                     label="1y",
                     step="year",
                     stepmode="backward"),
                dict(step="all")
            ])
        ),
        rangeslider=dict(
            visible=True
        ),
        type="date"

    )
)
fig.update_layout(

)


# In[ ]:




