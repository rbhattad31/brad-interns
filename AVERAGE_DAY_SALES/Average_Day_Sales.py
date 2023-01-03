import pandas as pd


def leap_year(year):
    bool_leap_year = False

    # divided by 100 means century year (ending with 00)
    # century year divided by 400 is leap year
    if (year % 400 == 0) and (year % 100 == 0):
        print("{0} is a leap year".format(year))
        bool_leap_year = True
    # not divided by 100 means not a century year
    # year divided by 4 is a leap year
    elif (year % 4 == 0) and (year % 100 != 0):
        print("{0} is a leap year".format(year))
        bool_leap_year = True
    # if not divided by both 400 (century year) and 4 (not century year)
    # year is not leap year
    else:
        print("{0} is not a leap year".format(year))
        bool_leap_year = False

    return bool_leap_year


def average_day_sales():
    # file path
    str_path = "sales register q1.xlsx"

    # read the Excel file  str_path
    sales_register_df = pd.read_excel(str_path, skiprows=4)
    print(sales_register_df)

    # creating a pivot table
    average_day_sales_pivot_df = pd.pivot_table(sales_register_df, index="Billing Date", values="Base Price in INR")
    print(average_day_sales_pivot_df)

    # reset index for having proper index for the dataframe and unsetting index column making usual column
    dataframe_pivot = average_day_sales_pivot_df.reset_index()
    print(dataframe_pivot)

    float_base_price_column_sum = dataframe_pivot["Base Price in INR"].sum()
    print(float_base_price_column_sum)

    # find quarter
        # create Month Column using Billing Date column
        # create year column using Billing Date Column
        # Get month unique values in a list from Month Column
        # Get year unique values in a list from Year column
        # quarter = None
        # Check if month column unique values list contains q1 columns then quarter = q1
            # q1_months = ['Apr', 'May', 'Jun']
            # q2_
            # q3_
            # q4_
            # if len(month_values_list) == 3:
                # for month in q1_months:
                    # if month in month_values_list:
                        # quarter = q1
                # for month in q2_months:
                    # if month in month_values_list:
                        # quarter = q2
                # for month in q3_months:
                    # if month in month_values_list:
                        # quarter = q3

                # for month in q4_months:
                    # if month in month_values_list:
                    # quarter = q4
            # else:
                # raise exception("sales register contains data of more than 3 months for a quarter")

            # if quarter == Q4:
                # year_unique_values_list = pd[year_column].unique.tolist()
                # year = year_unique_values_list[0]
                # find year whether it is leap or not

                # bool_leap_year = leap_year(year)
                # if bool_leap_year,
                    # int_days = 91
                # else
                    # int_days = 90
            # elif quarter == q1
                # days = 91
            # elif quarter == q2 or quarter == q3:
                # days = 92
            # else
                # pass
            # average = sum of base price column / days

            # create average column and assign with average

            # create variance column = None

            # apply variance formula for each row variance cell
            # df["Variance"] = df["col1"]-df["col2"]
            # create concentration column with None
            # assign values to concentration cells
            # float_variance_sum = dataframe_pivot["Variance"].sum()
            # df["Concentration"] = df["Varaince"]/varaince_total

    dataframe_pivot.to_excel("output.xlsx", sheet_name="Average day purchase sale", startrow=3)

