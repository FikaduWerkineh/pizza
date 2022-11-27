list0=[40,50,60,75]
list1=["S","M","L","XL"]
sum=0
def extra():
    global sum
    extraslice = input("do you want to extra slices y/n")
    if extraslice == "y":
        amountExtra = int(input("how many extra do yo want to add? "))
        sum += amountExtra * 2

def destination():
    global sum
    residentPriceinBsh1=20
    residentPriceObSh2=60

    destnation = input("enter your destnatuion: ")
    if destnation == "beersheba":
        for tr in list1:
            sum += list0[list1.index(tr)] + residentPriceinBsh1
    else:
        for tr in list1:
             sum += list0[list1.index(tr)] + residentPriceObSh2