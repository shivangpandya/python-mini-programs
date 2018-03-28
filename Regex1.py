#Regular expression to find occurence of sting in expression
import re

message = 'Call me whenever you get free at my number 201-659-0721 or at 201-809-0721'

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') #Prints first occurence,d stands for digit
mo = phoneNumRegex.search(message)
print(mo.group())

#To find all occurences

phoneNumRegex1 = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') #Prints all occurence
print(phoneNumRegex1.findall(message))



