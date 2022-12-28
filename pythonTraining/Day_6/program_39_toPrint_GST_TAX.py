Original_price = 100
Net_price = 124.7
GST_amount = Net_price - Original_price

GST_percent = ((GST_amount * 100) / Original_price)
print("GST = ", end='')

print(round(GST_percent), end='')
print("%")