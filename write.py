file = open("sample.txt", "w")
file.write("Hello, this is my first file handling program.\n")
file.write("Python file write example.")
file.write("\nHere nishant have written this code.")
file.close()

print("Data written to file successfully")

file = open("sample.txt", "r")
content = file.read()
print(content)
file.close()
