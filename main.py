name = input('What is your name? ')
print('Hello ' + name)
surname = input('What is your surname? ')
print('Hello ' + name + ' ' + surname)
birth_year = input('Enter your birth year: ')
age = 2023 - int(birth_year)
if 18 > age:
    input('You have to be 18+ to continue')
elif 0 > age or age > 100:
    input('Incorrect data')

else:
    input('Hi ' + name + ' ' + surname + ' ' + str(age) + ' years old')

while True:
    calc = input('Would you like to continue? yes/no ')

    if calc == 'yes':
        print('Calculator time')
        first_number = input('first number ')
        second_number = input('second number ')
        sum = float(first_number) + float(second_number)
        print('Sum: ' + str(sum))
    elif calc == 'no':
        print('bye :(((')
        break
    else:
        print('da ili net conch')
