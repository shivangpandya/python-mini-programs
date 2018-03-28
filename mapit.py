import webbrowser,sys
import pyperclip
#Check if command line argumentd are passed
if len(sys.argv) > 1:
    ' '.join(sys.argv[1:]) #Converts in sinngle string
    address = ' '.join(sys.argv[1:])
else:
        address = pyperclip.paste()

webbrowser.open('https://www.google.co.in/maps/place/' +address)
