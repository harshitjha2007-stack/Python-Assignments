
file = open("Table.csv", "w")
file.write("Name, Age, City\n")
file.write("Alice, 30, New York\n")
file.write("Bob, 25, Los Angeles\n")
file.close()

file = open("Table.csv", "r")
content = file.read()
print(content)
file.close()