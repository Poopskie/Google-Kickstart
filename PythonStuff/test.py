#-------------------------------------
#  Name:     Jackie Cai
#  Program:  E1CarJC.py
#  Compsci 30 Block 3
#  November 28th 2021
#  This Program is my own work - JC
# ------------------------------------


class car:

    def __init__(self, make, model, year, odometer, colour, price):
        self.make = make
        self.model = model
        self.year = year
        self. odometer = odometer
        self.colour = colour
        self.price = price

    def print_values(self):
        print("This Car's information:", self.make, self.model, self.year, self. odometer, self.colour, self.price, sep = " ")


inventory = []


if __name__ == '__main__':

    cars = int(input("How many cars are you putting in inventory?: "))
    for i in range(cars):

        data = input("Enter data in this order seperated with commas (make, model, year, odometer, colour, price): ")
        data_list = data.split(",")
        for i in range(len(data_list)):
            data_list[i] = data_list[i].replace(" ", "")
        
        inventory.append( car(data_list[0], data_list[1], data_list[2], data_list[3], data_list[4], data_list[5]) )

    for obj in inventory:
        obj.print_values()




















