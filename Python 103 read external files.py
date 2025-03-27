def read_and_modify_file():
    try:
        filename = input("Enter the filename to read: ")
        with open(filename, 'r') as file:
            content = file.readlines()
        modified_content = [line.upper() for line in content]
        new_filename = "modified_" + filename
        with open(new_filename, 'w') as new_file:
            new_file.writelines(modified_content)
        print(f"Modified file saved as {new_filename}")
    except FileNotFoundError:
        print("Error: File not found. Please check the filename and try again.")
    except IOError:
        print("Error: Could not read or write to the file.")
read_and_modify_file()
