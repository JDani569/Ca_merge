import pandas as pd
import numpy as np
import openpyxl

# df1 =  pd.read_excel("July'25\CA OMNI_1st July_Validation file.xlsx")
# df2= pd.read_excel("July'25\CA OMNI_2nd July_Validation file.xlsx")
# df3 =  pd.read_excel(r"July'25\CA OMNI_3rd July_Validation file.xlsx")
# df4 = pd.read_excel("July'25\CA OMNI_4th July_Validation file.xlsx")
# df5=  pd.read_excel("July'25\CA OMNI_7th July_Validation file.xlsx")
# df6 = pd.read_excel("July'25\CA OMNI_8th July_Validation file.xlsx")
# df7 = pd.read_excel("July'25\CA OMNI_10th July_Validation file.xlsx")
# df8=pd.read_excel("July'25\CA OMNI_11th July_Validation file.xlsx")
# df9 = pd.read_excel("July'25\CA OMNI_18 Jul_Validation file.xlsx")
# df10 = pd.read_excel("July'25\CA OMNI_21st July_Validation file.xlsx")
# df11 = pd.read_excel("July'25\CA OMNI_22ND July_Validation file.xlsx")
# df12 = pd.read_excel("July'25\CA OMNI_23rd July_Validation file.xlsx")
# df13 = pd.read_excel(r"July'25\CA OMNI_24 Jul_Validation file.xlsx")
# df14 = pd.read_excel("July'25\CA OMNI_25th July_Validation file.xlsx")
# df15 = pd.read_excel("July'25\CA OMNI_28th July_Validation file.xlsx")
# df16 = pd.read_excel("July'25\CA OMNI_29th July_Validation file.xlsx")
# df17 = pd.read_excel("July'25\CA OMNI_30th July_Validation file.xlsx")
# df18 = pd.read_excel("July'25\CA OMNI_31st July_Validation file.xlsx")

df1 = pd.read_excel("August'25\CA OMNI_1st_Aug_Validation file.xlsx")
df2 = pd.read_excel("August'25\CA OMNI_4th_Aug_Validation file.xlsx")
df3 = pd.read_excel("August'25\CA OMNI_5th_Aug_Validation file_latest.xlsx")
df4 = pd.read_excel("August'25\CA OMNI_5th_Aug_Validation file.xlsx")
df5 = pd.read_excel("DFF.xlsx")


df_merged = pd.concat([df1, df2], ignore_index=True)

DF = pd.concat([df_merged, df3], ignore_index=True)

DFF = pd.concat([DF, df4], ignore_index=True)

DFF_August = pd.concat([df5, DFF], ignore_index=True)

# DFF2 = pd.concat([DFF,df5], ignore_index=True)

# DFF3 = pd.concat([DFF2,df6], ignore_index=True)

# DFF4 = pd.concat([DFF3,df7], ignore_index=True)

# DFF5 = pd.concat([DFF4,df8], ignore_index=True)

# DFF6 = pd.concat([DFF5,df9], ignore_index=True)

# DFF7 = pd.concat([DFF6,df10], ignore_index=True)

# DFF8 = pd.concat([DFF7,df11], ignore_index=True)

# DFF9 = pd.concat([DFF8,df12], ignore_index=True)

# DFF10 = pd.concat([DFF9,df13], ignore_index=True)

# DFF11 = pd.concat([DFF10,df14], ignore_index=True)

# DFF12 = pd.concat([DFF11,df15], ignore_index=True)

# DFF13 = pd.concat([DFF12,df16], ignore_index=True)

# DFF14 = pd.concat([DFF13,df17], ignore_index=True)

# DFF_main = pd.concat([DFF14,df18], ignore_index=True)

# DFF_main = pd.concat([DFF15,df19], ignore_index=True)


# List of columns
desired_columns = [
    "Codes",
    "Processing Group Description",
    "Best External Description - Current",
    "Retailer SKU - Current",
    "Predicted Barcode - Current",
    "URL - Current",
    "#CA LOC PRODUCT CLASS",
    "Error (Yes/No)",
    "Comments",
    "User Profile",
    "Creation/Movement",
    "Current Nielsen Item ID",
]


# DFF_August1 = DFF_August[
#     (DFF_August['Error (Yes/No)'] == 'Yes') &
#     (DFF_August['Comments'].str.startswith('#CA LOC'))
# ]


# print(DFF_August1[['Error (Yes/No)', 'Comments']])


# DFF_August_ = pd.DataFrame
DFF_August_ = DFF_August[desired_columns]
# print(DFF_August_.columns)
DFF_August.to_excel("DFF_august_.xlsx", index=False)
