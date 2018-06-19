import pandas as pd
#make sure package "xlrd" installed

#Ex1: load excel file and using parse method
file_location='C:/Users/celin/OneDrive/Desktop/Learning/python/ImportandCleandatainPython1/battledeath.xlsx'
battledeath=pd.ExcelFile(file_location)
#figureout the sheets
print(battledeath.sheet_names)

# assign dataframe to single sheet

#sheet name, as a string
df1=battledeath.parse('2002')
#sheet index, as a float
df2 = battledeath.parse(0)

#print df1 and df2 head

print(df1.head())

print(df2.head())


#Ex2:  you'll use the method parse(). This time, however, you'll add the additional arguments skiprows, names and parse_cols. These skip rows, name the columns and designate which columns to parse, respectively. All these arguments can be assigned to lists containing the specific row numbers, strings and column numbers, as appropriate.
#Parse the first sheet by index. In doing so, skip the first row of data and name the columns 'Country' and 'AAM due to War (2002)' using the argument names. The values passed to skiprows and names all need to be of type list.
# Parse the first sheet and rename the columns: df1
df1 = battledeath.parse(0, skiprows=[0], names=['Country', 'AAM due to War (2002)'])

# Print the head of the DataFrame df1
print(df1.head())



#Parse the second sheet by index. In doing so, parse only the first column with the parse_cols parameter, skip the first row and rename the column 'Country'. The argument passed to parse_cols also needs to be of type list.
# Parse the first column of the second sheet and rename the column: df2
df2 = battledeath.parse(1, parse_cols=[0], skiprows=[0], names=['Country','AAM due to War (2004)'])

# Print the head of the DataFrame df2
print(df2.head())