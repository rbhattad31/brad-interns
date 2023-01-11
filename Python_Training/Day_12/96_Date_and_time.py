import pandas as pd
#from datetime import datetime
"""
data={'Date':['15-1-2012']}
df=pd.DataFrame(data)
df['Date']=pd.to_datetime(df['Date'])
print(df)
"""
"""
data={'Time':['9:20 PM']}
df=pd.DataFrame(data)
df['Time']=pd.to_datetime(df['Time'])
print(df)
"""
"""
from pytz import timezone
today=datetime.today()
timezones=['Asia/Kolkata']
for tzone in timezones:
  local_date=today.astimezone(timezone(tzone))
data={'Date':[local_date]}
df=pd.DataFrame(data)
print(df)
"""
"""
from datetime import date
today=date.today()
data={'Date':[today]}
df=pd.DataFrame(data)
print(df)
"""
"""
from datetime import date
data={'Date':['11-1-2023','12-1-2023','13-1-2023','14-1-2023']}
df=pd.DataFrame(data)
df['Date']=pd.to_datetime(df['Date'])
print(df)
"""
"""
from datetime import time
data={'Time':['9:20 AM','12:00 PM','2:00 PM','10:00 PM','1:00 AM','6:00 AM']}
df=pd.DataFrame(data)
df['Time']=pd.to_datetime(df['Time'])
print(df)
"""
"""
from datetime import time
from pytz import timezone
now=datetime.now()
timezones=['Asia/Kolkata']
for tzone in timezones:
  local_time=now.astimezone(timezone(tzone))
data={'Time':[local_time]}
df=pd.DataFrame(data)
print(df)
"""
