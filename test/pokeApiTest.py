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

        self.response={
        "berries_names": [
        "cheri",
        "chesto",
        "pecha",
        "rawst",
        "aspear",
        "leppa",
        "oran",
        "persim",
        "lum",
        "sitrus",
        "figy",
        "wiki",
        "mago",
        "aguav",
        "iapapa",
        "razz",
        "bluk",
        "nanab",
        "wepear",
        "pinap"
        ],
        "frequency_growth_time": {
        "2": 5,
        "3": 5,
        "4": 3,
        "5": 5,
        "8": 1,
        "12": 1
        },
        "max_growth_time": 12,
        "mean_growth_time": 4.1,
        "median_growth_time": 4,
        "min_growth_time": 2,
        "variance_growth_time": 5.78
        
    }

    def test_poke_api(self):

        """ test get sequence info válida """
        res = self.client().get(
            "/api/v1/pocket/allBerryStats",
            headers={"Content-Type": "application/json"},
        )
        jd = json.loads(res.data)
        self.assertEqual(jd.get("data"), self.response)
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