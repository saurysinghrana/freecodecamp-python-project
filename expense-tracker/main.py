def add_expense(expenses, amount, category):
    expenses.append({
        'amount': amount,
        'category': category
    })


def print_expenses(expenses):

    if not expenses:
        print('\nNo expenses recorded.')
        return

    for expense in expenses:
        print(f"Amount: {expense['amount']}, Category: {expense['category']}")


def total_expenses(expenses):
    return sum(map(lambda expense: expense['amount'], expenses))


def filter_expenses_by_category(expenses, category):
    return filter(
        lambda expense: expense['category'].lower() == category.lower(),
        expenses
    )


def main():

    expenses = []

    while True:

        print('\n=== Expense Tracker ===')
        print('1. Add an expense')
        print('2. List all expenses')
        print('3. Show total expenses')
        print('4. Filter expenses by category')
        print('5. Exit')

        choice = input('\nEnter your choice: ')

        if choice == '1':

            amount = float(input('Enter amount: '))
            category = input('Enter category: ')

            add_expense(expenses, amount, category)

            print('\nExpense added successfully.')

        elif choice == '2':

            print('\nAll Expenses:')
            print_expenses(expenses)

        elif choice == '3':

            print(f'\nTotal Expenses: {total_expenses(expenses)}')

        elif choice == '4':

            category = input('Enter category to filter: ')

            filtered_expenses = filter_expenses_by_category(
                expenses,
                category
            )

            print(f'\nExpenses for {category}:')
            print_expenses(filtered_expenses)

        elif choice == '5':

            print('\nExiting program...')
            break

        else:
            print('\nInvalid choice. Please try again.')


main()