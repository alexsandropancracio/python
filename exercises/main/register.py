import os
import time

registrations = []

while True:
    os.system('cls')
    enter = input('Press Enter to begin.')
    if enter != '':
        print('\nIncorrect Alternative. Use the correct alternative to continue.')
        time.sleep(3)
        continue
    while True:
        os.system('cls')
        try:
            start = input('[1] Register People \n[2] View Register People \n[3] Remove Register People \n[4] Show Over 18s \n[5] Exit \nEnter one of the options: ')
            option = int(start)
        except ValueError:
            print('\nPlease enter only numbers according to the alternatives.')
            time.sleep(3)
            continue
        if option == 1:
            while True:
                os.system('cls')
                print('Press enter on any os the options to go back.')
                name = input('Enter a name: ')
                if name == '':
                    break
                age = None
                exit = False
                while age is None:
                    os.system('cls')
                    print('Press enter on any os the options to go back.')
                    print(f'Enter a name: {name.title()}')
                    try:
                        age = input('Enter an age: ')
                        if age == '':
                            exit = True
                            name = None
                            break
                        years = int(age)
                        if years <= 0:
                            print('Invalid age. Try again.')
                            time.sleep(2)
                            age = None
                            continue
                        registrations.append({'person': name.title(), 'age': years})
                        continue
                    except ValueError:
                        print('\nEnter only numbers to enter age. Try again.')
                        time.sleep(3)
                        age = None
                        continue
                if exit:
                    break
        if option == 2:
            while True:
                os.system('cls')
                if len(registrations) < 1:
                    print('No data recorded. Please register some to be able to view it.')
                    time.sleep(3.5)
                    break
                else:
                    for people in registrations:
                        print(f'Name: {people["person"]}, Age: {people["age"]}')
                    exit = input('\nPress Enter to go back.')
                    if exit == '':
                        break
                    else:
                        print('\nPress the correct alternative to retur. Try again.')
                        time.sleep(3)
                        continue
        if option == 3:
            while True:
                    os.system('cls')
                    if len(registrations) < 1:
                        print('No records found. Register the data to be removed. Try again.')
                        time.sleep(3)
                        break
                    else:                    
                        for x, people in enumerate(registrations):
                            print(f'[{x + 1}] Name: {people["person"]}, Age: {people["age"]}')
                        remove = input('\nChoose the registration to be removed according to the number(press Enter to go back): ')
                        if remove == '':
                            break
                        try:
                            deleted = int(remove) - 1
                            if deleted >= 0:
                                if deleted < len(registrations):
                                    turnedoff = registrations.pop(deleted)
                                    print(f'\n{turnedoff["person"]} successfully deleted!')
                                    time.sleep(3)
                                    continue
                                else:
                                    print('\nThe number is greater than the number os records to be removed. Please try again.')
                                    time.sleep(3.5)
                                    continue
                        except ValueError:
                            print('\nTo remove a registered data item, enter only numbers. Try again.')
                            time.sleep(3)
                            continue
        if option == 4:            
            while True:
                os.system('cls')
                if len(registrations) >= 1:
                    os.system('cls')
                    print('Registration for people over 18 yeares old are:')
                    for people in registrations:
                        if people['age'] >= 18:
                            print(f'Name {people["person"]}, Age: {people["age"]}')
                        exit = input('\nPres Enter to go back.')
                        if exit == '':
                            break
                        else:
                            print('\nPress the correct alternative to retur. Try again.')
                            time.sleep(3)
                            continue
                else:
                    print('No records found for people over 18. Register to be displayed.')
                    time.sleep(3)
                    break
        if option == 5:
            print('\nFinishing program.')
            time.sleep(3)
            print('Come back often!')
            time.sleep(1.5)
            break