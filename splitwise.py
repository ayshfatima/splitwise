a = {}
people = int(input("Enter the number of people: "))
for i in range(people):
    name = input(f"Enter the name of the person {i+1}: ")
    a[name] = 0  # Initialize each person's balance to zero

expenses = int(input("Enter the number of expenses: "))
for j in range(expenses):
    payer = input("Enter the name of the person who paid the amount: ")
    expense_name = input("Enter the expense name: ")
    amount = int(input("How much paid? "))
    splitter = int(input("Enter 1 for splitting equally among people or enter 2 for custom splitting: "))

    if splitter == 1:
        # Equal split
        share = amount / people
        for person in a:
            if person == payer:
                a[person] += amount - share
            else:
                a[person] -= share

    elif splitter == 2:
        # Custom split
        total_share = 0
        for person in a:
            share = float(input(f"Enter the share for {person}: "))
            total_share += share
            if person == payer:
                a[person] += amount - share
            else:
                a[person] -= share

print("\nBalances:")
for person, balance in a.items():
    if balance > 0:
        print(f"{person} is owed: ${balance:.2f}")
    elif balance < 0:
        print(f"{person} owes: ${-balance:.2f}")
    else:
        print(f"{person} is settled.")
