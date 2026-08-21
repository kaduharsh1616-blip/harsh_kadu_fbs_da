###TO CALCULATE TOTAL SALARY OF EMPLOYEE

## INPUT VALUE

basic=int(input('enter the value of basic'))
da = 10 / 100 * basic
ta = 12 /100 * basic
hra = 15/ 100 * basic

totalsalary = basic + da + ta + hra 
print("da:",da)
print("ta:",ta)
print("hra:",hra)
print('totalsalary:',totalsalary)
