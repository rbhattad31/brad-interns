import pandas as pd
exam_data  = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
        'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
        'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
        'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
df=pd.DataFrame(exam_data)
df1=df.iloc[0:len(df['name']),0:1]
print(df1)
print('\n')
print(df1.size)
print('\n')
df2=df.iloc[0:4,0:2]
print(df2)
print('\n')
print(df2.size)
