namelist=[]
def storename():
    name=input("Enter the name to be saved:")
    name=name.strip().title()
    namelist.append(name)
    return name

def listnames():
    print("*"*30)
    print("Names in the list")
    print("*"*30)
    for name in namelist:
        print(name)
    print("*"*30)

def searchName(search):
    search=search.strip().tittle()
    found = False
    for name in namelist:
        if name == search:
            found = True
            break
    if found == True:
        print("Name exist in the list")
    else:
        print("Name doesn't exit....!")

while True:
        print("*"*30)
        print("1.Enter a name")
        print("2.list of names")
        print("3.search for a name")
        print("4.exit")
        print("*"*30)

        choice=int(input("Enter the choice:"))
        print("choice entered:",choice)
        if choice==1:
            name=input("Enter the name:")
        elif choice==2:
            listnames(name)
        elif choice==3:
            searchName(name)
        elif choice==4:
            break