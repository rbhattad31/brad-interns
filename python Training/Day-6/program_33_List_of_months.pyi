Pip install fiscalyear
import datetime
import fiscalyear
from dateutil import relativedelta
from fiscalyear import *

fiscalyear.setup_fiscal_calendar (start_month=7)

first_fiscal_year = 2022
current_fiscal_year = FiscalDate.today().fiscal_year
number_of_loops = current_fiscal_year - first_fiscal_year + 1

for x in range(0, number_of_loops):fy = FiscalYear(first_fiscal_year + x)
    fystart = fy.start.strftime("%b %d %Y")
    fyend = fy.end.strftime("%b %d %Y")
    print(f"The fiscal year {fy.fiscal_year} runs from {fystart} to {fyend}")
    d = datetime.datetime(fy.start.year, fy.start.month,fy.start.day)

 for m in range(0, 12):
    next_month_start = d + relativedelta.relativedelta(months=m, day=1)
    next_month_end = d + relativedelta.relativedelta(months=m, day=31)
    print(f"{next_month_start.strftime('%b %d, %Y')} to {next_month_end.strftime('%b %d, %Y')}")


