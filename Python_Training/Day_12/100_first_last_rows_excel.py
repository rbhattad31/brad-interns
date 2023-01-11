import pandas as pd
df=pd.read_csv('vgsales.csv')
df1=pd.concat([df.head(10),df.tail(10)])
#df1.style.highlight_max(color='yellow').highlight_min(color='red').set_precision(2).hide_index()
#df1.style.background_gradient()
def wrong_year(val):
  color = 'red' if val < 1900 else 'black'
  return 'color: %s' % color
df1.style.applymap(wrong_year, subset=pd.IndexSlice[:, ['Year']])
