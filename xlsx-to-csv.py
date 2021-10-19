"""
Created on Wed Sep  8 15:29:35 2021

@author: Michael.Burman


Column names: 
Policy Number, LOB, Policy Effective Date, Effective Year, Claim Number, Loss Date, Report Date, 
Accident Description, Claim Status, Total Reserved, Total Paid, Total Incurred, Recovered,
Filename, Valuation Date
"""
import pandas as pd
import numpy as np
import datetime as date

hrow = int(input("On which row do the headers begin? (Number only)"))-1
hcol = input("On which column does the data begin? (Letter)").upper()


simple = ['Policy Number', 'LOB', 'Policy Effective Date', 'Effective Year', 'Claim Number', 'Loss Date', 'Report Date', 
'Accident Description', 'Claim Status', 'Total Reserved', 'Total Paid', 'Total Incurred', 'Recovered',
'Filename', 'Valuation Date']

expanded = ['Policy Number', 'LOB', 'Policy Effective Date', 'Effective Year', 'Claim Number', 'Loss Date', 'Report Date', 
'Accident Description','Accident State', 'Deductible/SIR', 'Net Paid', 'Deductible Paid', 'Paid Expense', 'Paid Indemnity', 
'Paid Medical', 'Deductible Reverse', 'Claim Reserve', 'Gross Incurred', 'Gross Paid', 'Net Incurred',
'Gross Incurred Limited to XX', 'Gross Incurred as XX', 'Loss Run', 'Valuation Date', 'Location']

def read_data():
    '''Returns a dataframe from a converted .xlsx->CSV as a pandas dataframe.'''
    data = pd.ExcelFile(input("What is the name of the file?")+".xlsx")
    #csv_name = input("What is the name of the desired .csv?")+".csv"
    #data.to_csv(csv_name, encoding="utf-8")
    #data = pd.read_csv(csv_name)
    if len(data.sheet_names) > 1: 
        print("Warning: This Excel file has multiple sheets. There are "+len(data.sheet_names)+" in the Excel file.")
    return data

detailtype = input("Simple or Expanded loss data? (TYPE 'S' OR 'E'. ").lower()

def merge_sheets(data):
    '''
    Inputs: 
    data: Excel sheet as a pandas object
    
    Organizes sheet names from the inputted excel spreadsheet then concatenates them into single dataframe.
    '''
    dflist = []
    tab_names = data.sheet_names
    if len(tab_names) > 1:
        for tab in tab_names:
            df = data.parse(sheetname=tab, skiprows=hrow) #parses data sheet and adds it to a list for concatenation
            dflist.append(df)
        df = pd.concat(dflist)
    else: 
        df = data.parse(skiprows=hrow)
    print("------------------------------------------------------------------")
    print(df.info())
    return df

def extract_cols(df):
    '''
    Inputs: 
    df: Pandas dataframe
    detailtype: Inputted strirng determining which columns are going to be utilized

    Takes dataframe columns, creates a new dataframe, and joins the old dataframe to the new one, only taking the needed columns.
    '''
    grabbed_cols = []
    while True:
        grabbed_col = input("Name exact column you would like to grab(type 'break' to exit): ")
        if grabbed_col == "break":
            break
        else:
            grabbed_cols.append(grabbed_col)
    new_df = pd.DataFrame()
    for col in grabbed_cols:
        new_df[col] = df[col]
    return new_df


def extract_policy_year(df):
    '''Input:
    df: Formatted new dataframe extracted from old spreadsheet.
    This function reads the date of loss, and uses the effective date to generate the policy year for the loss run.'''
    loss_date_col_name = str(input("What is the name of the Loss Date column?"))
    df[loss_date_col_name] = pd.to_datetime(df[loss_date_col_name])
    df['day_of_year_of_loss'] = df[loss_date_col_name].dt.dayofyear
    df['day_of_year_of_policy']= (pd.to_datetime(arg=str(input("What's the policy year month and day? (mm-dd):  ")+'-2000'), infer_datetime_format=True)).dayofyear#placeholder year
    df['Policy_Year'] = np.where((df['day_of_year_of_loss'] >= df['day_of_year_of_policy']), (df[loss_date_col_name].dt.year),  df[loss_date_col_name].dt.year-1)
    df = df.drop('day_of_year_of_loss', 1) #Drop day of year columns
    df = df.drop('day_of_year_of_policy' , 1)
    return df

def merge_financials(df):
    '''Input:
    df: Dataframe with condition that it NEEDS to have its financial amounts merged (i.e. needs total paid, total incurred, total reserve, etc.)
    This function takes these extra financial columns and merges them for ease of transition to summary.'''
    grabbed_cols = []
    if (input("Do we need to merge for total incurred? (Y/N): ")) == "Y":
        while True: #column population loop
            grabbed_col = input("Name exact column you would like to grab for TOTAL INCURRED (type 'break' to exit): ")
            if grabbed_col == "break":
                break
            else:
                grabbed_cols.append(grabbed_col)
        df['Total Incurred'] = df[grabbed_cols].sum(axis=1)

    if (input("Do we need to merge for total paid? (Y/N): ")) == "Y":
        grabbed_cols = []
        while True: #column population loop
            grabbed_col = input("Name exact column you would like to grab for TOTAL PAID (type 'break' to exit): ")
            if grabbed_col == "break":
                break
            else:
                grabbed_cols.append(grabbed_col)
        df['Total Paid'] = df[grabbed_cols].sum(axis=1)

    if (input("Do we need to merge for total reserve? (Y/N): ")) == "Y":
        grabbed_cols = []
        while True: #column population loop
            grabbed_col = input("Name exact column you would like to grab for TOTAL RESERVE (type 'break' to exit): ")
            if grabbed_col == "break":
                break
            else:
                grabbed_cols.append(grabbed_col)
        df['Total Reserve'] = df[grabbed_cols].sum(axis=1)
    return df

df = read_data()
df = merge_sheets(df)
df = extract_cols(df)
if input("Do you need to extract policy year? (Y/N): ") == "Y":
    df = extract_policy_year(df)
print(df.head(5))
print("-------------------------------------------------------------------")
if input("Do we have all combined necessary financial info from Loss Run? (Incurred, Paid, Reserve, Recovery): ") == "Y":
    df = merge_financials(df)
print(df.head(5))
