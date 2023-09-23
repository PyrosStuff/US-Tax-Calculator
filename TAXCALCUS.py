print("Welcome to the US sales tax calculator!")
print("COUNTIES")
print("1: Florida")
print("2: Georgia")
print("3: Tennesee")
print("4: South Carolina")
print("5: North Carolina")
print("6: Alabama")
print("7: Mississippi")
tax = 0
state = 0
state = int(input("Please enter your state number: "))
if state == 1:
    print("You have selected: Florida.")
    flcounty = 0
    flcounty = int(input("Select your county. "))
elif state == 2:
    print("You have selected: Georgia.")
    gacounty = 0
    gacounty = int(input("Select your county. "))
elif state == 3:
    print("You have selected: Tennessee.")
    tncounty = 0
    tncounty = int(input("Select your county. "))
elif state == 4:
    print("You have selected: South Carolina.")
    sccounty = 0
    sccounty = int(input("Select your county. "))
elif state == 5:
    print("You have selected: North Carolina.")
    nccounty = 0
    nccounty = int(input("Select your county. "))
elif state == 6:
    print("You have selected: Alabama.")
    alcounty = 0
    alcounty = int(input("Select your county. "))
elif state == 7:
    print("You have selected: Mississippi.")
    mscounty = 0
    mscounty = int(input("Select your county. "))