def Vehicle():
    tax = {1:50, 2:10,3:20,4:100,5:5}
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
                car_tax += tax.get(user)

        if user == 2:
            bus_count += 1
            print "bus no %d" %(bus_count)
            if bus_count > 2:
                print "no entry for today"
            else:
                print"welcome and pay tax 10rupees"
                bus_tax += tax.get(user)

        if user == 3:
            bike_count += 1
            print "Bike no %d" %(bike_count)
            if bike_count > 5:
                print "no entry now"
            else:
                print"welcome and pay tax 20rupees"
                bike_tax += tax.get(user)

        if user == 4:
            import datetime
            truck_time = datetime.datetime.now()
            tt = truck_time.hour
            if 6 > tt > 24:
                truck_count += 1
                print "truck no %d " %(truck_count)
                print "welcome and pay tax 50rupees"
                truck_tax += tax.get(user)
            else:
                print "entry allowed after 24hours"


        if user == 5:
            auto_count += 1
            auto_tax += tax.get(user)
            print "auto no %d" %(auto_count)
            print"welcome and pay tax 5 rupees"

        if user == 0:
            result = car_tax + bus_tax + bike_tax + truck_tax + auto_tax
            total_tax += result


            flag = False
            print "submit the total tax %d rupees" %(total_tax)




Vehicle()
