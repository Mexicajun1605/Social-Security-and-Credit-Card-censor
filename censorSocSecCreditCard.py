#Soc Sec and Credit Card Censurer

import pyperclip, re

soSecRegex = re.compile(r"""
    (\d{3})+ #First three digits
    (\s|-)?        #separator
    (\d{2})+           #Second 2 digits
    (\s|-)         #separator
    (\d{4})+           #Last four digits
""", re.VERBOSE)

creditCardRegex = re.compile(r"""
    (\d{4})     #a pattern of 4 numbers and then a space
    (\s)?
    (\d{4})
    (\s)?
    (\d{4})
    (\s)?
    (\d{4})
""", re.VERBOSE)

#Getting the text to search and censor from the clipboard
text = str(pyperclip.paste())

#This string will be filled with our censored text
matches = ''

#This loop defines matches as our text with Social Security numbers censored
for soSec in soSecRegex.findall(text):
    soSec = soSecRegex.sub('CENSORED', text)
    matches += soSec
#This loop takes the previous result and searches for the
#Credit Card numbers in the string and censors those second
for card in creditCardRegex.findall(matches):
    matches = creditCardRegex.sub('CENSORED', matches)
    


#As long as the string is greater than 0, we get the following, easily 
#copied to the clipboard
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('')
    print('Copied to clipboard')
    print(matches)
else: 
    print('No Social Security numbers or Credit Cards were found.')