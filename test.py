import pytest
import requests
import main
from .test.pokeApiTest import *

def test_index():
    main.app.testing = True
    client = main.app.test_client()

    r = client.get("/")
    assert r.status_code == 200

