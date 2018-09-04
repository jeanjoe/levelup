import unittest
from models.bookticket import BookTicket

class TestBookTicket(unittest.TestCase):

    def test_book_ticket_class(self):
        bookticket = BookTicket()
        self.assertIsInstance(bookticket, BookTicket)

    def test_instance_of_tickets_to_be_list(self):
        bookTicket = BookTicket()
        self.assertIsInstance(bookTicket.tickets, list)

    def test_book_ticket(self):
        bookTicket = BookTicket()
        
        self.assertEqual(bookTicket.book_ticket("Manzede Benard", "manzede@gmail.com"), 
            [ {"fullname": "Manzede Benard", "email": "manzede@gmail.com" }])
        self.assertEqual(len(bookTicket.tickets), 1)

    def test_get_ticket(self):
        bookTicket = BookTicket()
        bookTicket.book_ticket("Manzede Benard", "manzede@gmail.com")
        self.assertEqual(bookTicket.get_ticket("manzede@gmail.com"), 
            {"fullname": "Manzede Benard", "email": "manzede@gmail.com" })


