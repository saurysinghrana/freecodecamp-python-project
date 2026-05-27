from bisection import square_root_bisection


def main():

    print('=== Square Root Finder using Bisection Method ===')

    while True:

        try:
            number = float(input('\nEnter a number: '))

            result = square_root_bisection(number)

            print(f'\nApproximate square root of {number} is: {result}')

        except ValueError as error:
            print(f'\nError: {error}')

        choice = input('\nDo you want to continue? (y/n): ').lower()

        if choice != 'y':
            print('\nExiting program...')
            break


main()