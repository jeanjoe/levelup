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
        
        self.assertEqual(bookTicket.add_ticket("Manzede Benard", "manzede@gmail.com"), 
            [ {"fullname": "Manzede Benard", "email": "manzede@gmail.com" }])
        self.assertEqual(len(bookTicket.tickets), 1)

    def test_get_ticket_by_email(self):
        bookTicket = BookTicket()
        bookTicket.add_ticket("Manzede Benard", "manzede@gmail.com")
        self.assertEqual(bookTicket.get_ticket("manzede@gmail.com"), 
            {"fullname": "Manzede Benard", "email": "manzede@gmail.com" })

    def test_ticket_not_found(self):
        bookTicket = BookTicket()
        self.assertIsNone(bookTicket.get_ticket("annonymous@gmail.com"))

    def test_remove_ticket(self):
        bookTicket = BookTicket()
        bookTicket.add_ticket("Manzede Benard", "manzede@gmail.com")
        bookTicket.remove_ticket("manzede@gmail.com")
        self.assertEqual(len(bookTicket.tickets), 0)

