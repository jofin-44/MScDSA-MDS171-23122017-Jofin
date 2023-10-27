#create a petstore class where you have the details of pets available and their details.
#The class will whave methods
#-Store a new pet details
#-search for a pet
#-Sell a pet
#-List of all pets

#importing your pet store class, create a petstore remain file,where you will implement a menudrive program for admin - who will mange the store &
#...user who will see the pets and buy pets.
class petstore:
    def __init__(self):
        self.pets=[
            {"name" : "cat",
             "colour": "gold",
             "age" : "1",
             "status" : "available"
             },
            {"name" : "dog",
             "colour" : "brown",
             "age" : "2",
             "status" : "available"
             },
            {"name" : "rabbit",
             "colour" : "white",
             "age" : "3",
             "status" : "available"
             }]
    def addpet(self):
        n=int(input("number of pets to be added:"))
        for i in range(1,n+1,1):
            name = input("Enter the name:")
            colour = input("Enter the colour of the pet:")
            age = input("Enter the age:")
            status = input("Enter the status of pet:")
            newpet={"name" : name,"colour": colour,"age" : age,"status" : status}
            self.pets.append(newpet)
            print(newpet)

        print(self.pets)
a=petstore()
a.addpet()
