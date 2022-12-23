price_article = int(input("enter any value:"))
GST = int(input("enter GST value:"))     # 5%,12%,18%,28%
GST_amount = (price_article * GST)/100
print("The gst amount is:", GST_amount)
Net_price = price_article - GST_amount
print("final price of the article is:", Net_price)
