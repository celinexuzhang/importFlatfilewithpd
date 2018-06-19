import pandas as pd
#make sure package "xlrd" installed
file_location='C:/Users/celin/OneDrive/Desktop/Learning/python/ImportandCleandatainPython1/battledeath.xlsx'
battledeath=pd.ExcelFile(file_location)
#figureout the sheets
print(battledeath.sheet_names)

# assign dataframe to single sheet

#sheet name, as a string
df1=battledeath.parse('2002')
#sheet index, as a float
df2 = battledeath.parse(0)
