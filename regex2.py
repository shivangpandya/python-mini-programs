#Regex to find pattern where number is followed by a word
import re
print('Input a message here')
message=input()

xmasRegex = re.compile('\d+\s\w+')
xmasRegex.findall(message)
