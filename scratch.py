"""
Problem: Print out user-provided text
Target Users: testers
Interface: Command line
Functional Requirements:  Prompt for user input
												Process input and respond
Testing: Editor test and then execute separately
Maintainer: philhatt@mac.com
"""

# Text string above is initial Python docstring
team
# Welcome message

print ("Python input program (c) 2012")

while True:
    reply = raw_input('Enter text ')   # If Python 3 raw_input is just input
    if reply == 'stop': break
    try:
        num = int(reply)
    except:
        print(reply)
    else:
        print(num ** 2)
    print('done')
