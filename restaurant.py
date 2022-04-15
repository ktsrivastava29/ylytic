class Restaurant():

    def __init__(self, restaurant_name,cuisine_type, served=0):
        self.restaurant = restaurant_name
        self.cuisine = cuisine_type
        self.served = served


    def describe_restaurant(self):
        print("\n==========This is our restaurant " + self.restaurant.title() + "===============")
        print("We serve you amazing " + self.cuisine + " 's cusine")


    def open_restaurant(self):
        print("The restaurant is open now ")


    def customers_table(self, numOfcustomer):
        if((numOfcustomer%2==0) and (numOfcustomer<=12)):
            print("Allowed")


    def reservation_time(self, time):
        if((time >=17) and (time>=23)):
            print("You can register")


    def set_number_served(self,served):
        self.served = served
        
    def increment_number_served(self,additional_served):
        self.served += additional_served

restaurant = Restaurant('Plaza','vietnamese')
restaurant.describe_restaurant()


print("\nNumber served: " + str(restaurant.served))
restaurant.served = 430

print("Number served: " + str(restaurant.served))
restaurant.increment_number_served(1257)

print("Number served: " + str(restaurant.served))
restaurant.increment_number_served(239)

print("Number served: " + str(restaurant.served))






