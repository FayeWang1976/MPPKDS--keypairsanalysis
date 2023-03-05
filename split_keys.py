#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 29 21:26:26 2023

@author: wangzhehan
"""

import openpyxl
import pandas
import pandas as pd

if __name__ == '__main__':

    # list_cols = ["E_phi", "E_psi", "N_0", "N_n", "P", "Q"]
    # dict to store columns needs splitting and the number of splits
    dict_cols = {
        "f": 2,
        "h": 2,
        "E_phi": 2,
        "E_psi": 2,
        "N_0": 4,
        "N_n": 4,
        "P": 8,
        "Q": 8
    }

    # Read the original Excel file
    df = pandas.read_excel("key_list_for_matlab.xlsx")

    # Stores output data
    out = pandas.DataFrame()

    for i in dict_cols:
        # Replace the []; with spaces
        df[i] = df[i].str.replace("[", " ", regex=False)
        df[i] = df[i].str.replace("]", " ", regex=False)
        df[i] = df[i].str.replace(";", " ", regex=False)

        # Split based on one or more \s
        x = df[i].str.split(" +", expand=True)

        for j in range(dict_cols[i]):
            # Drop the first column (since in split the first column and last is "")
            out[f"{i}_{j}"] = x[j+1]

    # Rearrange the columns
    input=out.iloc[:,0:8]
    reinsertR=pd.concat([df['R_n'],df['R_0'],df['R_n'],df['R_0'],df['R_n'],df['R_0'],df['R_n'],df['R_0']],axis=1)
    input=pd.concat([input,input,reinsertR],axis=1)
    
    output=out.iloc[:,16:32]
    reinsertN=out.iloc[:,8:16]
    output=pd.concat([output,reinsertN],axis=1)

    out=pd.concat([input,output],axis=1)
    # Covert all to numeric
    out = out.apply(pd.to_numeric)

    out.to_excel("split_key_list_for_matlab.xlsx", index=False)
    out.to_csv("split_key_list_for_matlab.csv", index=False)

    print()
