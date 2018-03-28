#!python3

import re,pyperclip

#TODO : regex object for phone numbers
phonneRegex = re.compile(r'''

#differennt formats of phone numbers which can exist
# 415-555-0000 ,555-0000 , (415) 555-0000, 555-0000 ext 12345 , ext. 12345 , x12345)
(
((\d\d\d)|(\(\d\d\d\)))?        #area code(optional)
\s|-)                           #first sperator
\d\d\d                          #first 3 digits
-                               #spearator
\d\d\d\d                        #last 4 digits
(((ext(\.)?\s)|x)               #extensions word part (optional)
((\d{2,5}))?                    #extensions number part (optional)
)
''',re.VERBOSE)





#TODO :  regex object for email address

emailRegex = re.compile(r'''
#differennt formats of email which can exist
# something.+_thing@(\d{2,5}))?.com

[a-zA-Z0-9_.+]+     #name part
@                   # @symbol
[a-zA-Z0-9_.+]+     # domain name part



''',re.VERBOSE)

#TODO : Get text of clipboard

text = pyperclip.paste()

#TODO : Extract email and phone from this text

extractedPhone = phoneRegex.findall(text)
extractedEmail = emaiRegex.findall(text)

allPhoneNumbers = []
for phoneNumber in extractedPhone:
        allPhoneNumbers.append(phoneNumber[0])



#TODO: Copy the extracted phone and email to clipboard
'\n'.join(allPhoneNumbers)+ '\n' + '\n'.join(extractedEmail)
pyperclip.copy(results)



