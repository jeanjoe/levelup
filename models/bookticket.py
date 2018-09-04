
class BookTicket():

    """Constructor for initializing global variables"""
    def __init__(self):
        self.tickets = []

    """ Function to book ticket"""
    def book_ticket(self, name, email):
        visitor = {
            "fullname": name,
            "email": email
        }
        self.tickets.append(visitor)
        return self.tickets
        