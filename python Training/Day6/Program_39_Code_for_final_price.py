price_Artical = int(input("enter any value:"))
Gst = int(input("enter value of Gst:"))  # 5%,12%,15%,28%
gst_amount = (price_Artical * Gst) / 100
print("Amount of gst:", gst_amount)
Net_price = price_Artical - gst_amount
print("Final price of article is:", Net_price)
