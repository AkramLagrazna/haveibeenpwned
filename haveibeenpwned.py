import requests
import pprint

print("-----------------------------")
print("Welcome to \"Have i been Pwned?\"")
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
        jsonn = connection.json()
        pp = pprint.PrettyPrinter(indent=1)
        pp.pprint(jsonn)
        print pp
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
        
        
        
