# File Creation
with open("my_file.txt", "w") as file:
    file.write("This is line 1.\n")
    file.write("12345\n")
    file.write("Another line with some numbers: 98765\n")

# File Reading and Display
print("Contents of my_file.txt:")
with open("my_file.txt", "r") as file:
    for line in file:
        print(line.strip())

# File Appending
with open("my_file.txt", "a") as file:
    file.write("This is line 4 (appended).\n")
    file.write("67890\n")
    file.write("Final line appended with numbers: 54321\n")

# Error Handling
try:
    with open("non_existent_file.txt", "r") as file:
        for line in file:
            print(line.strip())
except FileNotFoundError:
    print("File not found.")
except PermissionError:
    print("Permission denied.")
finally:
    print("Error handling complete.")
