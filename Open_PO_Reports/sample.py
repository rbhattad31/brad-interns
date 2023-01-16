import pandas as pd
open_po_df = pd.read_excel("open PO.xlsx", skiprows=1)
print(open_po_df)

open_po_df["Order Date"] = pd.to_datetime(open_po_df["Order Date"], errors='coerce')
open_po_df["PO Date"] = pd.to_datetime(open_po_df["PO Date"], errors='coerce')

recent_audit_date = open_po_df["Order Date"].max()
print(recent_audit_date)
open_po_df["no of days"] = 0




for index in open_po_df.index:
    po_date = open_po_df.loc[index]["PO Date"]
    no_of_days = recent_audit_date - po_date
    print(no_of_days)
    open_po_df.at[index, 'no of days'] = no_of_days

# find last date of audit
    # date column , select most recent date
# create a new column - no.of.days
# for every row,
#   find no.days by last_date_of_audit - PO date value
#   assign the values to no.of days
open_po_df["PO Date"] = pd.to_datetime(open_po_df["PO Date"]).dt.strftime("%d-%m-%Y")
open_po_df["Order Date"] = pd.to_datetime(open_po_df["Order Date"]).dt.strftime("%d-%m-%Y")
print(open_po_df)

open_po_df.to_excel("open_po_output.xlsx")
# open_po_df = pd.DataFrame(columns=["Order Date"])
# quarters = pd.date_range(open_po_df['Order Date'].min(), open_po_df['Order Date'].max()+pd.tseries.offsets.QuarterEnd(), freq='Q')
# open_po_df['Q_date '] = quarters[quarters.searchsorted(open_po_df['Order Date'].values)]
# open_po_df.to_excel("open_po_output.xlsx")