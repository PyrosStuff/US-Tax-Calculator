print("Welcome to the US sales tax calculator!")
print("STATES")
print("1: Florida")
print("2: Georgia")
print("3: Tennesee")
print("4: South Carolina")
print("5: North Carolina")
print("6: Alabama")
print("7: Mississippi")
print("8: Virginia")
print("9: West Virginia")
print("10: Louisiana")
print("11: Arkansas")
print("12: Kentucky")
tax = 0
state = 0
state = int(input("Please enter your state number: "))
if state == 1:
    print("You have selected: Florida.")
    flcounty = 0
    print("County group 1: Alucha, Bay, Bradford, Calhoun, Clay, Collier, Columbia, Desoto, Duval, Escambia, Franklin, Gadsden, Gilchrist, Glades, Gulf, Hamilton, Hardee, Hendry, Highlands, Hillsborough, Holmes, Jackson, Jefferson, Lafayette, Lee, Leon, Levy, Liberty, Madison, Marion, Monroe, Nassau, Okeechobee, Orange, Osceola, Pasco, Pinellas, Polk, Putnam, Santa Rosa, Saint Johns, Suwannee, Wakulla, Walton, Washington")
    print("County group 2: Baker, Brevard, Broward, Charlotte, Dixie, Flagler, Hernando, Indian River, Lake, Manatee, Martin, Miami-Dade, Okaloosa, Palm Beach, Sarasota, Seminole, Saint Lucy, Sumter, Taylor, Union, Volusia")
    flcounty = int(input("Select your county group. "))
    if flcounty == 1:
        print("You have selcted county group: 1")
        tax == .075
    elif flcounty == 2:
        print("You have selected county group: 2")
        tax == .07
    elif flcounty == 3:
        print("You have selected county group: 3")
        tax == .065
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
elif state == 8:
    print("You have selected: Virginia.")
    vicounty = 0
    vicounty = int(input("Select your county. "))
elif state == 9:
    print("You have selected: West Virginia.")
    wvcounty = 0
    wvcounty = int(input("Select your county. "))
elif state == 10:
    print("You have selected: Louisiana.")
    locounty = 0
    mscounty = int(input("Select your county. "))
elif state == 11:
    print("You have selected: Arkansas.")
    arcounty = 0
    arcounty = int(input("Select your county. "))
elif state == 12:
    print("You have selected: Kentucky.")
    kecounty = 0
    kecounty = int(input("Select your county. "))
