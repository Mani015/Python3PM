
# Regular expressions (regex) are patterns used to match and manipulate strings of text.
# They are widely used in programming and text processing to search, match, and manipulate text based on specific patterns.
#
# Here are some common components and syntax used in regular expressions:
#
# Literal Characters: Ordinary characters like letters, digits, and symbols represent themselves. For example, the regex pattern "cat" matches the string "cat" exactly.
#
# Metacharacters: These are special characters with reserved meanings in regex. Some common metacharacters include:
#
# . (dot): Matches any character except a newline.
# (asterisk): Matches zero or more occurrences of the preceding character or group.
# (plus): Matches one or more occurrences of the preceding character or group.
# ? (question mark): Matches zero or one occurrence of the preceding character or group.
# | (pipe): Acts as an OR operator, matches either the expression before or after it.
# ^ (caret): Matches the start of a line.
# $ (dollar): Matches the end of a line.
# \ (backslash): Escapes a metacharacter to be treated as a literal character.
# Character Classes: These are enclosed in square brackets and define a set of characters to match. For example, [aeiou] matches any vowel.
#
# Quantifiers: These specify the number of occurrences of a character or group. Some common quantifiers include:
#
# {n}: Matches exactly 'n' occurrences of the preceding character or group.
# {n,}: Matches at least 'n' occurrences of the preceding character or group.
# {n,m}: Matches between 'n' and 'm' occurrences of the preceding character or group.
# Anchors: These match specific positions in the input string. The commonly used anchors are:
#
# ^ (caret): Matches the start of the string.
# $ (dollar): Matches the end of the string.
# \b: Matches a word boundary.
# Groups and Capture: Parentheses ( ) are used to group and capture portions of a pattern. The captured groups can be used for further processing or extraction.
#
# These are just the basics of regular expressions. They can be much more complex and powerful, allowing for advanced text manipulation and pattern matching. Various programming languages and tools provide support for regular expressions, allowing you to apply them in your code to achieve specific text processing tasks.






# syntax: re.functionname(pattren,string,flags=0)
# match,search,findall,finditer,split,sub
#


# A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern.
#
# RegEx can be used to check if a string contains the specified search pattern.
stu = "The only way to do great work is to love what you do."
import re

# Match Object
# A Match Object is an object containing information about the search and the result.

m1 = re.match('The',stu)
# print(m1)
# <re.Match object; span=(0, 3), match='The'>


# Note: If there is no match, the value None will be returned, instead of the Match Object.
m2 = re.match('h',stu)
print(m2)
# None






