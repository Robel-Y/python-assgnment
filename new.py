def read_and_modify_file():
    try:
        # Ask user for the file name
        filename = input("Enter the filename to read from include the file type: ")

        # Try to open the file for reading
        with open(filename, 'r') as file:
            content = file.read()

        # Modify the content (convert to uppercase for demo)
        modified_content = content.upper()

        # Create a new file and write the modified content
        new_filename = "modified_" + filename
        with open(new_filename, 'w') as new_file:
            new_file.write(modified_content)

        print(f"✅ Modified content written to: {new_filename}")

    except FileNotFoundError:
        print("❌ Error: File not found. Please check the filename.")
    except PermissionError:
        print("❌ Error: Permission denied to read the file.")
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")

# Run the function
read_and_modify_file()
