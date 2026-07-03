import os

try:
    # Create and write to a file
    file = open("sample.txt", "w")
    file.write("Welcome to Alfido Tech Internship")
    file.close()

    print("File created successfully.")

    # Read the file
    file = open("sample.txt", "r")
    data = file.read()
    file.close()

    print("File Content:")
    print(data)

    # Rename the file
    os.rename("sample.txt", "new_sample.txt")
    print("File renamed successfully.")

except FileNotFoundError:
    print("File not found.")

except Exception as e:
    print("Error:", e)
