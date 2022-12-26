import re
def change_date_format(dt):
        return re.sub(r'(\d{4})-(\d{1,2})-(\d{1,2})', '\\3-\\2-\\1', dt)
dt1 = "2000-07-12"
print("Original date in YYY-MM-DD Format: ", dt1)
print("New date in DD-MM-YYYY Format: ", change_date_format(dt1))
