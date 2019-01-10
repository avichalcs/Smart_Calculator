import sys
sys.path.append('/module1/')
import module1
from module1.calci import * 
print(responses[0])
print(responses[1])
print("Note-> Don't write anything with comma")
while True:
    print()
    text= input("Enter operation\n")
    for word in text.split(' '):
        if word.upper() in operations.keys():
            try:
                m=extract_numbers_from_text(text)
                r=operations[word.upper()](m[0],m[1])
                print(r)
            except:
                print("Something went wrong. Please retry!!")
            finally:
                break
        elif word.upper() in commands.keys():
            commands[word.upper()]()
            break
    else:
        sorry()
