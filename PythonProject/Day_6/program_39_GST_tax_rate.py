price = int(input("Enter the value"))
gst = int(input("Enter the GST value"))  # 5%, 12%, #18%
gst_amount = (price*gst)/100
print("gst amount is ", gst_amount)
net_price = price-gst_amount
print("final price is ", net_price)

