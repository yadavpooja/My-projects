#calculate the distance from the origin#
import math
class Distance():
    def __init__(self,name,x= 0,y = 0):
            self.name = name
            self.x = x
            self.y = y

    def get_distance(self):
        return int(((self.x **2) + (self.y ** 2)) ** 0.5)


def dis(name, x,y):
    try:
        x = int(x)
        y = int(y)
        a = Distance(name,x,y)
        ans = a.get_distance()
        if x == 0 or y == 0:
            return 0
        else:
            return ans
    except ValueError:
        return 1
    except SyntaxError:
        return 2


if __name__ == "__main__":
    Flag = True
    while Flag:
        name = raw_input("Enter the name: ")
        #try:
        x = raw_input("Enter your first co-ordinate: ")
        y = raw_input("Enter your second co-ordinate: ")
        result = dis(name, x,y)
        if not result:
            Flag = False
        elif result == 1:
            print("Enter a integer")
        elif result == 2:
            print("Enter a integer")
        else:
           # a = Distance(x,y)
            print ("%s have to cover %d km distance." %(name.title(),result))

       # except NameError:
        #    print("Enter a integer")
       # except SyntaxError:
        #    print("Enter a integer")



