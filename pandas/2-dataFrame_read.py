import pandas as pd

#read data from csv file into a data
df1 = pd.read_csv(r"C:\Users\hp\Desktop\PYTHON-CORE\Python-core\pandas\datasets\1-sampleFile.csv", encoding="latin1")

print(df1)

#read data from json file into a data
df2 = pd.read_json(r"C:\Users\hp\Desktop\PYTHON-CORE\Python-core\pandas\datasets\3-sampleFile.json")

print(df2)

#read data from excel file into a data
df3 = pd.read_excel(r"C:\Users\hp\Desktop\PYTHON-CORE\Python-core\pandas\datasets\2-sampleFile.xlsx", engine="openpyxl")

print(df3)




data = {
    "Name": ['Arjun', 'Arun', 'Tarun', 'Ankur', 'Tanu', 'Manu'],
    "Age" : [20,22,21,25,30,31],
    "Salary": [30000, 40000, 41000, 50000, 60000, 44000],
    "Performance": [89,90,91,87,86,93],
    "City": ['Mumbai', 'Agra', 'Chennai', 'Goa', 'Meerut', 'Paris']
}

df1 = pd.DataFrame(data)


#read first 3 rows of df1 data
print("First 3 rows:")
print(df1.head(3)) #if no value passed by default it will show first 5 rows


#read last 3 rows of df1 data
print("\n\nLast 3 rows")
print(df1.tail(3)) #if no value passed by default it will show last 5 rows


#get information about the whole data
print("\n\nInfo method:")
print(df1.info())


#print Descriptive Statistics of Data
print("\n\nDescriptive statistics of data:")
print(df1.describe())


#print the shape of data
print(f'\nShape: {df1.shape}')

#print all the column's name
print(f'\ncolumns: {df1.columns}')