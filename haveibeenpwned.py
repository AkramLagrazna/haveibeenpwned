import requests
import json

print("-----------------------------")
print("Welcome to \"Have i been Pwned?\" v1.1")
print("-----------------------------")
par = {
    "truncateResponse" : "true"
    }
y = 'y'
n = 'n'
active = 0
while active != 1:
    email = raw_input("Enter your e-mail please.  ")
    connection = requests.get("https://haveibeenpwned.com/api/v2/breachedaccount/"+str(email))
    if connection.status_code is 200:
        print("Connected..")
        print("Printing output..")
        try:
            variabile = 5
            for i in range(0,variabile):
                print("Printing Hacked Details. ")
                print("Domain       :  "+str(connection.json()[i]['Domain']))
                print("Info Hacked  :  "+str(connection.json()[i]['DataClasses']))
                print("Name         :  "+str(connection.json()[i]['Name']))
                print("Dump Verified:  "+str(connection.json()[i]['IsVerified']))
                print("Description  :  "+str(connection.json()[i]['Description']))
                print('')
                print('..')
        except IndexError:
                      variabile = i
        
        
        
        
            
        exitt = raw_input("You want to search another e-mail?  ")
        if exitt is n:
            print("Perfect. bye bye!")
            active = 1
        else:
            print("Perfect, let's search for another e-mail!")
    elif connection.status_code is 404:
        print("GOOD NEWS!")
        print("Nothing to worry about!")
        print("You got no hacked passwords!")
        exitt = raw_input("You want to search another e-mail?  ")
        if exitt is n:
            print("Perfect. bye bye!")
            active = 1
        else:
            print("Perfect, let's search for another e-mail!")
    else:
        print("Error connecting..")
        exitt = raw_input("You want to search another e-mail?  ")
        if exitt is n:
            print("Perfect. bye bye!")
            active = 1
        else:
            print("Perfect, let's search for another e-mail!")
