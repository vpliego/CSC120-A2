class Computer:
    # this will probably need to have the date, model, of the computer, etc.
    #In order to give the main something to call back to, we can define the attributes below and give them the names used in the main. 
    def __init__(self, description, processor_type, hard_drive_capacity, memory, operating_system, year_made, price):
        self.description = description
        self.processor_type = processor_type
        self.hard_drive_capacity = hard_drive_capacity 
        self.memory = memory 
        self.operating_system = operating_system 
        self.year_made = year_made
        self.price = price 

# using this method so that we are able to update the price of a computer.
    def update_price(new_price): 
        price = new_price
# this should be able to update the operating_system information. 
    def update_os(new_os):
        operating_system = new_os


# What attributes will it need?
     
    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    # type = type
    # string model, string processor, int storage, int space, string interface, int year, int

    # What methods will you need?