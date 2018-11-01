
# coding: utf-8

# # 数据趋势拆解
# <liyuxia@baidu.com> 2018-11-01

# In[98]:


import pandas as pd
import numpy as np
from datetime import datetime
from statsmodels.tsa.seasonal import seasonal_decompose
import matplotlib.pylab as plt
import warnings
warnings.filterwarnings('ignore')

get_ipython().run_line_magic('matplotlib', 'inline')


# # 读数据

# In[127]:


def get_trend(s, fname):
    decomposition = seasonal_decompose(s)
    trend = decomposition.trend
    seasonal = decomposition.seasonal
    residual = decomposition.resid
    df = pd.DataFrame({'original': s.values,
                       'trend': trend.values,
                       'seasonal': seasonal.values,
                       'residual': residual.values},
                      index=s.index,
                      columns=['original', 'trend', 'seasonal', 'residual'])
    df.to_csv(fname, sep='\t')

    df[['trend', 'seasonal', 'residual']].sum(axis=1) -df['original']
    plt.figure();
    fig, ((ax1), (ax2), (ax3), (ax4)) = plt.subplots(4, 1, figsize=(9,6), sharex=True, sharey=False)

    ax1.plot(s, label='原始数据')
    ax2.plot(trend, label='趋势')
    ax3.plot(seasonal,label='季节性')
    ax4.plot(residual, label='残差')

    for ax in plt.gcf().get_axes():
        ax.legend(loc='upper left')
        
    return df


# In[125]:


df = pd.read_excel('./data/lisa_trend.xlsx')
df.set_index('week', inplace=True)
df.head()


# In[128]:


df_new = get_trend(df[2015], './Lisa/out_test.csv')


# In[129]:


df_new.head(40)

