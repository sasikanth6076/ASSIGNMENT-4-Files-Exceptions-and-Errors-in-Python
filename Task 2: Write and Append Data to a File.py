with open("sample.txt", "r+") as file:
    adding_data = file.write(input("Enter text to write to the file:"))
    print("Data successfully written to output.txt\n")


with open("sample.txt", "a") as file1:
    appending = file1.write(input("Enter additonal text to append: "))
    print("Data Successfully appended.")