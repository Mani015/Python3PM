
# Types of File
# Text File: Text file usually we use to store character data. For example, test.txt
# Binary File: The binary files are used to store binary data such as images, video files, audio files, etc.

# "r" - Read - Default value. Opens a file for reading, error if the file does not exist
#
# "a" - Append - Opens a file for appending, creates the file if it does not exist
#
# "w" - Write - Opens a file for writing, creates the file if it does not exist
#
# "x" - Create - Creates the specified file, returns an error if the file exists


# File Mode	Meaning
# w		Create a new file for writing. If a file already exists, it truncates the file first. Use to create and write content into a new file.
# x		Open a file only for exclusive creation. If the file already exists, this operation fails.
# a		Open a file in the append mode and add new content at the end of the file.
# b		Create a binary file
# t		Create and open a file in a text mode



# syntax:open('filename','mode')

# f1 = open('file1.txt','x')
# print(f1)
# <_io.TextIOWrapper name='file1.txt' mode='x' encoding='cp1252'>



# f2 = open('C:\\Users\DELL\Desktop\Python Definations\\god.txt','x')
# print(f2)
# <_io.TextIOWrapper name='C:\\Users\\DELL\\Desktop\\Python Definations\\god.txt' mode='x' encoding='cp1252'>
