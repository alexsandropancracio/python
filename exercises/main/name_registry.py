import os
import time

names = []

while True:
    os.system('cls')
    name = input('Enter a name(to show the names entered, type "exit"): ')
    if name == 'exit':
        break
    elif name == '':
        print()
        print('This field cannot be left blank, please enter a name.')
        time.sleep(3.5)
    else:
        names.append(name)

os.system('cls')
print('The names entered are: ')
for x in names:
    print(x)
