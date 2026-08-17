#Create a class Transport with variable type.Create two child classes Boat and Bus with variables,Boat has 
#capacity,source,destination and Bus has the variables seat_no,source,destination.
#Initialize all the variables of all the classes with constructor.Define show() method in 
#transport class to display the type of transport.Define show() method in Boat class to 
# display the records of Boat and define another Show() method in Bus class.
# Create two Objects of the Boat class and two objects of the Bus class.
#-------------------------------------------------------------------------------------------

class Transport:
    def __init__(self,type):
        self.type=type
    def show(self):
        print("Type of transport",self.type)
class Boat(Transport):
    def __init__(self,type,capacity,source,destination):
        super().__init__(type)
        self.capacity=capacity
        self.source=source
        self.destination=destination
    def show(self):
        super().show()
        print("Capacity: ",self.capacity)
        print("Source: ",self.source)
        print("Destination: ",self.destination)
class Bus(Transport):
    def __init__(self,type,seat_no,source,destination):
        super().__init__(type)
        self.seat_no=seat_no
        self.source=source
        self.destination=destination
    def show(self):
        super().show()
        print("Seat number: ",self.seat_no)
        print("Source: ",self.source)
        print("Destination: ",self.destination)
ob1=Boat("Water",10,"howrah","princep ghat")
ob2=Boat("Water",12,"jaipur","jaisalmer")
ob3=Bus("Road",12,"barasat","dumdum")
ob4=Bus("Road",14,"Dhanbad","Ranchi")
ob1.show()
ob2.show()
ob3.show()
ob4.show()


