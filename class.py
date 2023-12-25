class flight():
    def __init__(self,capacity):
        self.capacity = capacity
        self.passengers = []

    def add_passengers(self, name):
        if not self.open_seats():
            return False
        self.passengers.append(name)
        return True

    def open_seats(self):
        return self.capacity - len(self.passengers)

Flight = flight(3)

people = ["Yunisha", "Hima", "Yojana", "Sumina"]
for person in people:
     
    if Flight.add_passengers(person):
        print(f"Added {person} to flight successfully.")
    else:
        print(f"no avaiable seats for {person}")