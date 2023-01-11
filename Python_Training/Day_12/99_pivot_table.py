import pandas as pd
"""
df=pd.read_csv('vgsales.csv')
null_value=pd.isnull(df['Other_Sales'])
df1[null_value]
"""
import pandas as pd
import numpy as np
df=pd.read_csv('vgsales.csv')
df1=pd.pivot_table(df,index=['Rank','Year'],aggfunc=np.sum)
df1.head(50)
