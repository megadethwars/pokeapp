import unittest
import os
import json
from app import create_main_app


class pokeAPITest(unittest.TestCase):
    """
    API Test Case
    """


    def setUp(self):
        self.app = create_main_app()
        self.client = self.app.test_client

    def test_third_party_manager(self):

        """ test get sequence info válida """
        res = self.client().get(
            "/api/v1/pocket/allBerryStats",
            headers={"Content-Type": "application/json"},
        )
        jd = json.loads(res.data)
        self.assertEqual(res.status_code, 200)

        """ test get sequence info válida """
        res = self.client().get(
            "/api/v1/pocket/allBerryStats/hist",
            headers={"Content-Type": "application/json"},
        )
        jd = json.loads(res.data)
        self.assertEqual(res.status_code, 200)

if __name__ == "__main__":
    unittest.main()