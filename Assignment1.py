basic=float(input("basic pay of an employee: "))

HRA=basic*10/100
TA=basic*5/100
salary=basic+HRA+TA
Pro_tax=salary*2/100
final_salary=salary-Pro_tax
print("final salary after the deduction is",final_salary)

print("The basic pay is",basic,"with HRA",HRA,"with TA",TA,"Total salary",salary,"Deduction of professional tax",Pro_tax)
