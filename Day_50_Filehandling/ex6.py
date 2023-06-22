

# You can return one line by using the readline() method


# By calling readline() two times, you can read the two first lines:
r1=open('file1.txt','r')

# r2 = r1.readline()
# for i in r2:
#     print(i)
# Love your enemies , and do good to them.
# r3 = r1.readline()
# print(r2)



for i in r1:
    print(i)

# Love your enemies , and do good to them.
#
#
#
# the pain you feel today will be strenght tomorrow
#
#
#
# kill them with success and burn them with your smile
#
#
#
#
#
# Do not judge a book by its cover
#
# The truth will set you free


# Advantages:
# Versatility: File handling in Python allows you to perform a wide range of operations, such as creating, reading, writing, appending, renaming, and deleting files.
# Flexibility: File handling in Python is highly flexible, as it allows you to work with different file types (e.g. text files, binary files, CSV files, etc.), and to perform different operations on files (e.g. read, write, append, etc.).
# User–friendly: Python provides a user-friendly interface for file handling, making it easy to create, read, and manipulate files.
# Cross-platform: Python file handling functions work across different platforms (e.g. Windows, Mac, Linux), allowing for seamless integration and compatibility.
# Disadvantages:
# Error-prone: File handling operations in Python can be prone to errors, especially if the code is not carefully written or if there are issues with the file system (e.g. file permissions, file locks, etc.).
# Security risks: File handling in Python can also pose security risks, especially if the program accepts user input that can be used to access or modify sensitive files on the system.
# Complexity: File handling in Python can be complex, especially when working with more advanced file formats or operations. Careful attention must be paid to the code to ensure that files are handled properly and securely.
# Performance: File handling operations in Python can be slower than other programming languages, especially when dealing with large files or performing complex operations.