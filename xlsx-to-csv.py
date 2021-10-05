"""
Created on Wed Sep  8 15:29:35 2021

@author: Michael.Burman


Column names: 
Policy Number, LOB, Policy Effective Date, Effective Year, Claim Number, Loss Date, Report Date, 
Accident Description, Claim Status, Total Reserved, Total Paid, Total Incurred, Recovered,
Filename, Valuation Date
"""
print("hello")
import pandas as pd

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
            dataframes.append(df)
        df = pd.concat(dflist)
    else: 
        df = data.parse(skiprows=hrow)
    print("------------------------------------------------------------------")
    print(df.info())
    return df

def extract_cols(df, detailtype):
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
    new_df = pd.dataframe
    for col in grabbed_cols:
        new_df[col] = df[col]
    return new_df

df = read_data()
df = mergedata(df, detailtype)
df =  
    
        