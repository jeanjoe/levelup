import unittest
from models.bookticket import BookTicket

class TestBookTicket(unittest.TestCase):

    #Instanciate BookTicket class and add a visitor
    def setUp(self):
        self.bookTicket = BookTicket()
        self.bookTicket.add_ticket("Manzede Benard", "manzede@gmail.com")

    #Test existence of BookTicket class
    def test_book_ticket_class(self):
        self.assertIsInstance(self.bookTicket, BookTicket)

    #Test tickets to be instance of list
    def test_instance_of_tickets_to_be_list(self):
        self.assertIsInstance(self.bookTicket.tickets, list)

    #Test add Ticket to the list
    def test_add_ticket(self):
        self.assertEqual(self.bookTicket.add_ticket("jean", "jean@gmail.com"), 
            [ {'email': 'manzede@gmail.com', 'fullname': 'Manzede Benard'}, 
            {"fullname": "jean", "email": "jean@gmail.com" }])
        self.assertEqual(len(self.bookTicket.tickets), 2)

    #Test get ticket by email
    def test_get_ticket_by_email(self):
        self.assertEqual(self.bookTicket.get_ticket("manzede@gmail.com"), 
            {"fullname": "Manzede Benard", "email": "manzede@gmail.com" })

    #Test ticket not found
    def test_ticket_not_found(self):
        self.assertIsNone(self.bookTicket.get_ticket("annonymous@gmail.com"))

    #Test remove ticket
    def test_remove_ticket(self):
        self.bookTicket.remove_ticket("manzede@gmail.com")
        self.assertEqual(len(self.bookTicket.tickets), 0)

    #Empty the ticket list
    def tearDown(self):
        self.bookTicket.tickets = []

