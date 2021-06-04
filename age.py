driving = input('Have you dirved before?')
if driving != 'y' and driving != 'n':
    print('You can only type y or n')
    raise SystemExit

age = input('What is your age?')
age = int(age)

if driving == 'y':
    if age >= 18:
        print('You pass')
    else:
        print('Why do you have a driver license?')
elif driving == 'n':
    if age >= 18:
        print('why')
    else:
        print('you may go to take the test in 18')