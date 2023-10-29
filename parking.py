class Garage:
    def __init__(self):
        self.tickets = []
        self.parkingSpaces = []
        self.currentTicket = {}

    def takeTicket(self):
        if not self.tickets:
            print("No tickets available")
                return
        self.tickets.pop(0)
        self.parkingSpaces.pop(0)
        else:
            print("Please, take your ticket.")

    def payForParking(self):
        if not self.currentTicket:
            print("No ticket to pay for.")
            return
        else:
            payment = input("Please enter the amount: ")
            if payment:
                print("Your ticket has been paid, you have 15mins to leave.")
                self.currentTicket["paid"] = True

    def leaveGarage(self):
        if not self.currentTicket:
            print("No ticket to leave.")
        elif not self.currentTicket.get("paid", False):
            payment = input("Please enter the payment amount: ")
            if payment:
                print("Thank you, have a nice day!")
                self.parkingSpaces.append(True)
                self.tickets.append(True)
        else:
            print("Thank you, have a nice day!")
            self.parkingSpaces.append(True)
            self.tickets.append(True)