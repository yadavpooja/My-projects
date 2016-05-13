#calculate the distance from the origin#




class Distance():
    def __init__(self,x= 0,y = 0):
            self.x = x
            self.y = y

    def get_distance(self):
        return ((self.x **2) + (self.y ** 2)) ** 0.5


def dis():
    Flag = True
    while Flag:
        name = raw_input("Enter the name: ")
        try:
            x = int(input("Enter your first co-ordinate: "))
            y = int(input("Enter your second co-ordinate: "))
            if x == 0 or y == 0:
                Flag = False
            else:
                a = Distance(x,y)
                print ("%s have to cover %d km distance." %(name.title(),a.get_distance()))

        except NameError:
            print("Enter a integer")
        except SyntaxError:
            print("Enter a integer")


dis()
