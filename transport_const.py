class Transport:
    def __init__(self,type):
        self.type=type
    def show(self):
        print("Type of transport:",self.type)
class Bus(Transport):
    def __init__(self,type,seat_no,source,destination):
        super().__init__(type)
        self.seat_no=seat_no
        self.source=source
        self.destination=destination
    def show(self):
        print(self.type)
        print(self.seat_no)
        print(self.source)
        print(self.destination)
ob1=Bus("Road",11,"Howrah","Barasat")     
ob1.show()   