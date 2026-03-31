import csv
row_count = 0
with open("Table.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        row_count +=1

print("Total number of rows:", row_count)