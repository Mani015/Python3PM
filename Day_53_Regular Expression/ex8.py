

# \W	Returns a match where the string DOES NOT contain any word characters

import re

W1 = 'My wife name $Ramya # @ % '

W2 = re.findall('\W',W1)
print(W2)
# [' ', ' ', ' ', '$', ' ', '#', ' ', '@', ' ', '%', ' ']


