def calc_main():
    methods = {'Add': '+', 'Subtract': '-', 'Multiply': '*', 'Divide': '/', 'Exit': 'Exiting'}
    total = 0

    while True:

        operation = input('Please choose an operation mode: \n'
                          'Add, subtract, multiply, divide, exit \n'
                          '=>').capitalize()
        if operation == 'Exit':
            print('Exiting...')
            break
        else:
            print(f'{total} {methods[operation]}')

        user_input = input('=> ')
        if user_input.isdigit() and int(user_input) >= 0:
            if operation == 'Add':
                total += int(user_input)

            elif operation == 'Subtract':
                total -= int(user_input)

            elif operation == 'Multiply':
                total *= int(user_input)

            elif operation == 'Divide':
                total /= int(user_input)

            continue
        else:
            print('Invalid input.')
            continue
    print(f'Answer: {total}')


calc_main()
