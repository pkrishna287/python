def calculator():
    operation = input('''
+ for addition
- for subtraction
* for multiplication
/ for division
% for reminder
// for exponent
Please type in the math operation: ''')
    number_1 = int(input('Please enter the first number: '))
    number_2 = int(input('Please enter the second number: '))
    if operation == '+':
        print('{} + {} = '.format(number_1, number_2))
        print(number_1 + number_2)
    elif operation == '-':
        print('{} - {} = '.format(number_1, number_2))
        print(number_1 - number_2)
    elif operation == '*':
        print('{} * {} = '.format(number_1, number_2))
        print(number_1 * number_2)
    elif operation == '/':
        print('{} / {} = '.format(number_1, number_2))
        print(number_1 / number_2)
    elif operation == '%':
        print('{} % {} = '.format(number_1, number_2))
        print(number_1 % number_2)
    elif operation == '//':
        print('{} // {} = '.format(number_1, number_2))
        print(number_1 // number_2)
    else:
        print('You have not given a valid operator') 
calculator()