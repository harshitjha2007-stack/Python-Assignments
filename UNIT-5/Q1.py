filename = input("Enter the filename: ")

try:
    with open(filename, "r") as file:
        content = file.read()
        print(content)

except FileNotFoundError:
    print(f"Error: The file '{filename}' was not found.")
    
except PermissionError:
    print(f"Error: You do not have permission to read the file '{filename}'.")
