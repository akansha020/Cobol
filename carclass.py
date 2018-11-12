import pdb
class Vehicle:
    name = ""
    kind= "car"
    color= ""
    value = 100.00
    def description(self):
        dec_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind
        ,self.value)
        return dec_str
    
car1 = Vehicle()
car1.name = "Fed"
car1.color ="blue"
car1.kind = "convertible"
car1.value = 200.00

car2 = Vehicle()
car2.name = "Jump"
car2.color = "red"
car2.kind = "van"
car2.value = 3000.00
print(car1.description())
print(car2.description())
