import unittest
from models.bookticket import BookTicket

class TestBookTicket(unittest.TestCase):

    def test_book_ticket_class(self):
        bookticket = BookTicket()
        self.assertIsInstance(bookticket, BookTicket())

    def test_instance_of_tickets_to_be_list(self):
        bookTicket = BookTicket()
        self.assertIsInstance(bookTicket.tickets, list)
