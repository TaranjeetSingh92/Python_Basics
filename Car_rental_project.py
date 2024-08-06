from datetime import datetime
import time
class Rental_Cars:
    def __init__(self):
        self.available_cars=73
        self.rent_car=None
        self.booktime=None
        self.rental_mode=None
        self.returntime=None
    def available_car(self):
        print("Total available Cars are:",self.available_cars)
    def booking_time(self):
        self.booktime=datetime.now()
        return self.booktime
    def renting_hourly(self):
        rent_hourly=int(input("Enter the Number of cars you want to rent hourly:"))
        if rent_hourly > 0 and rent_hourly <=self.available_cars:
            self.rent_car=rent_hourly
            self.available_cars=self.available_cars-self.rent_car
            print("You booked ",self.rent_car," cars at ",self.booking_time())
        elif rent_hourly <=0:
            print("You Entered Invalid Numebr")
        else:
            print(rent_hourly," Cars Not avaiable at this time")
            
    def renting_daily(self):
        rent_daily=int(input("Enter the Number of cars you want to rent daily"))
        if rent_daily > 0 and rent_daily <=self.available_cars:
            self.rent_car=rent_daily
            self.available_cars=self.available_cars-self.rent_car
            print("You booked ",self.rent_car," cars at ",self.booking_time())
        elif rent_daily <=0:
            print("You Entered Invalid Numebr")
        else:
            print(rent_daily," Cars Not avaiable at this time")
        
    def renting_weekly(self):
        rent_weekly=int(input("Enter the Number of cars you want to rent weekly"))
        if rent_weekly > 0 and rent_weekly <=self.available_cars:
            self.rent_car=rent_weekly
            self.available_cars=self.available_cars-self.rent_car
            print("You booked ",self.rent_car," cars at ",self.booking_time())
        elif rent_weekly <=0:
            print("You Entered Invalid Numebr")
        else:
            print(rent_weekly," Cars Not avaiable at this time")

    def return_car(self):
        print("You have rented:",self.rent_car)
        print("Your rent mode is:",self.rental_mode)
        print("Your Book time was:",self.booktime)
        self.returntime=datetime.now()
        print("Your return time is:",self.returntime)
        self.available_cars=self.available_cars+self.rent_car
        rental_period=self.returntime-self.booktime
        print("Your rental Period is:",rental_period)
        print("Your Invoice is generated please pay the bill,thanks")
        
    def renting_car(self):
        print("Rent a car 1.Hourly 2.Daily 3.Weekly")
        choose=input("Choose any of above option else press any other key:")
        if choose=="1":
            self.rental_mode="hourly"
            self.renting_hourly()
        elif choose=="2":
            self.rental_mode="daily"
            self.renting_daily()
        elif choose=="3":
            self.rental_mode="weekly"
            self.renting_weekly()
        else:
            print("Bye,Have a Nice Day")
        
        print("You Need to return cars now")
        print("Please wait,processing return request...")
        time.sleep(60)
        self.return_car()

class Customer(Rental_Cars):
    def __init__(self):
        super().__init__()
        
    def availablecars(self):
        self.available_car()
    def rentcar(self):
        self.renting_car()
    def options(self):
        print("----------------------WELCOME---------------------")
        while(True):
            c_input=int(input("Enter 1 to check available cars, 2 to rent a car, Press any other key to exit:"))    
            if c_input==1:
                self.availablecars()
            elif c_input==2:
                self.rentcar()
            else:
                print("Bye,have a nice day,thanks")
                break
        
customer1=Customer()
customer1.options()