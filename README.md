# 📝 Read and Modify File - Python Script

This Python script reads the contents of a text file, modifies the content (by converting it to uppercase as an example), and writes the modified content to a **new file**.

> This project demonstrates proper use of **file handling** and **error handling** in Python.

---

## 🚀 Features

- 📂 Reads any text-based file from user input  
- 🔄 Modifies the content (uppercase conversion as demo)  
- 📝 Writes the result into a new file  
- ⚠️ Handles common errors gracefully (e.g. file not found, permission denied)  

---

## 📁 How It Works

1. Asks the user to enter the filename (e.g., `data.txt`)  
2. Reads the content from that file  
3. Converts the content to uppercase  
4. Saves the new content to `modified_<filename>` (e.g., `modified_data.txt`)  
5. Handles errors like missing files or permission issues  

---

## 🧪 Example

Suppose you have a file called `example.txt` containing:

-Hello world.
This is a test.

## Running the script:
python read_and_modify_file.py

## Input:
Enter the filename to read from include the file type:
example.txt
## Output:
✅ Modified content written to:
modified_example.txt
## Content of modified_example.txt:
HELLO WORLD.
THIS IS A TEST.
