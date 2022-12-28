income = {'Anne' : 1111,
          'Bert' : 2222,
          'Cara' : 9999999}

print(min(income, key=income.get))
# Anne