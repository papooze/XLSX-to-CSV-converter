# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 15:29:35 2021

@author: Michael.Burman


Column names: 
Policy Number, LOB, Policy Effective Date, Effective Year, Claim Number, Loss Date, Report Date, 
Accident Description, Claim Status, Total Reserved, Total Paid, Total Incurred, Recovered,
Filename, Valuation Date
"""
import pandas as pd

#data = pd.read_excel("15-18 Zurich Loss Runs.xlsx")
#data.to_csv('test.csv', encoding="utf-8")
fname = input("What is the filename of the loss data?")

data = pd.read_csv("test.csv")

simple = ['Policy Number', 'LOB', 'Policy Effective Date', 'Effective Year', 'Claim Number', 'Loss Date', 'Report Date', 
'Accident Description', 'Claim Status', 'Total Reserved', 'Total Paid', 'Total Incurred', 'Recovered',
'Filename', 'Valuation Date']

expanded = ['Policy Number', 'LOB', 'Policy Effective Date', 'Effective Year', 'Claim Number', 'Loss Date', 'Report Date', 
'Accident Description','Accident State', 'Deductible/SIR', 'Net Paid', 'Deductible Paid', 'Paid Expense', 'Paid Indemnity', 
'Paid Medical', 'Deductible Reverse', 'Claim Reserve', 'Gross Incurred', 'Gross Paid', 'Net Incurred',
'Gross Incurred Limited to XX', 'Gross Incurred as XX', 'Loss Run', 'Valuation Date', 'Location']

def rename_cols(df, detailtype):
    renamed_cols = []
    for col_name in df.columns:
        resp = input("Should " + col_name + " be renamed? Type N or new name.")
        if resp != "N":
            renamed_cols.append(col_name)
    rename_dict = {}
    for preset in detailtype: 
        rename_dict[preset] = ""
    
        