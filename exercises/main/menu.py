import os
import time

products = []

while True:
    os.system('cls')
    starting = input('Press Enter to begin.')
    if starting == '':
        while True:
                os.system('cls')
                try:
                    start = int(input('''[1] Register Products
[2] View Products
[3] Remove Products
[4] Exit
Select options: '''))
                except ValueError:
                    print()
                    print('Please, enter only numbres according to the options. Try again.')
                    time.sleep(3.5)
                    continue   
                if start == 1:
                    os.system('cls')
                    while True:
                        storing = input('Please enter a product(enter [0] to return): ')
                        products.append(storing)
                        if products == '0':
                            products.remove('0')
                            break
                elif start == 2:
                    if len(products) < 1:
                        print()
                        print('No products found, enter a product to be displayed.')
                        time.sleep(3.5)
                        continue
                    else:
                        while True:
                            os.system('cls')
                            for x in products:
                                
                                print(x)
                            print()
                            back = input('Type [0] to go back: ')
                            if back != '0':
                                print()
                                print('To go back, type the correct option')
                                time.sleep(3.5)
                                continue
                            else:
                                break
                elif start == 3:
                    while True:
                        os.system('cls')
                        if len(products) >= 1:
                            for y in products:
                                print(y)
                            print()
                            rem = input('Enter the name of the product you want to delete(enter [0] to go back): ')
                            if rem in products:
                                products.remove(rem)
                            elif rem == '0':
                                break
                            else:
                                print()
                                print('Enter the product name as it appears in the product list.')
                                time.sleep(3.5)
                        else:
                            os.system('cls')
                            print('There are no products to remove. Enter products so you can remove them.')
                            time.sleep(3.5)
                            break
                        
                elif start == 4:
                    print()
                    print('Thank you for choosing us! Come back soon.')
                    time.sleep(3)
                    break
                else:
                    print()
                    print('We did not identify the value entered, please try again.')
                    time.sleep(3.5)
                    continue
    else:
        print()
        print('Enter unidentified, to start, press Enter.')
        time.sleep(3.5)