list0=[40,50,60,75]
list1=["S","M","L","XL"]
sum=0
from pizza_function import extra
from pizza_function import destination

age1=int(input("Enter age: "))
residentPriceinBsh1=20
residentPriceObSh2=60
while age1>=18:
    for tr in list1:
        sum+=list0[list1.index(tr)]
    tyap = input("Enter size: ")
    extra()
    destination()
    print(sum)
    customer = input("do you want to contnue? y/n ")
    if customer == 'n':
        break
    else:
        continue
else:
    print(" Soory you canot order!!")
