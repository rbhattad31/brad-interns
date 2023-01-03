import re
import datetime
def change_date_format(dt):
    return re.sub(r'(\d{4})-(\d{1,2})-(\d{1,2})', '\\2-\\3-\\1', dt)

dt2 = "2022-12-26"
print("Original date in YYYY-MM-DD Format: ", dt2)
print("New date in DD-MM-YYYY Format: ", change_date_format(dt2))
