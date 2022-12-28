df['As Quarter'] = df['Date'].dt.to_period('Q-MAR')
print(df)