import csv

columns = []
with open('character.csv','r',encoding='utf-8') as f: 
    reader = csv.reader(f)
    for row in reader:
        if columns:
            for i, value in enumerate(row):
                columns[i].append(value)
        else:
            # first row
            columns = [[value] for value in row]

# you now have a column-major 2D array of your file.
as_dict = {c[0] : c[1:] for c in columns}
ls = list(as_dict['可可蘿'])
print(as_dict['可可蘿'])