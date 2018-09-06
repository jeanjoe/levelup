
class BookTicket():

    """Constructor for initializing global variables"""
    def __init__(self):
        self.tickets = []

    """ Function to book ticket"""
    def add_ticket(self, name, email):
        visitor = {
            "fullname": name,
            "email": email
        }
        self.tickets.append(visitor)
        return self.tickets

    def get_ticket(self, email):
        for visitor in self.tickets:
            if visitor['email'] == email:
                return visitor
        return None
    
    def get_ticket_by_name(self, name):
        for visitor in self.tickets:
            if visitor['fullname'] == name:
                return visitor
        return None
        

    def remove_ticket(self, email):
        for visitor in self.tickets:
            if visitor['email'] == email:
                self.tickets.remove(visitor) 

        return None