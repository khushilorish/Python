import pandas as pd

data = {
    "Name": ['Arjun', 'Arun', 'Tarun', 'Ankur', 'Tanu', 'Manu'],
    "Age" : [20,32,21,35,37,31],
    "Salary": [70000, 40000, 41000, 50000, 60000, 88000],
    "Performance": [89,90,91,87,86,93],
    "City": ['Mumbai', 'Agra', 'Chennai', 'Goa', 'Meerut', 'Paris']
}

df = pd.DataFrame(data)

#selecting single columns
name = df['Name']
print(f'Name Column: \n{name}')

#selecting multiple columns
subset = df[["Name", "Salary"]]
print(f'\n\nSubset of data with names and salary: \n{subset}')


#filtering rows with salary > 50000
high_salary = df[df["Salary"]>50000]
print(f'\n\nEmployees whose Salary is greater than 50000: \n{high_salary}')

#filtering rows with 2 conditions
filter_row = df[(df["Salary"]>50000) & (df["Age"]>30)]
print(f'\n\nRows with Salary greater than 50k and age greater than 30: \n{filter_row}')