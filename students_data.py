class Student():
    def __init__(self,name,mother_name,father_name,dob,roll_no,fees,status=False):
        self.name = name
        self.mother_name = mother_name
        self.father_name = father_name
        self.dob = dob
        self.roll_no = roll_no
        self.fees = fees
        self.status = status

    def get_detail(self):
        print(("name: %s\nmother_name: %s\nfather_name: %s\n"
        "dob: %s\nroll_no: %d") \
        %(self.name,self.mother_name,self.father_name,self.dob,self.roll_no))


    def fees_detail(self):
        if self.status:
            print "Fees paid"
        else:
            print "%s have to pay %drupees" %(self.name,self.fees)



a = Student("jai","lara","roy","1 may 2011",1,1000,True)
b = Student("david","joe","jack","1 june 2010",3,2000)
a.get_detail()
a.fees_detail()
b.get_detail()
b.fees_detail()
