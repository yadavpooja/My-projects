def login():
    Flag = True
    data = {"riya": "123"}
    while Flag:
        name = raw_input("\nPlease enter your user name: ")
        if name in data:
            pp = raw_input("Please enter your password: ")
            if pp == data[name]:
                print "Logged in successfully.\n Enjoy different services."
            else:
                print "\nPlease enter a valid password."
        if name == "quit":
            Flag = False
            print"You exit"

        elif name not in data:
            print("Hello new user")
            user = raw_input("""Do you want to create your account? \nType y or yes to continue. """)
            if user == "y" or user == "yes":
                user1 = raw_input("\nPlease enter your user name? ")
                pp1 = raw_input("Please enter your password? ")
                data[user1] = pp1
                print("Your account created succesfully,enjoy!!")
                print("Login and continue or type quit to exit.\n Thank You.")









login()
