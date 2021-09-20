"""
Created on Wed Sep  8 15:29:35 2021

@author: Michael.Burman


Column names: 
Policy Number, LOB, Policy Effective Date, Effective Year, Claim Number, Loss Date, Report Date, 
Accident Description, Claim Status, Total Reserved, Total Paid, Total Incurred, Recovered,
Filename, Valuation Date
"""
import pandas as pd

simple = ['Policy Number', 'LOB', 'Policy Effective Date', 'Effective Year', 'Claim Number', 'Loss Date', 'Report Date', 
'Accident Description', 'Claim Status', 'Total Reserved', 'Total Paid', 'Total Incurred', 'Recovered',
'Filename', 'Valuation Date']

expanded = ['Policy Number', 'LOB', 'Policy Effective Date', 'Effective Year', 'Claim Number', 'Loss Date', 'Report Date', 
'Accident Description','Accident State', 'Deductible/SIR', 'Net Paid', 'Deductible Paid', 'Paid Expense', 'Paid Indemnity', 
'Paid Medical', 'Deductible Reverse', 'Claim Reserve', 'Gross Incurred', 'Gross Paid', 'Net Incurred',
'Gross Incurred Limited to XX', 'Gross Incurred as XX', 'Loss Run', 'Valuation Date', 'Location']

def read_data():
    '''Returns a dataframe from a converted .xlsx->CSV as a pandas dataframe.'''
    data = pd.read_excel(input("What is the name of the file?")+".xlsx")
    #csv_name = input("What is the name of the desired .csv?")+".csv"
    #data.to_csv(csv_name, encoding="utf-8")
    #data = pd.read_csv(csv_name)
    return data

detailtype = input("Simple or Expanded loss data?").lower()

def rename_cols(df, detailtype):
    '''
    Inputs: 
    df: dataframe, pandas object
    detailtype: List of columns used for CSV output.
    
    Renames columns from inputted .xlsx and returns a dictionary with the new column names.
    '''
    renamed_cols = []
    #columns from csv that need to be renamed
    rename_dict = {}
    #dictionary for use in pd.df.rename
    for col_name in df.columns:
        resp = input("Should " + col_name + " be renamed? y/n: ").upper()
        if resp != "N":
            renamed_cols.append(col_name)
    for col_name in renamed_cols:
        rename_dict[col_name] = input("What should " + col_name + " be called?")
    df.rename(columns=rename_dict)
    return df

def new_csv(df):
    '''
    Inputs: 
    '''

df = read_data()
df = rename_cols(df, detailtype)
new_csv(df)
    
        