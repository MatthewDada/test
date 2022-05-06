print('Enter the number assigned to the operation you want to perform')
print('Addition = 1')
print('Subtraction = 2')
print('Multiplication = 3')
print('Division = 4')
print('Power = 5')
print('Modulus = 6')
operation = input('What operation do you want to perform? \n')

if operation == '5':
    input_3 = float(input('Enter the base number \n'))
    input_4 = float(input('Enter the power \n '))
    print(f'The power of {input_3} by {input_4} is {input_3 ** input_4}')
elif operation == '1' or operation == '2' or operation == '3' or operation == '4' or operation == '6':
    input_1 = float(input('Enter the first number \n'))
    input_2 = float(input('Enter the second number \n'))

    if operation == '1':
        print(f'The sum of {input_1} and {input_2} is {input_1 + input_2}')
    elif operation == '2':
        print(f'The difference between {input_1} and {input_2} is {input_1 - input_2}')
    elif operation == '3':
        print(f'The product of {input_1} and {input_2} is {input_1 * input_2}')
    elif operation == '4':
        print(f'The quotient of {input_1} and {input_2} is {input_1 / input_2}')
    elif operation == '6':
        print(f'The modulo of {input_1} by {input_2} is {input_1 % input_2}')
else:
    print('You must enter 1, 2, 3, 4, 5 or 6')
    operation = input('What operation do you want to perform? \n')
