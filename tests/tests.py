import unittest
from models.bookticket import BookTicket

class TestBookTicket(unittest.TestCase):

    def setUp(self):
        """Instanciate BookTicket class and add a visitor."""
        self.bookTicket = BookTicket()
        self.bookTicket.add_ticket("Manzede Benard", "manzede@gmail.com")

    def test_book_ticket_class(self):
        """Test existence of BookTicket class."""
        self.assertIsInstance(self.bookTicket, BookTicket)

    def test_instance_of_tickets_to_be_list(self):
        """Test tickets to be instance of list."""
        self.assertIsInstance(self.bookTicket.tickets, list)

    def test_length_of_tickets(self):
        """Test length of tickets."""
        self.assertEqual(len(self.bookTicket.tickets), 1)

    def test_add_ticket(self):
        """Test add Ticket to the list."""
        self.assertEqual(self.bookTicket.add_ticket("jean", "jean@gmail.com"), 
            [ {'email': 'manzede@gmail.com', 'fullname': 'Manzede Benard'}, 
            {"fullname": "jean", "email": "jean@gmail.com" }])
        self.assertEqual(len(self.bookTicket.tickets), 2)

    def test_get_ticket_by_email(self):
        """Test get ticket by email."""
        self.assertEqual(self.bookTicket.get_ticket("manzede@gmail.com"), 
            {"fullname": "Manzede Benard", "email": "manzede@gmail.com" })

    def test_get_ticket_by_name(self):
        """Test get ticket by email."""
        self.assertEqual(self.bookTicket.get_ticket_by_name("Manzede Benard"), 
            {"fullname": "Manzede Benard", "email": "manzede@gmail.com" })

    def test_ticket_not_found(self):
        """Test ticket not found."""
        self.assertIsNone(self.bookTicket.get_ticket("annonymous@gmail.com"))

    def test_remove_ticket(self):
        """Test remove ticket."""
        self.bookTicket.remove_ticket("manzede@gmail.com")
        self.assertEqual(len(self.bookTicket.tickets), 0)

    def test_remove_ticket_not_found(self):
        """Test remove ticket not found."""
        self.assertIsNone(self.bookTicket.remove_ticket("annonymous@gmail.com"))

    def tearDown(self):
        """Empty the ticket list."""
        self.bookTicket.tickets = []