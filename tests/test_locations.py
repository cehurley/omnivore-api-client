__author__ = 'chadhurley'

from test_base import OmnivoreClientTestBase, main

class TestLocations(OmnivoreClientTestBase):
    def setUp(self):
        super(TestLocations, self).setUp()
        self.location_id = 'Mi8y7jcL'

    def test_list_locations(self):
        res = self.client.locations.list()
        self.assertTrue(isinstance(res['body'], list))
        self.assertTrue('development' in res['body'][0])
        self.assertTrue('display_name' in res['body'][0])

    def test_get_location(self):
        res = self.client.locations.getOne(location_id=self.location_id)
        self.assertTrue(isinstance(res['body'], dict))
        self.assertTrue('development' in res['body'])
        self.assertTrue('display_name' in res['body'])

if __name__ == '__main__':
    main()
