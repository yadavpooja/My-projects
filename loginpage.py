def login(username, password, data):
    if name in data:
        if data[name] == password:
            return 0
        else:
            return 1
    return 2

def register(username, password, data):
    if name not in data:
        data[name] = password
    return data


if __name__ == '__main__':
    Flag = True
    data = {"riya": "123"}
    while Flag:
        name = raw_input("\nPlease enter your user name: ")
        if name == "quit":
            Flag = False
            print"You exit"
        else:
            pp = raw_input("Please enter your password: ")
            login_result = login(name, pp, data)
            #import pdb; pdb.set_trace()
            if not login_result:
                print "Logged in successfully.\n Enjoy different services."
            elif login_result == 1:
                print "\nPlease enter a valid password."
            else:
                print("Hello new user")
                user = raw_input("""Do you want to create your account? \nType y or yes to continue. """)
                if user == "y" or user == "yes":
                    data = register(name, pp, data)
                    print("Your account created succesfully,enjoy!!")
                    print("Login and continue or type quit to exit.\n Thank You.")
