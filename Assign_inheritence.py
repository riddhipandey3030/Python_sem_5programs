class Transport:
    def get_val(self):
        self.type=input("Enter the name of the Transport: ")
    def show(self):
        print("Type of Transport:",self.type)
class Bus(Transport):
    def input_val(self,seat_no,source,destination):
        print("Seat no: ",seat_no)
        print()