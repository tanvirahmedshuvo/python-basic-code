#********Single Inheritance*******

# class Vehicle:
#     def general_usage(self):
#         print("General use: transporation")

# class car(Vehicle):
#     def __init__ (self):
#         print("I'm car")
#         self.wheels = 4 
#         self.has_roof = True
    
#     def specific_usage(self):
#         self.general_usage()
#         print("specific use: commute to work, vacation with family")

# class motorCycle(Vehicle):
#     def __init__ (self):
#         print("I'm motorcycle")
#         self.wheels = 2 
#         self.has_roof = False
    
#     def specific_usage(self):
#         self.general_usage()
#         print("specific use: road trip, racing")


# c = car()
# c.specific_usage()
# print(isinstance(c,car))

# m = motorCycle()
# m.specific_usage()


#********** Multiple Inheritance***********

class Father():
    def skills(self):
        print("gardening,programming")

class Mother():
    def skills(self):
        print("coocking,art")

class child(Father,Mother):
    def skills(self):
        Father.skills(self)
        Mother.skills(self)
        print("sport")


c = child()
c.skills()