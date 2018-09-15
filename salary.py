"""Salary details
Riza Marjadi"""

def salaryDetails(employee, salary, sales):
    pay = .07 * sales + salary
    fed = pay*.18
    retire = .1 * (pay - fed)
    sst = .06 * (pay - fed)
    takehome = pay - fed -  retire - sst
    
    print('\nSalary details for: ' + employee + '\n')
    print('Salary'.ljust(60,'.') + '$ ' + "{:,.2f}".format(salary).rjust(11))
    print('Sales'.ljust(60,'.') + '$ ' + "{:,.2f}".format(sales).rjust(11))
    print('Commission @ 7% of sales'.ljust(60,'.') + '$ ' + "{:,.2f}".format(.07 * sales).rjust(11))
    print('Gross income'.ljust(60,'.') + '$ ' + "{:,.2f}".format(pay).rjust(11))
    print('Federal income tax @ 18%'.ljust(60,'.') + '$ ' + "{:,.2f}".format(fed).rjust(11))
    print('Retirement @ 10% after tax'.ljust(60,'.') + '$ ' + "{:,.2f}".format(retire).rjust(11))
    print('Social security tax @ 6% after tax'.ljust(60,'.') + '$ ' + "{:,.2f}".format(sst).rjust(11))
    print('-' * 74)
    print('Take home pay (after tax, retirement, and social security)'.ljust(60,'.') + '$ ' + "{:,.2f}".format(takehome).rjust(11))

employee = input('Employee name: ')
salary = float(input('Salary amount: $'))
sales = float(input('Monthly sales: $'))

salaryDetails(employee, salary, sales)

