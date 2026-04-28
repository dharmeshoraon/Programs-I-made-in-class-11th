# Program to calculate income tax of an employee
basic=int(input("Enter the basic salary:"))
savings=int(input("Enter the total savings made:"))
if basic <=250000:
    tax=0
elif basic<=500000:
    if savings>150000:
        savings=150000
        tot_income=basic-savings-250000
        tax=tot_income*0.05
elif basic<=1000000:
    if savings>150000:
        savings=150000
        tot_income_5slab=500000-savings-250000
        tot_incomea_20slab=basic-500000
        tax=tot_income_5slab*0.05+tot_incomea_20slab*0.02
else:
    if savings>150000:
        savings=150000
        tot_income_5slab=500000-savings-250000
        tot_income_30slab=basic-1000000
        tax=tot_income_5slab*0.05+tot_income_30slab*0.03+100000
print("Total income tax to be paid",tax)