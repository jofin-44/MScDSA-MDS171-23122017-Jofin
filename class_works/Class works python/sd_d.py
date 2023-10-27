#details of students in the class
print("details of students in the class")
list_d=[]
sd={}
def store():
    Name=input("Name:")
    Register_no=int(input("Enter the reg_no.:"))
    Phone=int(input("Enter the phone number:"))
    Email=input("Enter the email:")
    return Name,Register_no,Phone,Email
def sd_d():
    Name.strip().title()
    list_d.append(Name)
    Register_no.strip().title()
    list_d.append(Register_no)
    Phone.strip().title()
    list_d.append(Phone)
    Email.strip.title()
    list_d.append(Email)
sd_d()
print(list_d)