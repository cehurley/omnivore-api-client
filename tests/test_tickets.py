__author__ = 'chadhurley'

from test_base import OmnivoreClientTestBase, main

class TestTickets(OmnivoreClientTestBase):
    def setUp(self):
        super(TestTickets, self).setUp()
        self.location_id = 'Mi8y7jcL'
        self.ticket_id = '5cL9KETx'

    def test_create_ticket(self):
        data= {
          "employee": "MjikgioG",
          "order_type": "KxiAaip5",
          "revenue_center": "gdTMpTKz",
        }
        res = self.client.tickets.create(location_id=self.location_id, data=data)
        self.assertTrue(isinstance(res['body'], dict))
        self.assertTrue('opened_at' in res['body'])
        self.assertTrue('ticket_number' in res['body'])
        self.assertTrue('totals' in res['body'])

    def test_get_ticket(self):
        res = self.client.tickets.getOne(location_id=self.location_id,
                                         ticket_id = self.ticket_id)
        self.assertTrue(isinstance(res['body'], dict))
        self.assertTrue('opened_at' in res['body'])
        self.assertTrue('ticket_number' in res['body'])
        self.assertTrue('totals' in res['body'])

if __name__ == '__main__':
    main()
