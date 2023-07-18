gross_income = float(input("Enter the income: "))
no_of_dependent = int(input("Enter number of dependent: "))
taxes = gross_income-10000-(3000*no_of_dependent)
tax = taxes*0.20
print(tax)