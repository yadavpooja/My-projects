#Program to generate a random password of length 5 to 10 length having
#weak,strong and excellent strength, and pressing 0 program exit.



import random
Flag = True
while Flag:

    length = int(input("Please enter the length of password between 5 to 10: "))
   # if length not in range(5,11):
    #    print("Please enter a valid length")
    if length == 0:
        Flag = False
        print" You exit"
        break
    elif length not in range(5,11):
        print("Please enter a valid length")
    else:
        
        print("1- weak")
        print("2-strong")
        print("3-excellent")
        strength = int(input("Please select the strength: "))
        data = "QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm"
        data1 = "QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm1234567890"
        data2 = "QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm1234567890!@#$%^&*()_+<>?/"

        if strength == 1:
            print(" ".join(random.sample(data,length)))
        elif strength == 2:
            print("".join(random.sample(data1,length)))
        elif strength == 3:
            print("".join(random.sample(data2,length)))
        elif strength == 0 :
            Flag = False
            print("You exit")
        else:
            print("Please select correct strength for your password")

