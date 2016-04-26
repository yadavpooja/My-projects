def Vehicle():
    dict = {1:50, 2:10,3:20,4:100,5:5}
    total_tax = 0
    car_count,car_tax = 0,0
    bus_count,bus_tax = 0,0
    bike_count,bike_tax = 0,0
    truck_count,truck_tax = 0,0
    auto_count,auto_tax = 0,0
    flag = True
    print("Enter the choice for vehicle")
    print("1. Car,50")
    print("2. Bus,10")
    print("3. Bike,20")
    print("4. Truck,100")
    print("5. Auto,5")
    while flag == True:
        user = int(input("enter the vehicle code: "))
        if user not in range(6):
            print "Please specify a correct vehicle id"
        if user == 1:
            car_count += 1
            print "car  no %d " %car_count
            #print car_tax
            if car_count > 3:
                print "entry restricted"
            else:
                print "welcome and pay tax 50rupees"
                car_tax += 50

        if user == 2:
            bus_count += 1
            print "bus no %d" %(bus_count)
            if bus_count > 2:
                print "no entry for today"
            else:
                print"welcome and pay tax 10rupees"
                bus_tax += 10

        if user == 3:
            bike_count += 1
            print "Bike no %d" %(bike_count)
            if bike_count > 5:
                print "no entry now"
            else:
                print"welcome and pay tax 20rupees"
                bike_tax += 20

        if user == 4:
            truck_count += 1
            print "truck no %d " %(truck_count)
            if truck_count > 2:
                print "no entry for heavy vehicles now"
            else:
                print "welcome and pay tax 50rupees"
                truck_tax += 100


        if user == 5:
            auto_count += 1
            auto_tax += 5
            print "auto no %d" %(auto_count)
            print"welcome and pay tax 5 rupees"

        if user == 0:
            result = car_tax + bus_tax + bike_tax + truck_tax + auto_tax
            total_tax += result


            flag = False
            print "submit the total tax %d rupees" %(total_tax)




Vehicle()
