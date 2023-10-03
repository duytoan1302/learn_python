aliens = 2
password="ALIENS"
print("Hurry up the aliens is attack we!")
print("You must use security system is up immediately!")
print("Hope you know the password, for the future of the earth")
print()
print("---------------------------------------------------------------------------")
print("Welcome to the security system all the earth")
print("---------------------------------------------------------------------------")
print()
guess = input("Please enter password:").upper()
while guess != password:
    print()
    print("The password is false.")
    print()
    aliens=aliens**2
    print("Have" ,aliens, "aliens the earth.Please try again")
    if aliens > 740000:
        break
    print()
    print("suggest the password:The things are attacking us.")
    print()
    guess = input("Hury up!Please fill in the diffrent").upper()
    
if aliens > 740000:
    print("Noooooo!The alien is outnumbe the people in the earth.we is lost.")
else:
    print("yeah!We or win.")
    
