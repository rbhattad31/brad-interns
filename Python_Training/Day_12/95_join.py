import pandas as pd
exam_data1= {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
        'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
        'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
        'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
df1=pd.DataFrame(exam_data1)
#print(ndf1)
exam_data2= {'name': ['Ayra', 'Deepesh', 'Kishan', 'Javed', 'Elon', 'Chopra', 'Mohit', 'ashish', 'Kohli', 'Naman'],
        'score': [13, 10, 18, 15, 12, 24, 16, 12, 10, 14],
        'attempts': [1, 2, 2, 1, 3, 1, 2, 2, 1, 3],
        'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
df2=pd.DataFrame(exam_data2)
res=pd.concat([df1,df2])
print(res)