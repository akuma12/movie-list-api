import json

import pytest

from api.movies import app


@pytest.fixture()

def test_get_movies():
    # Testing the get_movies method
