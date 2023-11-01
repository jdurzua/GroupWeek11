def budgeting():
budget = int(input("What is your current budget: "))
expense = int(input("What are your expenses: "))
if budget > expense:
    print("You have low expenses")
else:
    print("Your budget is low  and cant cover your expenses")