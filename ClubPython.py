# You run a club, and would like to save money on hiring human staff, so you write a virtual “bouncer” program. This bouncer asks the user’s age, 
# and if they are under the age of 18, they are not allowed access.

# RULES
# Have the bouncer ask the user’s age.
# If their age is above 18, have the bouncer allow them in.
# If their age is below 18, have the bouncer reject them entry.

def bouncer():
    age=int(input("Age: "))
    if age>18:
        print("Allowed")
    else:
        print("Not Allowed")

bouncer()